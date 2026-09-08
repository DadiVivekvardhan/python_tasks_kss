from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta

app = FastAPI()

# =========================
# JWT CONFIGURATION
# =========================

SECRET_KEY = "student-management-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# =========================
# USER LOGIN DETAILS
# =========================

USERNAME = "admin"
PASSWORD = "admin123"


# =========================
# STUDENT MODEL
# =========================

class Student(BaseModel):
    name: str
    age: int
    course: str
    email: str


# =========================
# TEMPORARY STUDENT DATA
# =========================

students = {}
student_id_counter = 1


# =========================
# CREATE ACCESS TOKEN
# =========================

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# =========================
# VERIFY TOKEN
# =========================

def verify_token(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid or expired token"
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise credentials_exception

        return username

    except JWTError:
        raise credentials_exception


# =========================
# LOGIN
# =========================

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    if (
        form_data.username != USERNAME
        or form_data.password != PASSWORD
    ):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )

    access_token = create_access_token(
        {"sub": form_data.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# =========================
# HOME
# =========================

@app.get("/")
def home():
    return {
        "message": "Student Management API is running"
    }


# =========================
# CREATE STUDENT
# =========================

@app.post("/students")
def create_student(
    student: Student,
    username: str = Depends(verify_token)
):

    global student_id_counter

    students[student_id_counter] = {
        "student_id": student_id_counter,
        "name": student.name,
        "age": student.age,
        "course": student.course,
        "email": student.email
    }

    created_student = students[student_id_counter]

    student_id_counter += 1

    return {
        "message": "Student created successfully",
        "student": created_student
    }


# =========================
# GET ALL STUDENTS
# =========================

@app.get("/students")
def get_students(
    username: str = Depends(verify_token)
):

    return {
        "students": list(students.values())
    }


# =========================
# GET ONE STUDENT
# =========================

@app.get("/students/{student_id}")
def get_student(
    student_id: int,
    username: str = Depends(verify_token)
):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]


# =========================
# UPDATE STUDENT
# =========================

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    student: Student,
    username: str = Depends(verify_token)
):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    students[student_id] = {
        "student_id": student_id,
        "name": student.name,
        "age": student.age,
        "course": student.course,
        "email": student.email
    }

    return {
        "message": "Student updated successfully",
        "student": students[student_id]
    }


# =========================
# DELETE STUDENT
# =========================

@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    username: str = Depends(verify_token)
):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }
