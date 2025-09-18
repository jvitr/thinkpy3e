# In addition to pi, the other variable defined in the math module is e, which 
# represents the base of the natural logarithm, written in math notation as e. 
# If you are not familiar with this value, ask a virtual assistant “What is 
# math.e?” Now let’s compute e² three ways:

# Use math.e and the exponentiation operator (**).
# Use math.pow to raise math.e to the power 2.
# Use math.exp, which takes as an argument a value, x, and computes ex.

# You might notice that the last result is slightly different from the other 
# two. See if you can find out which is correct.
import math


print(math.e ** 2)
print(math.pow(math.e, 2))
print(math.exp(2))
