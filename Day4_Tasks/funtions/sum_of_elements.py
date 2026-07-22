#Q. Write a function to find the sum of elements in a list using a user-defined function.

def sum_list(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total

my_list = [10, 20, 30, 40, 50]
print("Sum of elements =", sum_list(my_list))
