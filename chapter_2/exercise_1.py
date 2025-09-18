# 1. The volume of a sphere with radius r is 4/3 pi r³. What is the volume of 
# a sphere with radius 5? Start with a variable named radius and then assign 
# the result to a variable named volume. Display the result. Add comments to 
# indicate that radius is in centimeters and volume in cubic centimeters.
import math


raio = 5 # raio de 5 centímetros 
volume = raio ** 3 * math.pi * 4/3 # volume em centímetros cúbicos
print(f"O volume de uma esfera com raio de 5 centímetros é de \
{volume:.1f} cm³")
    