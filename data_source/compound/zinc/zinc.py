""" The ``data_source.compound.zinc`` package ``zinc`` module. """

from logging import Logger
from os import PathLike
from re import findall
from typing import Dict, Optional, Union

from data_source.base.base import BaseDataSource
from data_source.base.utility.download import BaseDataSourceDownloadUtility

from data_source.compound.zinc.utility.download import ZINCCompoundDatabaseDownloadUtility
from data_source.compound.zinc.utility.extraction import ZINCCompoundDatabaseExtractionUtility
from data_source.compound.zinc.utility.formatting import ZINCCompoundDatabaseFormattingUtility


class ZINCCompoundDatabase(BaseDataSource):
    """ The `ZINC <https://zinc20.docking.org>`_ chemical compound database class. """

    def __init__(
            self,
            logger: Optional[Logger] = None
    ) -> None:
        """
        The constructor method of the class.

        :parameter logger: The logger. The value `None` indicates that the logger should not be utilized.
        """

        super().__init__(
            logger=logger
        )

    def get_supported_versions(
            self
    ) -> Dict[str, str]:
        """
        Get the supported versions of the database.

        :returns: The supported versions of the database.
        """

        try:
            supported_versions = dict()

            for file_name in findall(
                pattern=r"href=\"([^\.]+)\.smi\.gz",
                string=BaseDataSourceDownloadUtility.send_http_get_request(
                    http_get_request_url="https://files.docking.org/bb/current"
                ).text
            ):
                supported_versions[
                    "v_building_blocks_{file_name:s}".format(
                        file_name=file_name
                    )
                ] = "https://doi.org/10.1021/acs.jcim.0c00675"

            for file_name in findall(
                pattern=r"href=\"([^\.]+)\.src\.txt",
                string=BaseDataSourceDownloadUtility.send_http_get_request(
                    http_get_request_url="https://files.docking.org/catalogs/source"
                ).text
            ):
                supported_versions[
                    "v_catalog_{file_name:s}".format(
                        file_name=file_name
                    )
                ] = "https://doi.org/10.1021/acs.jcim.0c00675"

            return supported_versions

        except Exception as exception_handle:
            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

            raise

    def download(
            self,
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the database.

        :parameter version: The version of the database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="ZINC chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_building_blocks"):
                    ZINCCompoundDatabaseDownloadUtility.download_v_building_blocks(
                        version=version,
                        output_directory_path=output_directory_path
                    )

                if version.startswith("v_catalog"):
                    ZINCCompoundDatabaseDownloadUtility.download_v_catalog(
                        version=version,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="ZINC chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="ZINC chemical compound database version '{version:s}'".format(
                            version=version
                        )
                    )
                )

        except Exception as exception_handle:
            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

            raise

    def extract(
            self,
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the database.

        :parameter version: The version of the database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been started.".format(
                            data_source="ZINC chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_building_blocks"):
                    ZINCCompoundDatabaseExtractionUtility.extract_v_building_blocks(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="ZINC chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="ZINC chemical compound database version '{version:s}'".format(
                            version=version
                        )
                    )
                )

        except Exception as exception_handle:
            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

            raise

    def format(
            self,
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the database.

        :parameter version: The version of the database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="ZINC chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_building_blocks"):
                    ZINCCompoundDatabaseFormattingUtility.format_v_building_blocks(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version.startswith("v_catalog"):
                    ZINCCompoundDatabaseFormattingUtility.format_v_catalog(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="ZINC chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="ZINC chemical compound database version '{version:s}'".format(
                            version=version
                        )
                    )
                )

        except Exception as exception_handle:
            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

            raise
