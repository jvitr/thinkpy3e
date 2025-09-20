# Write a function named print_right that takes a string named text as a 
# parameter and prints the string with enough leading spaces that the last 
# letter of the string is in the 40th column of the display.

# Hint: Use the len function, the string concatenation operator (+) and the 
# string repetition operator (*).

def print_right(text):
    print(" " * (40 - len(text)) + text)

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")