import unittest
import os
import sys
import io
from datetime import datetime

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from most_active_cookie import get_cookie_freq, \
    find_max_freq_from_dict, print_cookies_found, \
    validate_csv_file, validate_csv_headers, main, \
    InvalidCSVHeadersError

class ValidateCSVFileTest(unittest.TestCase):
    # Changing the root logs directory for the test cases
    test_logs_directory = "./logs/"

    def test_valid_file_name(self):
        file_name = "cookie_log.csv"

        captured_output = io.StringIO()
        sys.stdout = captured_output
        validate_csv_file(file_name, self.test_logs_directory)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "")

    def test_invalid_file_name_not_existing(self):
        file_name = "cookie_log_2.csv"

        captured_output = io.StringIO()
        sys.stdout = captured_output
        sys.stdout = sys.__stdout__

        with self.assertRaises(FileNotFoundError):
            validate_csv_file(file_name, self.test_logs_directory)

        
class ValidateCSVHeadersTest(unittest.TestCase):
    def test_valid_headers(self):
        headers = ["header1", "header2", "header3"]
        correct_headers = ["header1", "header2", "header3"]

        captured_output = io.StringIO()
        sys.stdout = captured_output
        validate_csv_headers(headers, correct_headers)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), "")


    def test_invalid_headers_wrong_number(self):
        headers = ["header1", "header2"]
        correct_headers = ["header1", "header2", "header3"]

        with self.assertRaises(InvalidCSVHeadersError):
            validate_csv_headers(headers, correct_headers)


    def test_invalid_headers_correct_number(self):
        headers = ["header1", "header2", "header4"]
        correct_headers = ["header1", "header2", "header3"]

        with self.assertRaises(InvalidCSVHeadersError):
            validate_csv_headers(headers, correct_headers)


    def test_valid_headers_empty(self):
        headers = []
        correct_headers = []

        captured_output = io.StringIO()
        sys.stdout = captured_output
        validate_csv_headers(headers, correct_headers)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), "")



class GetCookieFreqTest(unittest.TestCase):
    # Changing the root logs directory for the test cases
    test_logs_directory = "./logs/"

    def test_log_file_with_equal_freq_on_date_to_search(self):
        file_name = "cookie_log.csv"
        date_to_search = datetime.strptime("2018-12-08", '%Y-%m-%d')

        self.assertEqual(get_cookie_freq(
            file_name, date_to_search, self.test_logs_directory),
            {"SAZuXPGUrfbcn5UA": 1, "4sMM2LxV07bPJzwf": 1,
             "fbcn5UAVanZf6UtG": 1})

    def test_log_file_has_one_date(self):
        file_name = "cookie_log_one_date.csv"
        date_to_search = datetime.strptime("2018-12-08", '%Y-%m-%d')

        self.assertEqual(get_cookie_freq(
            file_name, date_to_search, self.test_logs_directory),
            {"SAZuXPGUrfbcn5UA": 1, "4sMM2LxV07bPJzwf": 1,
             "fbcn5UAVanZf6UtG": 1, "AtY0laUfhglK3lC7": 1})

    def test_log_file_does_not_have_date_to_search(self):
        file_name = "cookie_log.csv"
        date_to_search = datetime.strptime("2018-12-06", '%Y-%m-%d')

        self.assertEqual(get_cookie_freq(
            file_name, date_to_search, self.test_logs_directory),
            {})

    def test_log_file_has_no_records(self):
        file_name = "cookie_log_empty.csv"
        date_to_search = datetime.strptime("2018-12-08", '%Y-%m-%d')

        self.assertEqual(get_cookie_freq(
            file_name, date_to_search, self.test_logs_directory),
             {})


class FindMaxFreqFromDictTest(unittest.TestCase):
    def test_one_cookie_has_max_freq(self):
        dictionary = {"AtY0laUfhglK3lC7": 2, "SAZuXPGUrfbcn5UA": 1,
                      "5UAVanZf6UtGyKVS": 1}

        self.assertEqual(
            find_max_freq_from_dict(dictionary), ["AtY0laUfhglK3lC7"])

    def test_max_freq_tied(self):
        dictionary = {"AtY0laUfhglK3lC7": 2, "SAZuXPGUrfbcn5UA": 3,
                      "5UAVanZf6UtGyKVS": 3}

        self.assertEqual(
            find_max_freq_from_dict(dictionary),
            ["SAZuXPGUrfbcn5UA", "5UAVanZf6UtGyKVS"])

    def test_empty_dictionary(self):
        dictionary = {}

        self.assertEqual(find_max_freq_from_dict(dictionary), [])


class PrintCookiesFoundTest(unittest.TestCase):
    def test_multiple_items_list(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_cookies_found(["value1", "value2", "value3"])
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(),
         "value1\nvalue2\nvalue3")
        
    def test_one_item_list(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_cookies_found(["value1"])
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "value1")

    def test_no_item_list(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_cookies_found([])
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), "")


class EndToEndTest(unittest.TestCase):
    def test_main_functionality(self):

        original_argv = sys.argv

        # Set sys.argv to the desired test arguments
        sys.argv = ['most_active_cookie.py', 'cookie_log.csv', '-d', '2018-12-08']

        try:
            # Call the main function
            captured_output = io.StringIO()
            sys.stdout = captured_output
            main()
            sys.stdout = sys.__stdout__

            # Your assertions here
            self.assertEqual(captured_output.getvalue(),"SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n")

        finally:
            # Restore the original sys.argv
            sys.argv = original_argv

