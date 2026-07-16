#Q.Write a program to find the student with the highest marks from a dictionary.


students = {
    "Rahul": 85,
    "Anu": 92,
    "Vivek": 78
}

highest = max(students, key=students.get)

print("Student:", highest)
print("Marks:", students[highest])
