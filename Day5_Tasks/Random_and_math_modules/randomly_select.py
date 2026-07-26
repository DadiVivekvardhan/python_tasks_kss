#Q.Write a program that uses random.choice() to randomly select a student from a list and display:
#"The selected student for presentation is: <name>".

import random

students = ["VIVEK", "ROHIT", "MESSI","VIRAT"]

selected_student = random.choice(students)

print("The selected student for presentation is:", selected_student)
