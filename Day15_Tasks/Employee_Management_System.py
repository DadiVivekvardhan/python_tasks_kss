#5. Employee Management System (OOP + File + Dict)
#Scenario:
#Manage employee data.
#Task:
#● Create a class Employee
#● Store employees in a dictionary
#● Save data to a file
#● Use exception handling for invalid salary input
#● Use loop to display all employees


class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print()


employees = {}

try:
    for i in range(3):

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")

        salary = float(input("Enter Employee Salary: "))

        employee = Employee(emp_id, name, salary)

        employees[emp_id] = employee

except ValueError:
    print("Invalid salary! Please enter a number.")

print("\nEmployee Details:")

for emp_id, employee in employees.items():
    employee.display()

try:
    with open("employees.txt", "w") as file:

        for emp_id, employee in employees.items():
            file.write(f"ID: {employee.emp_id}\n")
            file.write(f"Name: {employee.name}\n")
            file.write(f"Salary: {employee.salary}\n")
            file.write("-------------------\n")

    print("Employee data saved successfully.")

except Exception as e:
    print("Error while saving file:", e)
