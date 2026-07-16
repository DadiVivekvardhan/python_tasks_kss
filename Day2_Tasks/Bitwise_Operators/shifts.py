#Q. Write a program to perform left shift (<<) and right shift (>>) operations on a number.

num = int(input("Enter a number: "))
shift = int(input("Enter number of positions to shift: "))

print("Left Shift =", num << shift)
print("Right Shift =", num >> shift)
