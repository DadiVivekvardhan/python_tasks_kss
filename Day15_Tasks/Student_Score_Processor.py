#1. Student Score Processor
#Scenario:
#A teacher stores student names and marks in a list of tuples.
#Task:
#● Convert data into a dictionary
#● Use a loop + condition to find students scoring above 50
#● Use math module to calculate average
#● Store results in a text file

import math

students = [
    ("Rahul", 45),
    ("Anu", 75),
    ("Vivek", 60),
    ("Priya", 40),
    ("Kiran", 85)]

student_dict = dict(students)

print("Student Dictionary:")
print(student_dict)

# 2. Find students scoring above 50
above_50 = []

for name, marks in student_dict.items():
    if marks > 50:above_50.append((name, marks))

print("\nStudents scoring above 50:")

for name, marks in above_50:
    print(name, marks)

total = sum(student_dict.values())
count = len(student_dict)

average = math.fsum(student_dict.values()) / count

print("\nAverage marks:", average)

with open("student_results.txt", "w") as file:

    file.write("Students scoring above 50:\n")

    for name, marks in above_50:
        file.write(f"{name}: {marks}\n")

    file.write(f"\nAverage marks: {average}")

print("\nResults saved to student_results.txt")
