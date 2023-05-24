import random
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
        color_text(error, 'red')
        print()


# Displays instructions
def instructions():
    print()
    color_text("**** How to Play ****", 'blue')
    print()
    print("Choose how many questions you want to "
          "answer (press <enter> for continuous mode)")
    print()
    print("Choose mode")
    print("Easy mode - Add 1 to a number up to 100")
    print("Medium mode - Add 1 to a number up to 500")
    print("Hard mode - Add 0.1 to a number up to 1000")
    print()
    print("You can enter 'xxx' at any time during the game to quit")
    print()
    print("After you finish your game you can choose to see your "
          "game history and statistics")
    print()
    print("At the end of the game you may choose to begin a new game")
    print()
    print("Good Luck :D")
    print()
    return ""


# Asks users how many rounds they want to play
def check_rounds():

    while True:
        response = input("How many questions: ")

        round_error = "Please type either <enter> or an integer that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    color_text(round_error, 'red')
                    continue

            except ValueError:
                color_text(round_error, 'red')
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

# Prints title with decorations and color
title = statement_generator("Welcome to The Plus One Game", "*", 3)
colour_title = color_text(title, 'cyan')

# Asks users if they have played before
# if 'no' then print instructions
played_before = choice_checker("Have you played before? ", y_n_list, y_n_error)
if played_before == "no":
    instructions()

play_again = "yes"
while play_again == "yes":

    # Set rounds played to 0 and empty game summary
    rounds_played = 0
    rounds_lost = 0
    rounds_won = 0
    game_summary = []

    # Ask user for # of rounds, <enter> for infinite mode
    rounds = check_rounds()

    # Choose difficulty
    mode_choice = choice_checker("Easy, Medium or Hard? ", mode_list, mode_error)

    end_game = "no"
    while end_game == "no":

        # Rounds Heading
        print()
        if rounds == "":
            heading = f"*** Continuous Mode: Question" \
                      f" {rounds_played + 1} ***"
        else:
            heading = f"*** Question {rounds_played + 1}" \
                      f" of {rounds} ***"

        color_text(heading, 'yellow')

        # Generate random num
        if mode_choice == "easy" or mode_choice == "medium":
            if mode_choice == "easy":
                max_num = 100
            if mode_choice == "medium":
                max_num = 500
            random_num = random.randint(1, max_num)
            answer = random_num + 1
            user_guess = num_check(f"What is 1 more than {random_num}: ", int, 0, max_num + 1)

        else:
            max_num = 1000
            random_num = round(random.uniform(1, max_num), 1)
            answer = round(random_num + 0.1, 1)
            print(answer)
            user_guess = num_check(f"What is 0.1 more than {random_num}: ", float, 0, max_num)

        # Print result in color and set outcome
        if user_guess == answer:
            result = "Correct ✔"
            # Set color to green
            color_result = "\033[92m" + result + "\033[0m"
            color_text("Correct ✔", 'green')
            rounds_won += 1
            outcome = f"Question {rounds_played + 1}: {color_result}"

        # End game if exit code is typed
        elif user_guess == "xxx":
            break

        # Print result in color and set outcome
        else:
            result = "Incorrect ❌"
            # Set color to red
            color_result = "\033[91m" + result + "\033[92m"
            color_text("Incorrect ❌", 'red')
            rounds_lost += 1
            outcome = f"Question {rounds_played + 1}: {color_result}, the correct answer was {answer}"


        rounds_played += 1
        # add results to game summary
        game_summary.append(outcome)


        # End game if requested # of rounds has been played
        if rounds_played == rounds:
            break

    if rounds_played >= 1:
        # Ask user if they want to see their game history
        # if 'yes' show game history
        print()
        show_stats = choice_checker("Would you like to see your"
                                    " end game history? "
                                    , y_n_list, y_n_error)

        # Calculate stats and print them out
        if show_stats == "yes":

            # Calculate game stat
            percent_win = rounds_won / rounds_played * 100
            percent_lose = rounds_lost / rounds_played * 100

            # Displays game history
            print()
            game_history = statement_generator("Game History", "-", 3)
            color_game_history = color_text(game_history, 'cyan')

            for game in game_summary:
                color_text(game, 'yellow')

            print()

            # displays game stats with % values to the nearest whole number
            statement_generator("Game Statistics", "-", 3)
            color_text(f"Win: {rounds_won}, {percent_win:.0f}%", 'green')
            color_text(f"Loss: {rounds_lost}, {percent_lose:.0f}%", 'red')

    # Ask user if they want to play again
    print()
    play_again = choice_checker("Would you like to play again? "
                                , y_n_list, y_n_error)
# If user hasn't played a round comment
# Don't give them the option of game history
if rounds_played < 1:
    print()
    print("Maybe play the game next time 🤦‍♂️")
else:
    print()
    color_text("Thanks for playing The Plus One Game 😃", "blue")
