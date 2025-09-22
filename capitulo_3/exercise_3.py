# Write a function called rectangle that takes a string and two integers and 
# draws a rectangle with the given width and height, made up using copies of 
# the string. Here’s an example of a rectangle with width 5 and height 4, 
# made up of the string 'H'.

def rectangle(text, width, height):
    for i in range(height):
        print(text * width)
    
rectangle("H", 5, 4)