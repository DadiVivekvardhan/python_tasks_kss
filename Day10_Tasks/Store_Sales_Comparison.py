#5. Store Sales Comparison
#Two stores record daily sales for 3 days.
#Scenario:
#Store A = [200, 250, 300]
#Store B = [180, 270, 310]
#Task:
#● Store them in NumPy arrays.
#● Find the daily difference in sales between the two stores.
#● Print the resulting array.

import numpy as np

store_A = np.array([200, 250, 300])
store_B = np.array([180, 270, 310])

difference = store_A - store_B

print("Store A Sales:", store_A)
print("Store B Sales:", store_B)
print("Daily Difference:", difference)
