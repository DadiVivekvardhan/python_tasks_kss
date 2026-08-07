#10. Data Processing Pipeline
#A data pipeline receives the following array:
#[12, 7, 25, 3, 18, 10]
#Scenario:
#1. Convert the list into a NumPy array.
#2. Sort the array.
#3. Split the sorted array into two equal parts.
#4. Calculate the sum of each part.
#Output:
#● Sorted array
#● Two split arrays
#● Sum of each part

import numpy as np

data = np.array([12, 7, 25, 3, 18, 10])

sorted_data = np.sort(data)

split_data = np.split(sorted_data, 2)

sum_part1 = np.sum(split_data[0])
sum_part2 = np.sum(split_data[1])
print("Sorted Array:", sorted_data)
print("First Split:", split_data[0])
print("Second Split:", split_data[1])
print("Sum of First Part:", sum_part1)
print("Sum of Second Part:", sum_part2)
