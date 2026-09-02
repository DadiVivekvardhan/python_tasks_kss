from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Student Management System")


# Student model
class Student(BaseModel):
    name: str
    age: int
    course: str


# Store students
students = []

# ID counter
next_id = 1


# Home
@app.get("/")
def home():
    return {"message": "Student Management System API is running"}


# Create student
@app.post("/students")
def add_student(student: Student):
    global next_id

    new_student = {
        "id": next_id,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    students.append(new_student)
    next_id += 1

    return {
        "message": "Student added successfully",
        "data": new_student
    }


# Get all students
@app.get("/students")
def get_students():
    return {
        "count": len(students),
        "data": students
    }


# Get student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return {
                "message": "Student found",
                "data": student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# Update student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for existing_student in students:
        if existing_student["id"] == student_id:
            existing_student["name"] = student.name
            existing_student["age"] = student.age
            existing_student["course"] = student.course

            return {
                "message": "Student updated successfully",
                "data": existing_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)

            return {
                "message": "Student deleted successfully",
                "data": student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )