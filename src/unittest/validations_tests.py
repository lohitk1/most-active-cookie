import unittest
import io
import sys
from validations import validate_csv_file, validate_date, validate_csv_headers


class ValidateCSVFileTest(unittest.TestCase):
    # Changing the root logs directory for the test cases
    test_logs_directory = "./src/logs/test_logs/"

    def test_valid_file_name(self):
        file_name = "cookie_log.csv"

        captured_output = io.StringIO()
        sys.stdout = captured_output
        returned_result = validate_csv_file(file_name, self.test_logs_directory)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "")
        self.assertTrue(returned_result)


    def test_invalid_file_name_not_existing(self):
        file_name = "cookie_log_2.csv"

        captured_output = io.StringIO()
        sys.stdout = captured_output
        returned_result = validate_csv_file(file_name, self.test_logs_directory)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), \
        "Given file name doesn't exist in the current directory")
        self.assertFalse(returned_result)


    def test_invalid_file_name_not_csv(self):
        file_name = "cookie_log.txt"

        captured_output = io.StringIO()
        sys.stdout = captured_output
        returned_result = validate_csv_file(file_name, self.test_logs_directory)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), \
        "Given file name does not correspond to a CSV file")
        self.assertFalse(returned_result)


class ValidateDateTest(unittest.TestCase):
    def test_valid_date_dateformat(self):
        date_string = "2018-12-09"

        self.assertTrue(validate_date("date", date_string))


    def test_invalid_date_wrong_length_dateformat(self):
        date_string = "2018-12-9"

        self.assertFalse(validate_date("date", date_string))


    def test_invalid_date_correct_length_dateformat(self):
        date_string = "20-12-9876"

        self.assertFalse(validate_date("date", date_string))


    def test_valid_date_datetimeformat(self):
        date_string = "2018-12-09T12:23:00+00:00"

        self.assertTrue(validate_date("datetime", date_string))


    def test_invalid_date_wrong_length_datetimeformat(self):
        date_string = "2018-12-9T12:23:00+00:00"

        self.assertFalse(validate_date("datetime", date_string))


    def test_invalid_date_correct_length_datetimeformat(self):
        date_string = "20-1233-08T12:23:00+00:00"

        self.assertFalse(validate_date("datetime", date_string))


class ValidateCSVHeadersTest(unittest.TestCase):
    def test_valid_headers(self):
        headers = ["header1", "header2", "header3"]
        correct_headers = ["header1", "header2", "header3"]

        self.assertTrue(validate_csv_headers(headers, correct_headers))


    def test_invalid_headers_wrong_number(self):
        headers = ["header1", "header2"]
        correct_headers = ["header1", "header2", "header3"]

        self.assertFalse(validate_csv_headers(headers, correct_headers))


    def test_invalid_headers_correct_number(self):
        headers = ["header1", "header2", "header4"]
        correct_headers = ["header1", "header2", "header3"]

        self.assertFalse(validate_csv_headers(headers, correct_headers))


    def test_valid_headers_empty(self):
        headers = []
        correct_headers = []

        self.assertTrue(validate_csv_headers(headers, correct_headers))
    