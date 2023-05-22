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
rounds_played = 5
rounds_lost = 3
rounds_won = 2

y_n_error = "Please enter either yes or no"
yes_no_list = ["yes", "no", "y", "n"]
game_summary = []

if rounds_played > 1:
    # Ask user if they want to see their game history
    # if 'yes' show game history
    show_stats = choice_checker("Would you like to see your"
                                " end game history? "
                                , yes_no_list, y_n_error)

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