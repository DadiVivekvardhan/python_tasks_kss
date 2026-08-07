#Q. Check Data Type of Inventory Values
#A warehouse stores product quantities:
#[10, 20, 30, 40]
#Task:
#● Convert it into a NumPy array.
#● Print the data type (dtype) of the array

import numpy as np

quantities = [10, 20, 30, 40]

inventory = np.array(quantities)

print("Inventory:", inventory)
print("Data Type:", inventory.dtype)
