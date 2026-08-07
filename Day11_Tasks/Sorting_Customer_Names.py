#Q. Sorting Customer Names
#A system stores customer names:
#["Ravi", "Anil", "Sita", "John"]
#Task:
#● Convert it to a NumPy array.
#● Sort the names alphabetically.

import numpy as np

customers = np.array(["Ravi", "Anil", "Sita", "John"])

sorted_customers = np.sort(customers)


print("Original Names:", customers)
print("Sorted Names:", sorted_customers)
