from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


# =========================
# MySQL Database Connection
# =========================

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="student_user",
        password="student123",
        database="student_management"
    )


# =========================
# Home Page - Get Students
# =========================

@app.route('/')
def index():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students_api")
    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", students=students)


# =========================
# Add Student
# =========================

@app.route('/add', methods=['POST'])
def add_student():

    name = request.form['name']
    age = request.form['age']
    course = request.form['course']
    marks = request.form['marks']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students_api (name, age, course, marks)
        VALUES (%s, %s, %s, %s)
        """,
        (name, age, course, marks)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect('/')


# =========================
# Delete Student
# =========================

@app.route('/delete/<int:student_id>')
def delete_student(student_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students_api WHERE id = %s",
        (student_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect('/')


# =========================
# Edit Student - Show Form
# =========================

@app.route('/edit/<int:student_id>')
def edit_student(student_id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM students_api WHERE id = %s",
        (student_id,)
    )

    student = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template("edit.html", student=student)


# =========================
# Update Student
# =========================

@app.route('/update/<int:student_id>', methods=['POST'])
def update_student(student_id):

    name = request.form['name']
    age = request.form['age']
    course = request.form['course']
    marks = request.form['marks']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE students_api
        SET name = %s,
            age = %s,
            course = %s,
            marks = %s
        WHERE id = %s
        """,
        (name, age, course, marks, student_id)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect('/')


# =========================
# Run Flask Application
# =========================

if __name__ == '__main__':
    app.run(port=5000, debug=True)
