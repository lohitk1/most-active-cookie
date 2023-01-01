import csv
from validations import validateCSVHeaders, validateDate
from displays import displayError

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
