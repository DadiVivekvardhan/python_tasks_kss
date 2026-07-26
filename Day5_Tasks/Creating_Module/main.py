

import calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Result =", calculator.add(num1, num2))

elif choice == "2":
    print("Result =", calculator.subtract(num1, num2))

elif choice == "3":
    print("Result =", calculator.multiply(num1, num2))

elif choice == "4":
    print("Result =", calculator.divide(num1, num2))

else:
    print("Invalid choice!")
