
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = f"{sides} {statement} {sides}"
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine goes here
statement_generator("Welcome to The Math Game", "*")

