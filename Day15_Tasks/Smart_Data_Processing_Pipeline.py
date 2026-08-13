#9. Smart Data Processing Pipeline
#Scenario:
#A system processes numeric data from file.
#Task:
#● Read numbers from a file
#● Use NumPy for calculations (mean, std)
#● Convert results to Pandas DataFrame
#● Use exception handling for bad data
#● Use a generator to stream data
#● Apply decorator to measure execution time

import numpy as np
import pandas as pd
import time

def read_numbers(filename):
    with open(filename, "r") as file:
        for line in file:
            try:
                number = float(line.strip())
                yield number
            except ValueError:
                print("Bad data skipped:", line.strip())

def measure_time(function):
    def wrapper():
        start = time.time()

        result = function()

        end = time.time()

        print("Execution time:", end - start, "seconds")

        return result

    return wrapper

@measure_time
def process_data():

    numbers = []

    for number in read_numbers("numbers.txt"):
        numbers.append(number)
        
    arr = np.array(numbers)
    
    mean_value = np.mean(arr)
    std_value = np.std(arr)

    df = pd.DataFrame({
        "Mean": [mean_value],
        "Standard Deviation": [std_value]
    })

    print("\nResults:")
    print(df)
    
process_data()
