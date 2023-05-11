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


# Asks users how many rounds they want to play
def check_rounds():

    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# checks users enter an integer between a low and high number
def int_check(question, low=None, high=None):
    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:
        try:
            # Ask the question
            response = int(input(question))

            # Checks input is not too high or
            # too low if a both upper and
            # lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between "
                          f"{low} and {high}")
                    continue

            # Checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is more"
                          f"than {low}")
                    continue

            return response

        # Checks input is an integer
        except ValueError:
            print("Please enter an integer that is more than 0")
            continue


# Adds decorations to selected text
def statement_generator(statement, decoration, lines=None):
    sides = decoration * 3

    statement = f"{sides} {statement} {sides}"
    top_bottom = decoration * len(statement)

    # use 3 lines for headings / heavy decoration
    if lines == 3:
        new_statement = f"{top_bottom}\n{statement}\n{top_bottom}"

    else:
        # default is one single line
        new_statement = statement

    return new_statement


# Main Routine


# Lists
y_n_list = ["yes", "no"]

# Errors
y_n_error = "Please enter either yes or no"

# Asks users if they have played before
# if 'no' then print instructions
played_before = choice_checker("Have you played before? ", y_n_list, y_n_error)
if played_before == "no":
    instructions()

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()
rounds_played = 0

play_again = "yes"
while play_again == "yes":

    # Rounds Heading
    print()
    if rounds == "":
        heading = f"Continuous Mode: Round" \
                  f" {rounds_played + 1}"
    else:
        heading = f"Round {rounds_played + 1}" \
                  f" of {rounds}"

    print(heading)
    quit_game = input(f"<enter> to continue or 'xxx' to end: ")

    # End game if exit code is typed
    if quit_game == "xxx":
        break

    # rest of loop / game
    print(f"You chose {quit_game}")

    rounds_played += 1

    # End game if requested # of rounds has been played
    if rounds_played == rounds:
        break

print("Thank you for playing")
