import argparse
import datetime
from utils.validations import validate_csv_file, validate_date
from utils.calculations import extract_cookie_frequency,\
     find_max_freq_from_dictionary
from utils.displays import display_error, print_items_found

def get_command_line_arguments():
    parser = argparse.ArgumentParser(
        prog="Most-Active-Cookie",
        description="Finds the most active cookie in a" \
            "cookie log file given a specific date")

    # Adding file_name as a positional argument
    parser.add_argument(
        "file_name", metavar="file_name", 
        help="CSV file name containing the cookie log")

    # Adding date as a required optional argument
    parser.add_argument(
        "-d", "--date", metavar="", required=True,
        help="Date (YYYY-MM-DD) for which to search for" +\
             "maximum occuring cookie")

    args = parser.parse_args()

    # Validating the given file name
    if (validate_csv_file(args.file_name) == False):
        # We don't need to add an error message here because the 
        # appropriate error is already displayed while validating
        display_error()

    # Validating the given date
    if (validate_date("date", args.date) == False):
        display_error(
            "Date to search is given in the wrong format." \
            "\nDate given: " + args.date +\
            "\nCorrect format: 'YYYY-MM-DD'")

    return [args.file_name, args.date]


def main():

    # Parsing the command line arguments to get the csv file name and date to
    # search for in file
    csv_file_name, date_to_search = get_command_line_arguments()

    # Extracting the cookies and their respective frequencies that occur on the
    # given date to search, and storing them in a hashmap
    cookie_freq_dictionary = extract_cookie_frequency(
        csv_file_name, date_to_search)

    # Finding the list of cookies with the maximum occuring frequency in the
    # hashmap
    max_freq_cookie_list = find_max_freq_from_dictionary(
        cookie_freq_dictionary)
    
    # Printing the calculated cookies with maximum occuring frequencies
    print_items_found(max_freq_cookie_list, "cookies")


if __name__ == "__main__":
    main()