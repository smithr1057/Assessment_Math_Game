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


# Asks users how many questions they want to play
def check_questions():

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
question_type_list = ["addition", "subtraction", "both"]

# Errors
y_n_error = "Please enter either yes or no"
mode_error = "Please choose either easy, medium or hard"
question_type_error = "Please choose either addition, subtraction or both"

play_again = "yes"
while play_again == "yes":

    # Set questions answered, wrong, right to 0 and empty quiz summary
    questions_answered = 0
    questions_wrong = 0
    questions_right = 0
    quiz_summary = []

    # Ask user for # of questions, <enter> for infinite mode
    questions = check_questions()

    # Choose difficulty and question type
    mode_choice = choice_checker("Easy, Medium or Hard? ", mode_list, mode_error)
    question_type = choice_checker("Would you like addition, subtraction or both? ", question_type_list, question_type_error)

    end_quiz = "no"
    while end_quiz == "no":

        # Questions Heading
        print()
        if questions == "":
            heading = f"*** Continuous Mode: Question" \
                      f" {questions_answered + 1} ***"
        else:
            heading = f"*** Question {questions_answered + 1}" \
                      f" of {questions} ***"

        color_text(heading, 'yellow')

        # Generate random num for different difficulty
        if mode_choice == "easy" or mode_choice == "medium":
            if mode_choice == "easy":
                max_num = 100
                number_a_m = 1
            if mode_choice == "medium":
                max_num = 500
                number_a_m = random.randint(1, 5)
            random_num = random.randint(1, max_num)


        else:
            max_num = 1000
            random_num = round(random.uniform(1, max_num), 2)
            number_a_m = round(random.uniform(0.01, 0.05), 2)

        # generate answer with chosen questions
        if question_type == "addition":
            answer = random_num + number_a_m
            less_more = "more"
        if question_type == "subtraction":
            answer = random_num - number_a_m
            less_more = "less"
        else:
            add_or_sub = random.randint(1, 10)
            if add_or_sub > 5:
                answer = random_num + number_a_m
                less_more = "more"
            else:
                answer = random_num - number_a_m
                less_more = "less"

        # Ask user for there guess
        user_guess = num_check(f"What is {number_a_m} {less_more} than {random_num}: ", int, 0, max_num + 1)

        # Print result in color and set outcome
        if user_guess == answer:
            result = "Correct ✔"
            # Set color to green
            color_result = "\033[92m" + result + "\033[0m"
            color_text("Correct ✔", 'green')
            questions_right += 1
            outcome = f"Question {questions_answered + 1}: {color_result}"

        # End quiz if exit code is typed
        elif user_guess == "xxx":
            break

        # Print result in color and set outcome
        else:
            result = "Incorrect ❌"
            # Set color to red
            color_result = "\033[91m" + result + "\033[92m"
            color_text("Incorrect ❌", 'red')
            questions_right += 1
            outcome = f"Question {questions_answered + 1}: {color_result}, the correct answer was {answer}"

        questions_answered += 1
        # add results to quiz summary
        quiz_summary.append(outcome)

        # End quiz if requested # of questions has been played
        if questions_answered == questions:
            break


print()
color_text("Thanks for playing The Plus One Quiz 😃", "blue")
