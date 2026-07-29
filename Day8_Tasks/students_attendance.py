#1. Student Attendance Record
#A teacher wants to store student attendance in a file named attendance.txt. Write a Python program that takes a student name as input and appends it to the file. Then
#display the contents of the file.

file = open("attendance.txt", "a")

name = input("Enter student name: ")

file.write(name + "\n")

file.close()

file = open("attendance.txt", "r")

print("\nAttendance Record:")
print(file.read())
file.close()
