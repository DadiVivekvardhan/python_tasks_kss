#Q. Write a recursive function to calculate the sum of digits of a number.
#Example: Input = 123 → Output = 6

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)

num = int(input("Enter a number: "))
print("Sum of digits =", sum_digits(num))
