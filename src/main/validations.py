import csv
import datetime

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