#Q. Write a recursive function to find the nth Fibonacci number.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter a number: "))
print("The", num, "th Fibonacci number is", fibonacci(num))
