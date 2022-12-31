import argparse

def getCommandLineArguments():
    parser = argparse.ArgumentParser(
        prog="Most-Active-Cookie",
        description="Finds the most active cookie in a \
            cookie log file given a specific date"
    )

    # Adding file_name as a positional argument
    parser.add_argument(
        "file_name", metavar="file_name", 
        help="CSV file name containing the cookie log"
        )

    # Adding date as a required optional argument
    parser.add_argument(
        "-d", "--date", metavar="", required=True,
        help="Date (YYYY-MM-DD) for which to search for maximum occuring cookie"
        )

    args = parser.parse_args()

    return [args.file_name, args.date]


def main():

    # Parsing the command line arguments to get the csv file name and date to search for in file
    csv_file_name, date_to_search = getCommandLineArguments()

    print(csv_file_name, date_to_search)


if __name__ == "__main__":
    main()