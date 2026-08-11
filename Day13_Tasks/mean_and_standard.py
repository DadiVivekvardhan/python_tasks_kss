#Q. Remove Outliers
#Given data:
#values = np.array([10, 12, 15, 18, 100, 14, 13])
#Task:
#● Compute the mean and standard deviation
#● Remove values that are more than 2 standard deviations from the mean

import numpy as np

values = np.array([10, 12, 15, 18, 100, 14, 13])

mean = np.mean(values)
std = np.std(values)

filtered = values[np.abs(values - mean) <= 2 * std]

print("Mean:", mean)
print("Standard deviation:", std)
print("Values after removing outliers:", filtered)
