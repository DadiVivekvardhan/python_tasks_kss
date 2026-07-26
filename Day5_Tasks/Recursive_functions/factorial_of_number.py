#Q. Write a recursive function to calculate the factorial of a number.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print("Factorial of", num, "is", factorial(num))
