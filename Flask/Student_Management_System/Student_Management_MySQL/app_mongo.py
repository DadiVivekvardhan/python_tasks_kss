from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# =========================================================
# MONGODB ATLAS CONNECTION
# =========================================================

MONGO_URI = "mongodb+srv://vivekvardhandadi_db_user:Shankar2013@cluster0.xwc4uhe.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

# Database
db = client["student_flask_db"]

# Collection
students_collection = db["students"]


# =========================================================
# HOME PAGE - DISPLAY ALL STUDENTS
# =========================================================

@app.route("/")
def index():

    students = list(students_collection.find())

    return render_template(
        "index.html",
        students=students
    )


# =========================================================
# ADD STUDENT
# =========================================================

@app.route("/add", methods=["POST"])
def add_student():

    name = request.form.get("name")
    age = request.form.get("age")
    course = request.form.get("course")
    marks = request.form.get("marks")

    # Convert values to proper data types
    age = int(age)
    marks = float(marks)

    # Find the highest student ID
    last_student = students_collection.find_one(
        {},
        sort=[("id", -1)]
    )

    if last_student:
        student_id = last_student["id"] + 1
    else:
        student_id = 1

    # Student document
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    # Insert into MongoDB
    students_collection.insert_one(student)

    # Return to home page
    return redirect(url_for("index"))


# =========================================================
# EDIT STUDENT PAGE
# =========================================================

@app.route("/edit/<int:student_id>")
def edit_student(student_id):

    student = students_collection.find_one(
        {"id": student_id}
    )

    if student is None:
        return "Student not found", 404

    return render_template(
        "edit.html",
        student=student
    )


# =========================================================
# UPDATE STUDENT
# =========================================================

@app.route("/update/<int:student_id>", methods=["POST"])
def update_student(student_id):

    name = request.form.get("name")
    age = request.form.get("age")
    course = request.form.get("course")
    marks = request.form.get("marks")

    # Convert values
    age = int(age)
    marks = float(marks)

    # Update MongoDB document
    students_collection.update_one(
        {"id": student_id},
        {
            "$set": {
                "name": name,
                "age": age,
                "course": course,
                "marks": marks
            }
        }
    )

    return redirect(url_for("index"))


# =========================================================
# DELETE STUDENT
# =========================================================

@app.route("/delete/<int:student_id>")
def delete_student(student_id):

    students_collection.delete_one(
        {"id": student_id}
    )

    return redirect(url_for("index"))


# =========================================================
# TEST MONGODB CONNECTION
# =========================================================

@app.route("/test-mongodb")
def test_mongodb():

    try:
        # Test connection
        client.admin.command("ping")

        return """
        <h2>MongoDB Atlas Connection Successful!</h2>
        <p>Database: student_flask_db</p>
        <p>Collection: students</p>
        """

    except Exception as e:

        return f"""
        <h2>MongoDB Connection Failed</h2>
        <p>{e}</p>
        """


# =========================================================
# RUN FLASK APPLICATION
# =========================================================

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
