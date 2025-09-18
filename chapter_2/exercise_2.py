# A rule of trigonometry says that for any value of x, (cos x)² + (sin x)² = 1.
# Let’s see if it’s true for a specific value of x like 42. Create a variable 
# named x with this value. Then use math.cos and math.sin to compute the sine 
# and cosine of x and the sum of their squared. The result should be close to 
# 1. 
# It might not be exactly 1 because floating-point arithmetic is not 
# exact—it is only approximately correct.
import math


x = 42 
print(math.sin(x) ** 2 + math.cos(x) ** 2)
