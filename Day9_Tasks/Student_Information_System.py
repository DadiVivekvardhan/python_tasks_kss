#1. Student Information System (Class & Object)
#A school wants a program to store student details. Create a Student class with attributes such as name, roll number, and marks. Create objects for at least three
#students and display their details.


class Student:

    def __init__(self,name,roll_number,marks):
        self.name=name
        
        self.roll_number=roll_number
        
        self.marks=marks

    def display(self):
        
        print("Name:", self.name)
        
        print("Roll Number:", self.roll_number)
        
        print("Marks:", self.marks)
        
        print("------------------------")

student1 = Student("vivek", 1, 89)

student2 = Student("vardhan", 2, 76)

student3 = Student("Rohit", 3, 92)

student1.display()

student2.display()

student3.display()
