import argparse
import csv
import datetime

def displayError(error_message=""):
    if (error_message != ""):
        print(error_message)
    quit()


def validateCSVFile(file_name):
    # Checking if the given file name exists in the directory
    try:
        file_obj = open(("../logs/{}".format(file_name)))

    except:
        print("Given file name doesn't exist in the current directory")
        return False

    # Checking if the given file name corresponds to a csv file
    try:
        csvreader = csv.reader(file_obj)
        next(csvreader)
    
    except:
        print("Given file name does not correspond to a CSV file")
        return False

    file_obj.close()
    return True


def validateDate(format, date_string):
    date_format = "%Y-%m-%d"

    # Checking if given date fits the given format
    try:
        datetime.datetime.strptime(date_string, date_format)

    except:
        return False

    return True


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

    # Validating the given file name
    if (validateCSVFile(args.file_name) == False):
        # We don't need to add an error message here because the appropriate error
        # is already displayed while validating
        displayError()

    # Validating the given date
    if (validateDate("date", args.date) == False):
        displayError("Date to search is given in the wrong format. \
            Correct format: 'YYYY-MM-DD'")

    return [args.file_name, args.date]


def main():

    # Parsing the command line arguments to get the csv file name and date to search for in file
    csv_file_name, date_to_search = getCommandLineArguments()

    print(csv_file_name, date_to_search)


if __name__ == "__main__":
    main()