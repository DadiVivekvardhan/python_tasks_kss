#Develop a Python program to manage student marks for three subjects. Store the subject names in a tuple

subjects = ("Math", "Science", "English")

#maintain unique student names in a set,
student_names = set()

#store each student’s marks in a list inside a dictionary where the key is the student name
students = {}


#Implement a recursive function to calculate the total marks from the list of marks.
def total_marks(marks, index):
    if index == len(marks):
        return 0
    return marks[index] + total_marks(marks, index + 1)



#Create user-defined functions to add a student with marks
#Also include exception handling to handle ValueError (non-numeric marks input)
#ZeroDivisionError(average calculation issues)
#TypeError (incorrect data type in marks)
#NameError (when a student name entered does not exist in the dictionary).
def add_student():
    try:
        name = input("Enter student name: ")

        marks = []

        for subject in subjects:
            mark = int(input(f"Enter marks for {subject}: "))

            if not isinstance(mark, int):
                raise TypeError

            marks.append(mark)

        student_names.add(name)
        students[name] = marks

        print("Student added successfully!")

    except ValueError:
        print("Error: Please enter numeric marks only.")

    except TypeError:
        print("Error: Marks should be integers.")



#function to display all student records
def display_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        for name, marks in students.items():
            print(name, ":", marks)




#calculate the average marks of a student.            
def calculate_average():
    try:
        name = input("Enter student name to calculate average: ")

        if name not in students:
            raise NameError

        marks = students[name]

        total = total_marks(marks, 0)

        average = total / len(marks)

        print("Total Marks:", total)
        print("Average Marks:", average)

    except NameError:
        print("Error: Student name does not exist.")

    except ZeroDivisionError:
        print("Error: Cannot calculate average.")

    except TypeError:
        print("Error: Invalid marks data.")


#The program should interact with the user through a simple menu
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        calculate_average()

    elif choice == "4":
        print("Program Ended.")
        break

    else:
        print("Invalid choice. Please try again.")
