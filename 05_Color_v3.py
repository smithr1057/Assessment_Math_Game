# V3 - simpler way to do a random color

import random

# Your text
text = "Hello, world!"

# List of ANSI escape codes for colors
colors = [
    '\033[31m',  # Red
    '\033[33m',  # Yellow
    '\033[32m',  # Green
    '\033[36m',  # Cyan
    '\033[34m',  # Blue
    '\033[35m',  # Magenta
]


black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'


# Choose a random color
color = random.choice(colors)
# Print the character in the chosen color
print(color + text)
