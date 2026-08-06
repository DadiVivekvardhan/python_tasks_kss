#University Staff Management (Hierarchical Inheritance)
#A university has different staff types such as Professor, LabAssistant, and Administrator. All inherit from a base class Staff. Implement hierarchical inheritance
#to manage and display their information.

class Staff:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Professor(Staff):

    def display(self):
        print("Professor Name :", self.name)
        print("Salary :", self.salary)


class LabAssistant(Staff):

    def display(self):
        print("Lab Assistant Name :", self.name)
        print("Salary :", self.salary)


class Administrator(Staff):

    def display(self):
        print("Administrator Name :", self.name)
        print("Salary :", self.salary)

p = Professor("Ramesh", 80000)
l = LabAssistant("Sita", 30000)
a = Administrator("Arun", 50000)

p.display()
print()

l.display()
print()

a.display()
