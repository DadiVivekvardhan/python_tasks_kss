#Q. Create a dictionary with 3 student names and their marks.

students = {
    "Rahul": {
        "Maths": 85,
        "Science": 90,
        "English": 88
    },
    "Anu": {
        "Maths": 92,
        "Science": 95,
        "English": 91
    },
    "Vivek": {
        "Maths": 78,
        "Science": 82,
        "English": 80
    }
}

for name, marks in students.items():
    print(name, ":", marks)
