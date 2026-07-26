#Write a Python program that generates 20 random numbers between 1 and 200 using the random module and store them in a list.
#Then using the math module, compute and display:
#● Maximum value
#● Minimum value
#● Square root of the maximum number
#● Logarithm of the minimum number

import random
import math

numbers = []

for i in range(20):
    numbers.append(random.randint(1, 200))

print("Random Numbers:", numbers)

maximum = max(numbers)
minimum = min(numbers)

print("Maximum value:", maximum)
print("Minimum value:", minimum)
print("Square root of the maximum number:", math.sqrt(maximum))
print("Logarithm of the minimum number:", math.log(minimum))
