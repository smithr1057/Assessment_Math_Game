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


# checks users enter an integer / float between a low and high number and allows 'xxx'
def num_check(question, type, low=None, high=None):
    # Used ChatGPT to allow the use of the letter 'x' used the prompt bellow
    # Make that function allow the letter 'x' to be used

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:
        try:
            if type == "int":
                # Ask the question
                response = input(question)

                # Check if response is 'x'
                if response.lower() == 'xxx':
                    return response

                # Convert the response to an integer
                response = int(response)
            else:
                # Ask the question
                response = input(question)

                # Check if response is 'xxx'
                if response.lower() == 'xxx':
                    return response

                # Convert the response to a float
                response = float(response)

            # Checks input is not too high or
            # too low if both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    color_text(f"Please enter a number between {low} and {high}", 'red')
                    continue

            # Checks input is not too low
            elif situation == "low only":
                if response < low:
                    color_text(f"Please enter a number that is more than {low}", 'red')
                    continue

            return response

        except ValueError:
            color_text("Please enter an integer or 'xxx'", 'red')
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


# Lets you change color of printed text easily
def color_text(text, color):
    # Code was found using chatGpt using prompt
    # "Python function that allows me to change the text color"
    # Code was changed a bit as some parts were unneeded

    # list of colors
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }

    # Prints text in specified color
    print(f"{colors[color]}{text}\033[0m")


# Main Routine


# Lists
y_n_list = ["yes", "no"]
mode_list = ["easy", "medium", "hard"]

# Errors
y_n_error = "Please enter either yes or no"
mode_error = "Please choose either easy, medium or hard"

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

    # Choose difficulty
    mode_choice = choice_checker("Easy, Medium or Hard? ", mode_list, mode_error)

    end_game = "no"
    while end_game == "no":

        # Rounds Heading
        print()
        if rounds == "":
            heading = f"Continuous Mode: Question" \
                      f" {rounds_played + 1}"
        else:
            heading = f"Question {rounds_played + 1}" \
                      f" of {rounds}"

        print(heading)

        quit_game = input(f"<enter> to continue or 'xxx' to end: ")



        # Generate random num and answer
        if mode_choice == "easy":
            max_num = 100

        elif mode_choice == "medium":
            max_num = 500

        elif mode_choice == "medium" or "easy":
            random_num = random.randint(1, max_num)
            answer = random_num + 1
            user_guess = num_check(f"What is 1 more than {random_num}: ", 0, max_num + 1)

        # if hard mode then do decimals
        else:
            max_num = 500
            random_num = round(random.uniform(1, max_num), 2)
            answer = random_num + 0.01
            user_guess = num_check(f"What is 0.01 more than {random_num}: ", float, 0, max_num)

        # Give colored feedback if right or wrong
        if user_guess == answer:
            color_text("Correct", 'green')
        # End game if exit code is typed
        elif user_guess == "xxx":
            break
        else:
            color_text("Incorrect", 'red')

        # End game if exit code is typed


    # rest of loop / game

    rounds_played += 1

    # End game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# If user hasn't played a round comment
# Don't give them the option of game history
if rounds_played < 1:
    print()
    print("Maybe play the game next time :)")
else:
    print()
    color_text("Thanks for playing the Add One Game :D", "blue")
