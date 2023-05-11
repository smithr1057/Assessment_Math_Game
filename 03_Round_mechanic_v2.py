# Main routine more efficient than v1

# Functions
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


# Main routine

rounds_played = 0

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

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
