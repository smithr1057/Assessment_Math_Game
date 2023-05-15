# V2 - Not using colorama to add color to text

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

# Loop over each character in the text
for i, char in enumerate(text):
    # Choose a color based on the character index
    color = colors[i % len(colors)]
    # Print the character in the chosen color
    print(color + char, end='')

# Reset the color
print('\033[0m')
