# Functions


# checks user answers with valid answer
def choice_checker(question, valid_list, error):
    while True:
        # Ask user for choice (and put it in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


# Displays instructions
def instructions():
    print()
    print("Instructions")
    print()
    return ""


# Main routine

# List and other
y_n_list = ["yes", "no"]
y_n_error = "Please enter either yes or no"

loop = "yes"
while loop == "yes":
    played_before = choice_checker("Have you played before? ", y_n_list, y_n_error)
    if played_before == "no":
        instructions()

    print("Program Continues")
