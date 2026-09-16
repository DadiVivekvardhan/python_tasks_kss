from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# In-memory storage for students
students = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "9876543210",
        "course": "B.Tech",
        "department": "Computer Science",
        "year": "3rd Year"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "phone": "9876543211",
        "course": "B.Sc",
        "department": "Information Technology",
        "year": "2nd Year"
    }
]
current_id = 3


@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify(students)


@app.route("/api/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)
    return jsonify({"error": "Student not found"}), 404


@app.route("/api/students", methods=["POST"])
def add_student():
    global current_id
    data = request.get_json()

    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email are required"}), 400

    student = {
        "id": current_id,
        "name": data.get("name", "").strip(),
        "email": data.get("email", "").strip(),
        "phone": data.get("phone", "").strip(),
        "course": data.get("course", "").strip(),
        "department": data.get("department", "").strip(),
        "year": data.get("year", "").strip()
    }

    students.append(student)
    current_id += 1

    return jsonify(student), 201


@app.route("/api/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    for student in students:
        if student["id"] == student_id:
            if "name" in data:
                student["name"] = data["name"].strip()
            if "email" in data:
                student["email"] = data["email"].strip()
            if "phone" in data:
                student["phone"] = data["phone"].strip()
            if "course" in data:
                student["course"] = data["course"].strip()
            if "department" in data:
                student["department"] = data["department"].strip()
            if "year" in data:
                student["year"] = data["year"].strip()
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


@app.route("/api/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    global students
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return jsonify({"message": "Student deleted successfully"})

    return jsonify({"error": "Student not found"}), 404


if __name__ == "__main__":
    port = int(os.environ.get("API_PORT", 5002))
    app.run(host="127.0.0.1", port=port, debug=True)

