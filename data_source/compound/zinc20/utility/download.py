""" The ``data_source.compound.zinc20.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import BaseDataSourceDownloadUtility


class ZINC20CompoundDatabaseDownloadUtility:
    """ The `ZINC20 <https://zinc20.docking.org>`_ chemical compound database download utility class. """

    @staticmethod
    def download_v_building_blocks(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_building_blocks_*` version of the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        BaseDataSourceDownloadUtility.download_file(
            file_url="https://files.docking.org/bb/current/{file_name:s}.smi.gz".format(
                file_name=version.split(
                    sep="_",
                    maxsplit=3
                )[-1]
            ),
            file_name="{file_name:s}.smi.gz".format(
                file_name=version.split(
                    sep="_",
                    maxsplit=3
                )[-1]
            ),
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_catalog(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_catalog_*` version of the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        BaseDataSourceDownloadUtility.download_file(
            file_url="https://files.docking.org/catalogs/source/{file_name:s}.src.txt".format(
                file_name=version.split(
                    sep="_",
                    maxsplit=2
                )[-1]
            ),
            file_name="{file_name:s}.src.txt".format(
                file_name=version.split(
                    sep="_",
                    maxsplit=2
                )[-1]
            ),
            output_directory_path=output_directory_path
        )
