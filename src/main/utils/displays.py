import sys

def display_error(error_message=""):
    """Function to display error messages to console
        
        Parameters:
            error_message (str): Error message to be printed
            
        Returns:
            None
        """
    sys.exit(error_message)


def print_items_found(list_of_items, item_name_plural="items"):
    """Function to properly display the items from list of items 
        
        Parameters:
            list_of_items (list): List of given items to be displayed
            item_name_plural (str): Plural form of the given items

        Returns: 
            None 
        """
    if (len(list_of_items) == 0):
        print("No", item_name_plural, "were found")

    for item in list_of_items:
        print(item)