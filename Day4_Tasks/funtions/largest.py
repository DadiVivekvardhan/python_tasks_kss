#Q. Write a Python program with a function that returns the largest of three numbers.

def largest_of_three(num1,num2,num3):

if num1>=num2 and num1>=num3:
    return num1
elif num2>=num1 and num2>=num3:
    return num2
elif num3>=num1 and num3>=num2:
    return num3

a=int(input("Enter the value a:"))
b=int(input("Enter the value b:"))
c=int(input("Enter the value c:"))

print("The largest of three numbers ",largest_of_three(num1,num2,num3))_
