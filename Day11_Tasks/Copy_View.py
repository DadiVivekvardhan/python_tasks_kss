#Q. Copy vs View Behavior in Data Processing
#Scenario:
#A dataset:
#[10, 20, 30, 40]
#Task:
#● Create a copy of the array.
#● Modify the original array.
#● Show that the copy does not change.
#● Repeat using view() and observe the difference.

import numpy as np

data = np.array([10, 20, 30, 40])

#● Create a copy of the array.
copy_data = data.copy()

#● Modify the original array.
data[0] = 100

#● Show that the copy does not change.
print("Original Array:", data)
print("Copy Array:", copy_data)

#● Repeat using view() and observe the difference.
data2 = np.array([10, 20, 30, 40])

view_data = data2.view()

data2[0] = 100

print("Original Array (View):", data2)
print("View Array:", view_data)
