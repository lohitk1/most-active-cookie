def displayError(error_message=""):
    """Function to display error messages to console
        
        Parameters:
            error_message (str): Error message to be printed
            
        Returns:
            None
        """
    if (error_message != ""):
        print(error_message)
    quit()


def printItemsFound(list_of_items, item_name_plural="items"):
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