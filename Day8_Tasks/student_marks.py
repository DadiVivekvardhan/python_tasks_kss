#4. Student Marks File Analyzer
#A teacher stores student marks in a file marks.txt in the format:
#Name Marks
#Example:
#Rahul 80
#Anita 90
#Ravi 75
#Write a Python program to:
#● Read the file
#● Display all student records
#● Calculate and display the average marks of the class

file = open("marks.txt", "r")

total = 0
count = 0

print("Student Records:")

for line in file:
    print(line)

    marks = int(line[-3:-1])

    total = total + marks
    count = count + 1

file.close()

average = total / count

print("Average Marks =", average)
