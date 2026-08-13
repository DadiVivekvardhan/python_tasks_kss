#10. Advanced Simulation System
#Scenario:
#Simulate exam results and generate reports.
#Task:
#● Generate random marks using random
#● Store in NumPy array
#● Convert to Pandas DataFrame
#● Use OOP to represent Student
#● Use conditions + loops to assign grades
#● Save report to file
#● Handle errors using try-except
#● Use math module for statistics

import random
import numpy as np
import pandas as pd
import math


# OOP: Create Student class
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"


try:

    names = ["Vivek", "Rahul", "Anu", "Kiran", "Ravi"]

    marks = [random.randint(0, 100) for i in range(5)]

    marks_array = np.array(marks)

    df = pd.DataFrame({
        "Name": names,
        "Marks": marks_array
    })

    grades = []

    for i in range(len(df)):

        student = Student(df.loc[i, "Name"], df.loc[i, "Marks"])

        grade = student.get_grade()

        grades.append(grade)

    df["Grade"] = grades

    total = sum(marks)
    average = total / len(marks)

    variance = sum((x - average) ** 2 for x in marks) / len(marks)
    standard_deviation = math.sqrt(variance)

    print("Student Report")
    print(df)

    print("\nAverage Marks:", average)
    print("Standard Deviation:", standard_deviation)

    with open("exam_report.txt", "w") as file:

        file.write("Student Exam Report\n")
        file.write("===================\n")
        file.write(df.to_string())
        file.write("\n\nAverage Marks: " + str(average))
        file.write("\nStandard Deviation: " + str(standard_deviation))

    print("\nReport saved successfully!")

except Exception as e:

    print("An error occurred:", e)
