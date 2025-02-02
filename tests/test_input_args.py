import unittest
from unittest.mock import patch
from scripts.download_extract_and_format_data import get_script_arguments

class TestInputArguments(unittest.TestCase):
    """Unit tests for `get_script_arguments()` function in the argument parser.
        Tests are mocked to simulate the command line arguments."""

    def test_valid_data_source_category_compound(self):
        """Test a valid argument `-dsc compound` is parsed correctly."""
        with patch('sys.argv', ['script_name', '-dsc', 'compound']):
            args = get_script_arguments()
            self.assertEqual(args.data_source_category, 'compound')

    def test_valid_data_source_category_reaction(self):
        """Test a valid argument `-dsc reaction` is parsed correctly."""
        with patch('sys.argv', ['script_name', '-dsc', 'reaction']):
            args = get_script_arguments()
            self.assertEqual(args.data_source_category, 'reaction')

    def test_invalid_data_source_category(self):
        """Test if an invalid argument `-dsc invalid_category` will raise an exception."""
        with patch('sys.argv', ['script_name', '-dsc', 'invalid_category']):
            with self.assertRaises(SystemExit) as cm:
                get_script_arguments()
            self.assertEqual(cm.exception.code, 2) 

    def test_valid_data_source_name(self):
        """Test a valid argument `-dsn chembl` is parsed correctly."""
        with patch('sys.argv', ['script_name', '-dsn', 'chembl']):
            args = get_script_arguments()
            self.assertEqual(args.data_source_name, 'chembl')

    def test_invalid_data_source_name(self):
        """Test if an invalid argument `-dsn unknown_source` will raise an exception."""
        with patch('sys.argv', ['script_name', '-dsn', 'unknown_source']):
            with self.assertRaises(SystemExit) as cm:
                get_script_arguments()
            self.assertEqual(cm.exception.code, 2)

    def test_valid_get_data_source_name(self):
        """Test a valid argument `-gdsn` is parsed correctly."""
        with patch('sys.argv', ['script_name', '-gdsn']):
            args = get_script_arguments()
            self.assertTrue(args.get_data_source_name)

    def test_valid_get_data_source_version(self):
        """Test a valid argument `-gdsv` is parsed correctly."""
        with patch('sys.argv', ['script_name', '-gdsv']):
            args = get_script_arguments()
            self.assertTrue(args.get_data_source_version)

    def test_valid_output_directory_path(self):
        """Test a valid argument `-odp /some/path` is parsed correctly."""
        with patch('sys.argv', ['script_name', '-odp', '/some/path']):
            args = get_script_arguments()
            self.assertEqual(args.output_directory_path, '/some/path')

    def test_missing_required_arguments(self):
        """Test if missing required arguments raises an exception."""
        with patch('sys.argv', ['script_name']):
            with self.assertRaises(SystemExit) as cm:
                get_script_arguments()
            self.assertEqual(cm.exception.code, 2)

    def test_valid_number_of_processes(self):
        """Test if argument `-odp 4` sets number of processes correctly."""
        with patch('sys.argv', ['script_name', '-nop', '4']):
            args = get_script_arguments()
            self.assertEqual(args.number_of_processes, '4')

    def test_empty_input(self):
        """ Test if no arguments are passed, it raises an exception."""
        with patch('sys.argv', ['script_name']):
            with self.assertRaises(SystemExit) as cm:
                get_script_arguments()
            self.assertEqual(cm.exception.code, 2)

    def test_non_str_type_input(self):
        """Test if non-string type input raises an exception."""
        with patch('sys.argv', ['script_name', '-dsc', 666]):
            with self.assertRaises(SystemExit) as cm:
                get_script_arguments()
            self.assertEqual(cm.exception.code, 2)

    def test_undefined_argument_input(self):
        """Test if an undefined argument raises an exception."""
        with patch('sys.argv', ['script_name', '-unknown', 'value']):
            with self.assertRaises(SystemExit) as cm:
                get_script_arguments()
            self.assertEqual(cm.exception.code, 2)

    def test_extra_spaces_in_arguments(self):
        """Test if extra spaces in arguments could be handled. like `-dsc    compound   ` """
        with patch('sys.argv', ['script_name', '-dsc', '   compound   ']):
            args = get_script_arguments()
            self.assertEqual(args.data_source_category.strip(), 'compound')

if __name__ == '__main__':
    unittest.main()