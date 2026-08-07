
#Q. Find Indexes of Specific Value
#A quality check system stores product defect codes:
#[2, 4, 1, 4, 3, 4, 5]
#Task:
#● Find the indexes where value = 4 using NumPy searching.


import numpy as np

defect_codes = np.array([2, 4, 1, 4, 3, 4, 5])

indexes = np.where(defect_codes == 4)

print("Defect Codes:", defect_codes)
print("Indexes of value 4:", indexes)
