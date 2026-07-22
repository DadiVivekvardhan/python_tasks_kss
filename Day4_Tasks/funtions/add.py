#Q. Write a program using a user-defined function to add two numbers.

def add(a, b):
    return a + b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", add(a, b))
