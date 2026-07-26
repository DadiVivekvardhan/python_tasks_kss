#Q.Write a Python program using the math module to calculate and display the square root, floor value, and ceiling value of a number entered by the user.

import math

num = float(input("Enter a number: "))

square_root = math.sqrt(num)
floor_value = math.floor(num)
ceiling_value = math.ceil(num)


print("Square root:", square_root)
print("Floor value:", floor_value)
print("Ceiling value:", ceiling_value)
