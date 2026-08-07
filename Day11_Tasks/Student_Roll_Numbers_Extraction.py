#Q. Student Roll Numbers Extraction
#A list contains roll numbers:
#[101, 102, 103, 104, 105, 106]
#Scenario:
#You want only the middle students (index 2 to 4).
#Task:
#● Use NumPy slicing to extract those values.

import numpy as np

roll_numbers = np.array([101, 102, 103, 104, 105, 106])

middle_students = roll_numbers[2:5]

print("Roll Numbers:", roll_numbers)
print("Middle Students:", middle_students)
