import datetime

def validate_csv_file(file_name, logs_directory = "./src/logs/"):
    """Function to validate whether given file name is a valid CSV file
    
        Parameters:
            file_name (str): Name of file to validate
            logs_directory (str): Stores the directory of the log files
            
        Returns:
            boolean: Whether file name corresponds to valid CSV file
    """

    # Checking if the given file name exists in the directory
    try:
        file_obj = open(("{}{}".format(logs_directory, file_name)))

    except:
        print("Given file name doesn't exist in the current directory")
        return False

    # Checking if the given file name corresponds to a csv file
    if(file_name[-4:] != ".csv"):
        print("Given file name does not correspond to a CSV file")
        return False

    file_obj.close()
    return True


def validate_date(format, date_string):
    """Function to validate if given date string matches the given date format
    
        Parameters:
            format (str): The expected date format. Ex: date, datetime
            date_string (str): The date to validate in string format
        
        Returns:
            boolean: Whether given date matches the given format
    """
    correct_length_of_date = 0
    if (format == "datetime"):
        correct_length_of_date = 25
        date_format = "%Y-%m-%dT%H:%M:%S%z"


    else:
        correct_length_of_date = 10
        date_format = "%Y-%m-%d"

    # Checking if length of given date is correct
    if (correct_length_of_date != len(date_string)):
        return False
    
    # Checking if given date fits the given format
    try:
        datetime.datetime.strptime(date_string, date_format)

    except:
        return False

    return True


def validate_csv_headers(headers, correct_headers):
    """Function to validate if given CSV header values match the 
    correct/expected header values
        
        Parameters:
            headers (list(any)): List of given header values
            correct_headers (list(any): List of correct/expected header values
            
        Returns:
            boolean: Whether given header values match 
            correct/expected header values
    """
    # Checking whether number of given headers is correct
    if (len(headers) != len(correct_headers)):
        return False

    # Checking whether each header is correct
    for header_index in range(len(headers)):
        if (headers[header_index] != correct_headers[header_index]):
            return False
    
    return True