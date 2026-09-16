from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# --------------------------------------------------
# FastAPI App
# --------------------------------------------------

app = FastAPI(title="Student Management System")


# --------------------------------------------------
# MySQL Configuration
# --------------------------------------------------

DATABASE_URL = "mysql+pymysql://student_user:student123@localhost:3306/student_management"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


# --------------------------------------------------
# Database Model
# --------------------------------------------------

class StudentDB(Base):
    __tablename__ = "students_api"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    course = Column(String(100), nullable=False)
    marks = Column(Float, nullable=False)


# --------------------------------------------------
# Create table if it doesn't exist
# --------------------------------------------------

Base.metadata.create_all(bind=engine)


# --------------------------------------------------
# Pydantic Model
# --------------------------------------------------

class Student(BaseModel):
    name: str
    age: int
    course: str
    marks: float


# --------------------------------------------------
# Database Dependency
# --------------------------------------------------

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# --------------------------------------------------
# HOME
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Student Management System API is running"
    }


# --------------------------------------------------
# CREATE STUDENT
# --------------------------------------------------

@app.post("/students")
def add_student(student: Student, db: Session = Depends(get_db)):

    new_student = StudentDB(
        name=student.name,
        age=student.age,
        course=student.course,
        marks=student.marks
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student added successfully",
        "data": {
            "id": new_student.id,
            "name": new_student.name,
            "age": new_student.age,
            "course": new_student.course,
            "marks": new_student.marks
        }
    }


# --------------------------------------------------
# GET ALL STUDENTS
# --------------------------------------------------

@app.get("/students")
def get_students(db: Session = Depends(get_db)):

    students = db.query(StudentDB).all()

    data = []

    for student in students:
        data.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "course": student.course,
            "marks": student.marks
        })

    return {
        "count": len(data),
        "data": data
    }


# --------------------------------------------------
# GET STUDENT BY ID
# --------------------------------------------------

@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):

    student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student found",
        "data": {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "course": student.course,
            "marks": student.marks
        }
    }


# --------------------------------------------------
# UPDATE STUDENT
# --------------------------------------------------

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    student: Student,
    db: Session = Depends(get_db)
):

    existing_student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()

    if not existing_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.course = student.course
    existing_student.marks = student.marks

    db.commit()
    db.refresh(existing_student)

    return {
        "message": "Student updated successfully",
        "data": {
            "id": existing_student.id,
            "name": existing_student.name,
            "age": existing_student.age,
            "course": existing_student.course,
            "marks": existing_student.marks
        }
    }


# --------------------------------------------------
# DELETE STUDENT
# --------------------------------------------------

@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    deleted_data = {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "course": student.course,
        "marks": student.marks
    }

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully",
        "data": deleted_data
    }
