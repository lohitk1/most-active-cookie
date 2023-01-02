import csv
from utils.validations import validate_csv_headers, validate_date
from utils.displays import display_error

def extract_cookie_frequency(
    file_name, date_to_search, logs_directory="./src/logs/"):
    """Function to extract the frequencies of each cookie found on given
    date from given CSV file and store it in a dictionary

        Parameters: 
            file_name (str): Name of valid CSV file
            date_to_search (str): Date in string for which to 
            find cookie frequencies
            
        Returns:
            dictionary: Dictionary with cookies as keys and their
            corresponding frequencies as values
    """
    # Opening the given csv file name to read contents
    csv_file_obj = open("{}{}".format(logs_directory, file_name))
    csvreader = csv.reader(csv_file_obj)

    # Validating headers
    headers = next(csvreader)
    if (validate_csv_headers(headers, ["cookie", "timestamp"]) == False):
        display_error(
            "Headers in CSV file do not fit the problem description." +\
            "Make sure you have given the correct csv file.")
    
    # Storing the cookies that appear on the date to search and their 
    # corresponding frequencies on that date in a hashmap
    cookie_freq_dictionary = dict()
    row_counter = 1
    for row in csvreader:
        if (validate_date("datetime", row[1]) == False):
            display_error(
                "Date in entry " + str(row_counter) + " of given CSV file" \
                " is in the wrong format. \nDate given: " + row[1] + \
                "\nCorrect format: 'YYYY-MM-DDTHH:MM:SS+HH:MM'"
                )

        # Modifying the frequency of cookie if the date in current row 
        # matches the date to search            
        if (row[1][:10] == date_to_search):
            cookie_freq_dictionary[row[0]] = 1 + \
                cookie_freq_dictionary.get(row[0], 0)
        
        row_counter += 1

    return cookie_freq_dictionary


def find_max_freq_from_dictionary(dictionary):
    """Function to find the list of items with maximum frequency 
    given a item,frequency dictionary
        
        Parameters:
            dictionary (dict): Dictionary with keys->items and 
            values->frequencies
            
        Returns:
            list: List of items with maximum frequency
    """
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
