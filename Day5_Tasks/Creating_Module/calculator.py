#Create a Python module named calculator.py that contains functions to perform:
#● Addition
#● Subtraction
#● Multiplication
#● Division
#Then write another Python program that imports this module and performs calculations based on user input.


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b
