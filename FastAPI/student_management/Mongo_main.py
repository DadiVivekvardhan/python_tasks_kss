from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pymongo import MongoClient
import certifi


# --------------------------------------------------
# MongoDB Connection
# --------------------------------------------------


# MongoDB Connection
MONGO_URL ="mongodb+srv://vivekvardhandadi_db_user:Shankar2013@cluster0.xwc4uhe.mongodb.net/?appName=Cluster0"

client = MongoClient(
    MONGO_URL,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=30000
)

database = client["student_management"]

students_collection = database["students"]


# Test MongoDB connection
try:
    client.admin.command("ping")
    print("MongoDB connected successfully")
except Exception as e:
    print("MongoDB connection failed:", e)


# FastAPI
app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Student Management API is running"
    }

# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="Student Management API",
    description="Student Management System using FastAPI and MongoDB",
    version="1.0.0"
)


# --------------------------------------------------
# Student Model
# --------------------------------------------------

class Student(BaseModel):
    student_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=5, le=100)
    course: str = Field(..., min_length=2, max_length=100)
    email: str


# --------------------------------------------------
# Home API
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Student Management API is running"
    }


# --------------------------------------------------
# CREATE STUDENT - POST
# --------------------------------------------------

@app.post("/students")
def create_student(student: Student):

    # Check whether student already exists
    existing_student = students_collection.find_one(
        {"student_id": student.student_id}
    )

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    # Convert Pydantic model to dictionary
    student_data = student.model_dump()

    # Insert into MongoDB
    students_collection.insert_one(student_data)

    return {
        "message": "Student created successfully",
        "student": student_data
    }


# --------------------------------------------------
# GET ALL STUDENTS - GET
# --------------------------------------------------

@app.get("/students")
def get_students():

    students = list(
        students_collection.find(
            {},
            {"_id": 0}
        )
    )

    return {
        "students": students
    }


# --------------------------------------------------
# GET STUDENT BY ID - GET
# --------------------------------------------------

@app.get("/students/{student_id}")
def get_student(student_id: int):

    student = students_collection.find_one(
        {"student_id": student_id},
        {"_id": 0}
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# --------------------------------------------------
# UPDATE STUDENT - PUT
# --------------------------------------------------

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    # Check whether the student exists
    existing_student = students_collection.find_one(
        {"student_id": student_id}
    )

    if not existing_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Make sure the ID in the URL and body are the same
    if student.student_id != student_id:
        raise HTTPException(
            status_code=400,
            detail="Student ID in URL and body must be the same"
        )

    student_data = student.model_dump()

    students_collection.update_one(
        {"student_id": student_id},
        {"$set": student_data}
    )

    return {
        "message": "Student updated successfully",
        "student": student_data
    }


# --------------------------------------------------
# DELETE STUDENT - DELETE
# --------------------------------------------------

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    result = students_collection.delete_one(
        {"student_id": student_id}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }

