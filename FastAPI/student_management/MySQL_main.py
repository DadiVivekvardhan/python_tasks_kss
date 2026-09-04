from fastapi import FastAPI
import pymysql

app = FastAPI()


# MySQL Connection
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Shankar@2013",
        database="student_management"
    )


# Home
@app.get("/")
def home():
    return {"message": "Student Management API"}


# GET - Get all students
@app.get("/students")
def get_students():
    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return students


# GET - Get one student
@app.get("/students/{student_id}")
def get_student(student_id: int):
    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute(
        "SELECT * FROM students WHERE id = %s",
        (student_id,)
    )

    student = cursor.fetchone()

    cursor.close()
    connection.close()

    if student:
        return student

    return {"message": "Student not found"}


# POST - Add student
@app.post("/students")
def add_student(name: str, age: int, course: str, marks: float):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO students (name, age, course, marks)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (name, age, course, marks))
    connection.commit()

    student_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return {
        "message": "Student added successfully",
        "id": student_id
    }


# PUT - Update student
@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    name: str,
    age: int,
    course: str,
    marks: float
):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    UPDATE students
    SET name = %s, age = %s, course = %s, marks = %s
    WHERE id = %s
    """

    cursor.execute(
        query,
        (name, age, course, marks, student_id)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return {"message": "Student updated successfully"}


# DELETE - Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = %s",
        (student_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return {"message": "Student deleted successfully"}
