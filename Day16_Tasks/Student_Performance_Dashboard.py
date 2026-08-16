#1. Student Performance Dashboard
#Scenario:
#A school records marks of students in one subject:
#marks = np.array([45, 67, 89, 56, 72, 91, 38])
#students = ["A", "B", "C", "D", "E", "F", "G"]
#Task:
#● Convert to Pandas DataFrame
#● Plot:
#○ Line graph → trend of marks
#○ Bar chart → student vs marks
#○ Pie chart → Pass (>50) vs Fail
#○ Histogram → distribution of marks
#○ Scatter plot → index vs marks

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({
    "Student": students,
    "Marks": marks})

print(df)

pass_count = (df["Marks"] > 50).sum()
fail_count = (df["Marks"] <= 50).sum()

plt.subplot(2, 3, 1)
plt.plot(df["Student"], df["Marks"], marker="o")
plt.title("Student Marks Trend")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.grid(True)

plt.subplot(2, 3, 2)
plt.bar(df["Student"], df["Marks"])
plt.title("Student vs Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.subplot(2, 3, 3)
plt.pie([pass_count, fail_count],labels=["Pass", "Fail"],autopct="%1.1f%%")
plt.title("Pass vs Fail")

plt.subplot(2, 3, 4)
plt.hist(df["Marks"], bins=5, edgecolor="black")
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")


plt.subplot(2, 3, 5)
plt.scatter(df.index, df["Marks"])
plt.title("Index vs Marks")
plt.xlabel("Index")
plt.ylabel("Marks")

plt.tight_layout()

plt.show()
