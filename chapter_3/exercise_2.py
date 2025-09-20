# Write a function called triangle that takes a string and an integer and draws 
# a pyramid with the given height, made up using copies of the string. 

def triangle(text, levels):
    for i in range(levels):
        print(text * (i + 1))

triangle("L", 5)