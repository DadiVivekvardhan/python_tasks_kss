#Q. Random Data & Filtering
#Generate random numbers:
#nums = np.random.randint(1, 100, 10)
#Task:
#● Filter values that are divisible by 5
#● Return sorted result.

import numpy as np

nums = np.random.randint(1, 100, 10)

filtered = nums[nums % 5 == 0]

result = np.sort(filtered)

print("Random numbers:", nums)
print("Divisible by 5:", result)
