#12. Random Dataset Normalization + Filtering
#Scenario:
#● Generate 8 random float values between 0 and 1.
#Task:
#1. Normalize by multiplying with 100
#2. Filter values greater than 50
#3. Sort the filtered values

import numpy as np

data = np.random.rand(8)
print("Original data:")
print(data)

normalized = data * 100
print("Normalized data:")
print(normalized)

filtered = normalized[normalized > 50]

sorted_values = np.sort(filtered)

print("Values greater than 50:")
print(filtered)

print("Sorted values:")
print(sorted_values)
