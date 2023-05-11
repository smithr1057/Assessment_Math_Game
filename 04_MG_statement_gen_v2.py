# Functions

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


# Main routine goes here
title = statement_generator("Welcome to the Math Game", "*", 3)
print(title)
