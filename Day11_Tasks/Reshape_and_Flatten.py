#Q. Reshape and Flatten Image Data
#Scenario:
#An image is stored as a 2 × 3 matrix:
#[[1,2,3],
#[4,5,6]]
#Task:
#1. Convert it into a NumPy array.
#2. Flatten the array into 1-D format.
#3. Print the flattened array

import numpy as np

image = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flatten_image = image.flatten()

print("Original Array:")
print(image)

print("Flattened Array:")
print(flatten_image)
