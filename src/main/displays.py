def displayError(error_message=""):
    if (error_message != ""):
        print(error_message)
    quit()


def printItemsFound(list_of_items, item_name_plural="items"):
    if (len(list_of_items) == 0):
        print("No", item_name_plural, "were found")

    for item in list_of_items:
        print(item)