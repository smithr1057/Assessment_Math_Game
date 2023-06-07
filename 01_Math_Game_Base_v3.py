import random
# V3 - Fixing all of ChatGPTs errors
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
          "answer (press <enter> for continuous mode).")
    print()
    print("Choose mode.")
    print("Easy mode - Add / subtract 1 to a number up to 100.")
    print("Medium mode - Add / subtract 1-5 to a number up to 500.")
    print("Hard mode - Add / subtract 0.01-0.05 to a number up to 1000.")
    print()
    print("Next you will need to enter if you would like to answer addition, subtraction or both.")
    print()
    print("You will also need to choose if you would like negative numbers.")
    print()
    print("You can enter 'xxx' at any time during the quiz to quit.")
    print()
    print("After you finish your quiz you can choose to see your "
          "quiz history and statistics.")
    print()
    print("At the end of the quiz you may choose to begin a new quiz.")
    print()
    print("Good Luck :D")
    print()
    return ""


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
            if type == "int":
                color_text("Please enter an integer or 'xxx'", 'red')
            else:
                color_text("Please enter a number or 'xxx'", 'red')
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
question_type_list = ["addition", "subtraction", "both"]

# Errors
y_n_error = "Please enter either yes or no"
mode_error = "Please choose either easy, medium or hard"
question_type_error = "Please choose either addition, subtraction or both"

# Prints title with decorations and color
title = statement_generator("Welcome to The Addition and Subtraction Quiz", "*", 3)
colour_title = color_text(title, 'cyan')

# Asks users if they have played before
# if 'no' then print instructions
played_before = choice_checker("Have you played before? ", y_n_list, y_n_error)
if played_before == "no":
    instructions()

play_again = "yes"
while play_again == "yes":

    # Set questions answered, wrong, right to 0 and empty quiz summary
    questions_answered = 0
    questions_wrong = 0
    questions_right = 0
    quiz_summary = []

    # Ask user for # of questions, <enter> for infinite mode
    questions = num_check("How many questions: ", int, 0)

    # Choose difficulty and question type
    mode_choice = choice_checker("Easy, Medium or Hard? ", mode_list, mode_error)
    question_type = choice_checker("Would you like addition, subtraction or both? "
                                   , question_type_list, question_type_error)
    negative_num = choice_checker("Would you like negative numbers? ", y_n_list, y_n_error)

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

        # Generate random number for different difficulty
        if mode_choice == "easy":
            add_sub_num = 1
            low_num = -100 - add_sub_num if negative_num == "yes" else 1
            max_num = 100 + add_sub_num
            random_num = random.randint(low_num, max_num)
        elif mode_choice == "medium":
            add_sub_num = random.randint(1, 5)
            low_num = -500 - add_sub_num if negative_num == "yes" else 1
            max_num = 500 + add_sub_num
            random_num = random.randint(low_num, max_num)
        else:
            add_sub_num = round(random.uniform(0.01, 0.05), 2)
            low_num = -1000 - add_sub_num if negative_num == "yes" else 1
            max_num = 1000 + add_sub_num
            random_num = round(random.uniform(low_num, max_num), 2)

        # Determine question type
        if question_type == "addition":
            add_or_sub = 1
        elif question_type == "subtraction":
            add_or_sub = -1
        else:
            add_or_sub = random.choice([1, -1])

        # Calculate answer and determine less/more
        answer = random_num + (add_sub_num * add_or_sub)
        less_more = "more" if add_or_sub == 1 else "less"

        # Ask user for their answer
        rounded_answer = round(answer, 2)
        user_answer = num_check(f"What is {add_sub_num} {less_more} than {random_num}: ", int, low_num, max_num)

        # Print result in color and set outcome
        if user_answer == rounded_answer:
            result = "Correct ✔"
            # Set color to green
            color_result = "\033[92m" + result + "\033[0m"
            print(color_result)
            questions_right += 1
            outcome = f"Question {questions_answered + 1}: {color_result}"

        # End quiz if exit code is entered
        elif user_answer == "xxx":
            break

        # Print result in color and set outcome
        else:
            result = "Incorrect ❌"
            # Set color to red
            color_result = "\033[91m" + result + "\033[91m"
            print(color_result)
            questions_wrong += 1
            # Set the color to red for my outcome if answer is incorrect
            user_wrong_answer = f"{add_sub_num} {less_more} than {random_num} is not {user_answer}"
            color_wrong_answer = "\033[91m" + user_wrong_answer + "\033[92m"
            outcome = f"Question {questions_answered + 1}: {color_result}, {color_wrong_answer}, the correct answer was {rounded_answer}"

        # add results to quiz summary
        quiz_summary.append(outcome)

        questions_answered += 1

        # End quiz if requested # of questions has been played
        if questions_answered == questions:
            break

    if questions_answered >= 1:
        # Ask user if they want to see their quiz history
        # if 'yes' show quiz history
        print()
        show_stats = choice_checker("Would you like to see your"
                                    " end quiz history? "
                                    , y_n_list, y_n_error)

        # Calculate stats and print them out
        if show_stats == "yes":

            # Calculate quiz stat
            percent_right = questions_right / questions_answered * 100
            percent_wrong = questions_wrong / questions_answered * 100

            # Displays quiz history
            print()
            quiz_history = statement_generator("Quiz History", "-", 3)
            color_quiz_history = color_text(quiz_history, 'cyan')

            # Print the outcomes in order and in color
            for quiz in quiz_summary:
                color_text(quiz, 'yellow')

            print()

            # displays quiz stats with % values to the nearest whole number
            statement_generator("Quiz Statistics", "-", 3)
            color_text(f"Correct: {questions_right}, {percent_right:.0f}%", 'green')
            color_text(f"Incorrect: {questions_wrong}, {percent_wrong:.0f}%", 'red')

    # Ask user if they want to play again
    print()
    play_again = choice_checker("Would you like to play again? "
                                , y_n_list, y_n_error)
# If user hasn't played a round, comment
# Don't give them the option of quiz history
if questions_answered < 1:
    print()
    print("Maybe play the quiz next time 🤦‍♂️")
else:
    print()
    color_text("Thanks for playing The Addition and Subtraction Quiz 😃", "blue")
