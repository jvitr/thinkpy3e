# The song “99 Bottles of Beer” starts with this verse:
#    99 bottles of beer on the wall
#    99 bottles of beer
#    Take one down, pass it around
#    98 bottles of beer on the wall

# Then the second verse is the same, except that it starts with 98 bottles and 
# ends with 97. The song continues – for a very long time – until there are 0 
# bottles of beer.

# Write a function called bottle_verse that takes a number as a parameter and 
# displays the verse that starts with the given number of bottles.

# Hint: Consider starting with a function that can print the first, second, or 
# last line of the verse, and then use it to write bottle_verse.

# Use this function call to display the first verse.
# bottle_verse(99)
# If you want to print the whole song, you can use this for loop, which counts 
# down from 99 to 1. 

def print_last_line(number_of_bottles):
    print(f"{number_of_bottles} bottles of beer on the wall ")
    print()

def bottle_verse(bottles):
    for i in range(bottles, 0, -1):
        print(f"{bottles} bottles of beer on the wall")
        print(f"{bottles} bottles of beer")
        print(f"Take one down, pass it around")
        bottles = i - 1
        print_last_line(bottles)

bottle_verse(10)