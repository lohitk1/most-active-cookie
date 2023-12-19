#!/usr/bin/env python3
"""
This module contains functionality to find most active cookie in a log file.

It contains functions for cli-parsing, csv file data extraction, and max
frequency computation.
"""
import argparse
import csv
import os
import logging
import sys
from datetime import datetime


class InvalidCSVHeadersError(Exception):
    """Exception raised when CSV headers do not match expected headers."""


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )


def parse_date(str_date: str) -> datetime:
    """
    Convert a string to a datetime object.

    This function takes a date (str) in the format 'YYYY-MM-DD' and converts it
    into a datetime object. If the string is not in correct format, it raises
    an ArgumentTypeError.

    Parameters:
    str_date (str): The date string to parse. Expected format is 'YYYY-MM-DD'.

    Returns:
    datetime: A datetime object representing the given date.
    """
    try:
        return datetime.strptime(str_date, '%Y-%m-%d')
    except ValueError as e:
        msg = f"Not a valid date: '{str_date}'. Expected format: YYYY-MM-DD."
        raise argparse.ArgumentTypeError(msg) from e


def parse_cli_args() -> argparse.Namespace:
    """
    Parse command-line arguments for the 'most-active-cookie' program.

    This function sets up an argument parser for a command-line app that
    requires a log file and a date. It expects the log file in CSV format
    and the date in 'YYYY-MM-DD' format. The function defines two arguments:
    one positional argument for the log file and one required option for
    the date.

    Returns:
    argparse.Namespace: An object containing the parsed arguments. This object
                        will have 'log_file' and 'date' attributes accessible,
                        corresponding to the input values provided by the user.
    """
    parser = argparse.ArgumentParser(
        prog="most-active-cookie",
        description="Find most active cookie in a log file given a date"
        )

    # Positional argument for the log file
    parser.add_argument("log_file", type=str,
                        help="Cookie log file in CSV format")

    # Required option for the date
    parser.add_argument(
        "-d", "--date",
        required=True,
        type=parse_date,
        help="Date (YYYY-MM-DD) to find the most active cookie"
        )

    return parser.parse_args()


def validate_csv_file(
    file_name: str,
    logs_directory: str = "./logs/"
) -> None:
    """
    Validate a CSV file in the specified directory.

    This function checks if the file exists in the specified path. If
    the file does not exist, the program will print an error message
    and exit..

    Parameters:
    file_name (str): The name of the CSV file to validate and open.
    logs_directory (str, optional): The directory where CSV file is located.
                                    Defaults to "./logs/".
    """
    path_to_csv = os.path.join(logs_directory, file_name)

    # Check if the file exists
    if not os.path.isfile(path_to_csv):
        msg = (f"File '{file_name}' not found in '{logs_directory}'.")
        raise FileNotFoundError(msg)


def validate_csv_headers(headers: list, correct_headers: list) -> None:
    """
    Validate headers from a CSV file.

    This function compares two lists of headers checking if each header in
    the 'headers' list matches the corresponding header in the
    'correct_headers' list. If there is a mismatch in either the number of
    headers or any specific header, the program will terminate.

    Parameters:
    headers (list): The list of headers to validate.
    correct_headers (list): The list of correct headers to compare against.
    """
    # Checking whether number of given headers is correct
    if len(headers) != len(correct_headers):
        msg = ("CSV file has wrong headers")
        raise InvalidCSVHeadersError(msg)

    # Checking whether each header is correct
    for header, correct_header in zip(headers, correct_headers):
        if header != correct_header:
            msg = ("CSV file has wrong headers")
            raise InvalidCSVHeadersError(msg)


def get_cookie_freq(file_name: str, date_to_search: datetime, logs_directory="./logs/") -> dict:
    """
    Read a CSV file to compute the frequency of cookies on a given date.

    This function validates a given csv file and iterates through the file,
    counting the frequency of each cookie that appears on the specified date
    using a dictionary.

    Parameters:
    file_name (str): The name of the CSV file to be read.
    str_date_to_search (str): The date (in 'YYYY-MM-DD' format) for which
                              to count cookie frequencies.
    logs_directory (str, optional): The directory where the CSV file is
                                    located. Defaults to "./logs/".

    Returns:
    dict: A dictionary where each key is a cookie and its value is the
          frequency on the specified date.
    """
    # Opening the given csv file name to read contents
    validate_csv_file(file_name, logs_directory)

    path_to_csv = os.path.join(logs_directory, file_name)

    # Attempt to open the file
    try:
        with open(path_to_csv, "r", encoding='utf-8') as csv_file_obj:
            csvreader = csv.reader(csv_file_obj)

            # Validating headers
            headers = next(csvreader)
            validate_csv_headers(headers, ["cookie", "timestamp"])

            # Storing the cookies that appear on the date to search and their
            # corresponding frequencies on that date in a hashmap
            cookie_freq_dict = {}
            for row in csvreader:
                date_in_csv = datetime.strptime(row[1][:10], '%Y-%m-%d')
                # Modifying the frequency of cookie if the date in current
                # row matches the date to search
                if date_in_csv == date_to_search:
                    cookie_freq_dict[row[0]] = \
                        1 + cookie_freq_dict.get(row[0], 0)

                # Since cookies are sorting by timestamp,
                # can stop after given date
                elif date_in_csv < date_to_search:
                    break

    except IOError as e:
        msg = f"IO Error occurred: {e}"
        raise IOError(msg) from e
    except csv.Error as e:
        msg = f"CSV Error: {e}"
        raise csv.Error(msg) from e

    return cookie_freq_dict


def find_max_freq_from_dict(cookies_dict: dict) -> list:
    """
    Return the items with the highest frequency in the given dictionary.

    This function iterates through a dictionary and finds the maximum value
    and returns a list of all keys that have this value.

    Parameters:
    cookies_dict (dict): A dictionary with cookies as keys and frequencies as
                         values.

    Returns:
    list: A list of items that have the highest frequency in the dictionary.
          If no items are found, returns an empty list.
    """
    max_freq = 0
    max_freq_item_list = []

    for item, freq in cookies_dict.items():
        # Restart list if higher frequency is found
        if freq > max_freq:
            max_freq = freq
            max_freq_item_list = [item]

        # Append to list if equal frequency is found
        elif freq == max_freq:
            max_freq_item_list.append(item)

    return max_freq_item_list


def print_cookies_found(list_of_cookies: list) -> None:
    """
    Print each cookie from a given list of cookies.

    This function iterates through a list of cookies and prints each one.
    If the list is empty, it prints a message indicating that no cookies
    were found.

    Parameters:
    list_of_cookies (list): A list of cookies to be printed.
    """
    if len(list_of_cookies) == 0:
        logging.info("No cookies were found")

    for item in list_of_cookies:
        print(item)


def main():
    """Print the most active cookie in a given cookie log file."""
    try:
        # Extracting cli arguments
        cli_args = parse_cli_args()

        log_file = cli_args.log_file
        date = cli_args.date

        # Calculating the cookie with the maximum frequency
        cookie_freq_dict = get_cookie_freq(log_file, date)

        max_freq_cookie_list = find_max_freq_from_dict(cookie_freq_dict)

        # Displaying the cookie(s)
        print_cookies_found(max_freq_cookie_list)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
