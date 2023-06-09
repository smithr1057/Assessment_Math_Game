import random
# V3 - Editing the modes to add hard mode with decimals


# Functions
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
mode_list = ["easy", "medium", "hard"]
y_n_list = ["yes", "no", "y", "n"]
# error
mode_error = "Please choose either easy, medium or hard"
y_n_error = "Please enter either yes or no"

rounds_won = 0
rounds_lost = 0
rounds_played = 0
game_summary = []

# loop
loop = "yes"
while loop == "yes":
    # Choose difficulty
    mode_choice = choice_checker("Easy, Medium or Hard? ", mode_list, mode_error)

    game = "yes"
    while game == "yes":

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
            result = "Correct ✔"'\033[92m'
            color_text("Correct ✔", 'green')
            rounds_won += 1
            outcome = f"Question {rounds_played + 1}: {result}"

        # End game if exit code is typed
        elif user_guess == "xxx":
            break

        # Print result in color and set outcome
        else:
            result = "Incorrect ❌"'\033[91m'
            color_text("Incorrect ❌", 'red')
            rounds_lost += 1
            outcome = f"Question {rounds_played + 1}: {result}, the correct answer was {color_text(answer, 'green')}"

        rounds_played += 1
        game_summary.append(outcome)


    if rounds_played > 1:
        # Ask user if they want to see their game history
        # if 'yes' show game history
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
                print(game)

            print()

            # displays game stats with % values to the nearest whole number
            statement_generator("Game Statistics", "-", 3)
            color_text(f"Win: {rounds_won}, {percent_win:.0f}%", 'green')
            color_text(f"Loss: {rounds_lost}, {percent_lose:.0f}%", 'red')

        print()
        print("Thanks for playing the Plus one game :D")

    # If user hasn't played a round comment
    # Don't give them the option of game history
    elif rounds_played < 1:
        print("Maybe play the game next time :)")