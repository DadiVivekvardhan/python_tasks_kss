#1. Student Marks Analysis
#A teacher stores the marks of 5 students in a NumPy array.
#Scenario:
#You are given marks [45, 67, 89, 56, 72].
#Task:
#● Convert the list into a NumPy array.
#● Add 5 grace marks to every student.
#● Print the updated marks.
import numpy as np

marks = [45, 67, 89, 56, 72]

marks_array = np.array(marks)

updated_marks = marks_array + 5

print("Original Marks:", marks_array)
print("Updated Marks:", updated_marks)
