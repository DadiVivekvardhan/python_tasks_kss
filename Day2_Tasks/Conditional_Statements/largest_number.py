#Q. Write a program to find the largest of three numbers using if-elif-else.

a = int(input("Enter first number: "))

b = int(input("Enter second number: "))

c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is", a)
    
elif b >= a and b >= c:
    print("Largest number is", b)
    
else:
    print("Largest number is", c)
