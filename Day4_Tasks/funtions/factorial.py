#Q. Write a function that returns the factorial of a number.


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

number = int(input("Enter a number: "))
print("Factorial =", factorial(number))
