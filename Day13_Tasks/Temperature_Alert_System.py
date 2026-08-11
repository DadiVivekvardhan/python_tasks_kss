#3. Temperature Alert System
#Temperatures recorded in a city:
#temps = np.array([28, 32, 35, 31, 29, 40, 38])
#Task:
#● Identify days where temperature is greater than 30.
#● Return their indices.


import numpy as np

temps = np.array([28, 32, 35, 31, 29, 40, 38])

condition = temps > 30

indices = np.where(condition)[0]

print("Temperatures above 30:", temps[condition])
print("Their indices:", indices)
