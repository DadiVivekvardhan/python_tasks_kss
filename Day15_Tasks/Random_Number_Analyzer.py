#2. Random Number Analyzer
#Scenario:
#A system generates random numbers for testing.
#Task:
#● Use random to generate 10 numbers
#● Store in a list
#● Use loop + condition to count even/odd numbers
#● Use set to remove duplicates

import random

numbers = []

for i in range(10):
    number = random.randint(1, 20)
    numbers.append(number)

print("Random numbers:")
print(numbers)

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\nEven numbers count:", even_count)
print("Odd numbers count:", odd_count)

unique_numbers = set(numbers)

print("\nNumbers after removing duplicates:")
print(unique_numbers)
