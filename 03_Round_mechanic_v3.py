# Main routine more efficient than v1

# Functions

# checks users enter an integer / float between a low and high number and allows 'xxx'
# Also allows <enter> if required
def num_check(question, type, enter, low=None, high=None):
    # Used ChatGPT to allow the use of the letter 'x' used the prompt below
    # Make that function allow the letter 'x' to be used

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:
        # Ask the question
        response = input(question)

        # Allow user to enter 'xxx'
        if response == 'xxx':
            return response
        # if specified allow user to enter nothing
        if enter == 'yes':
            if response == "":
                return response

        try:
            if type == "int":
                # Convert the response into an integer
                response = int(response)
            else:
                # Convert the response into a float
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

        # If error the respond with appropriate error message
        except ValueError:
            if type == "int":
                if enter == 'yes':
                    color_text("Please type either <enter> or an integer that is more than 0", 'red')
                else:
                    color_text("Please enter an integer or 'xxx'", 'red')
            else:
                color_text("Please enter a number or 'xxx'", 'red')


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


# Main routine

rounds_played = 0

# Ask user for # of rounds, <enter> for infinite mode
rounds = num_check("How many questions: ", 'int', 'yes', 0)

end_game = "no"
while end_game == "no":

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
