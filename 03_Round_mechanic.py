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


# Main routine


rounds_played = 0


# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = f"Continuous Mode: Round {rounds_played + 1}"
        print(heading)
        choose = input(f"<enter> to continue or 'xxx' to end: ")
        if choose == "xxx":
            break
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        print(heading)
        choose = input(f"<enter> to continue or 'xxx' to end: ")
        if rounds_played == rounds - 1:
            end_game = "yes"

    # rest of loop / game
    print(f"You chose {choose}")

    rounds_played += 1

print("Thank you for playing")
