import colorama
import random

colorama.init()

# List of colors
colors = [
    colorama.Fore.RED,
    colorama.Fore.YELLOW,
    colorama.Fore.GREEN,
    colorama.Fore.CYAN,
    colorama.Fore.BLUE,
    colorama.Fore.MAGENTA,
]

# Your text
text = "Hello, world!"

# Loop over each character in the text
for char in text:
    # Choose a random color
    color = random.choice(colors)
    # Print the character in the chosen color
    print(color + char, end='')

# Reset the color
print(colorama.Style.RESET_ALL)


