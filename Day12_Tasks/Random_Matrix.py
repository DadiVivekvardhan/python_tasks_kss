#10. Random Matrix and Condition Filtering
#Scenario:
#● Generate a 3×3 matrix of random numbers (0–50).
#Task:
#● Filter elements greater than 25.
#● Print filtered values.

import numpy as np
matrix = np.random.randint(0, 51, (3, 3))

print("Random Matrix:")
print(matrix)

filtered_values = matrix[matrix > 25]

print("Values greater than 25:")
print(filtered_values)
