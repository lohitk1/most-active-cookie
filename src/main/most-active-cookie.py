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
    if (format == "datetime"):
        date_format = "%Y-%m-%dT%H:%M:%S%z"

    else:
        date_format = "%Y-%m-%d"

    # Checking if given date fits the given format
    try:
        datetime.datetime.strptime(date_string, date_format)

    except:
        return False

    return True
    

def validateCSVHeaders(headers, correct_headers):
    # Checking whether number of given headers is correct
    if (len(headers) != len(correct_headers)):
        return False

    # Checking whether each header is correct
    for header_index in range(len(headers)):
        if (headers[header_index] != correct_headers[header_index]):
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


def extractCookieFrequency(file_name, date_to_search):
    # Opening the given csv file name to read contents
    csv_file_obj = open("../logs/{}".format(file_name))
    csvreader = csv.reader(csv_file_obj)

    # Validating headers
    headers = next(csvreader)
    if (validateCSVHeaders(headers, ["cookie", "timestamp"]) == False):
        displayError(
            "Headers in CSV file do not fit the problem description. \
            Make sure you have given the correct csv file."
        )
    
    # Storing the cookies that appear on the date to search and their 
    # corresponding frequencies on that date in a hashmap
    cookie_freq_dictionary = dict()
    row_counter = 1
    for row in csvreader:
        if (validateDate("datetime", row[1]) == False):
            displayError(
                "Date in row " + row_counter + " of given CSV file \
                is in the wrong format. \nDate in row " + row_counter + \
                " of given CSV file of wrong format."
                    )

        # Modifying the frequency of cookie if the date in current row 
        # matches the date to search            
        if (row[1][:10] == date_to_search):
            cookie_freq_dictionary[row[0]] = 1 + cookie_freq_dictionary.get(row[0], 0)
        
        row_counter += 1

    return cookie_freq_dictionary


def findMaxFreqFromDictionary(dictionary):
    max_freq = 0
    max_freq_item_list = []

    for item, freq in dictionary.items():
        # Restart list if higher frequency is found
        if(freq > max_freq):
            max_freq = freq
            max_freq_item_list = [item]

        # Append to list if equal frequency is found
        elif (freq == max_freq):
            max_freq_item_list.append(item)

    return max_freq_item_list


def main():

    # Parsing the command line arguments to get the csv file name and date to search for in file
    csv_file_name, date_to_search = getCommandLineArguments()

    # Extracting the cookies and their respective frequencies that occur
    # on the given date to search, and storing them in a hashmap
    cookie_freq_dictionary = extractCookieFrequency(csv_file_name, date_to_search)

    # Finding the list of cookies with the maximum occuring frequency in the hashmap
    max_freq_cookie_list = findMaxFreqFromDictionary(cookie_freq_dictionary)

    print(max_freq_cookie_list)


if __name__ == "__main__":
    main()