import unittest
from utils.calculations import extract_cookie_frequency, find_max_freq_from_dictionary

class ExtractCookieFrequencyTest(unittest.TestCase):
    # Changing the root logs directory for the test cases
    test_logs_directory = "./src/logs/test_logs/"

    def test_log_file_with_equal_freq_on_date_to_search(self):
        file_name = "cookie_log.csv"
        date_to_search = "2018-12-08"

        self.assertEqual(extract_cookie_frequency(file_name, date_to_search, self.test_logs_directory), \
            {"SAZuXPGUrfbcn5UA": 1, "4sMM2LxV07bPJzwf": 1, "fbcn5UAVanZf6UtG": 1})
        

    def test_log_file_has_one_date(self):
        file_name = "cookie_log_one_date.csv"
        date_to_search = "2018-12-08"

        self.assertEqual(extract_cookie_frequency(file_name, date_to_search, self.test_logs_directory), \
            {"SAZuXPGUrfbcn5UA": 1, "4sMM2LxV07bPJzwf": 1, "fbcn5UAVanZf6UtG": 1, "AtY0laUfhglK3lC7": 1})


    def test_log_file_does_not_have_date_to_search(self):
        file_name = "cookie_log.csv"
        date_to_search = "2018-12-06"

        self.assertEqual(extract_cookie_frequency(file_name, date_to_search, self.test_logs_directory), \
            {})
        

    def test_log_file_has_no_records(self):
        file_name = "cookie_log_empty.csv"
        date_to_search = "2018-12-08"

        self.assertEqual(extract_cookie_frequency(file_name, date_to_search, self.test_logs_directory), \
             {})


class FindMaxFreqFromDictionaryTest(unittest.TestCase):
    def test_one_cookie_has_max_freq(self):
        dictionary = {"AtY0laUfhglK3lC7": 2, "SAZuXPGUrfbcn5UA": 1, "5UAVanZf6UtGyKVS": 1}

        self.assertEqual(find_max_freq_from_dictionary(dictionary), ["AtY0laUfhglK3lC7"])


    def test_max_freq_tied(self):
        dictionary = {"AtY0laUfhglK3lC7": 2, "SAZuXPGUrfbcn5UA": 3, "5UAVanZf6UtGyKVS": 3}

        self.assertEqual(find_max_freq_from_dictionary(dictionary), ["SAZuXPGUrfbcn5UA", "5UAVanZf6UtGyKVS"])

    
    def test_empty_dictionary(self):
        dictionary = dict()

        self.assertEqual(find_max_freq_from_dictionary(dictionary), [])        
