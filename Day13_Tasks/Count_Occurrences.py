#Q. Count Occurrences
#You have:
#data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
#Task:
#● Count how many times each unique number appears.
#● Return numbers with their counts.

import numpy as np

data = np.array([1, 2, 2, 3, 1, 4, 2, 3])

numbers = np.unique(data)

for num in numbers:
    count = np.sum(data == num)
    print(num, ":", count)
