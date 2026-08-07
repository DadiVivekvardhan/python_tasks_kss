#9. Multi-Department Data Aggregation
#A company collects employee counts from two branches.
#Branch A:
#[[10, 20],
#[30, 40]]
#Branch B:
#[[5, 15],
#[25, 35]]
#Scenario:
#● Combine the two matrices.
#● Calculate the total employees across all departments.
#● Print the combined matrix and total.
import numpy as np

branch_A = np.array([
    [10, 20],
    [30, 40]
])

branch_B = np.array([
    [5, 15],
    [25, 35]
])

combined_matrix = branch_A + branch_B

total_employees = np.sum(combined_matrix)

print("Branch A:")
print(branch_A)

print("Branch B:")
print(branch_B)

print("Combined Matrix:")
print(combined_matrix)

print("Total Employees:", total_employees)
