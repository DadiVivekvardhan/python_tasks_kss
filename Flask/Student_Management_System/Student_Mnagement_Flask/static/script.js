const API_URL = "http://127.0.0.1:5002/api/students";

let allStudents = [];


// ===============================
// Load Students
// ===============================

async function loadStudents() {

    try {

        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Failed to load students");
        }

        allStudents = await response.json();

        displayStudents(allStudents);

    } catch (error) {

        console.error("Error:", error);

        alert("Unable to connect to the Flask server.");
    }
}


// ===============================
// Display Students
// ===============================

function displayStudents(students) {

    const tableBody = document.getElementById("student-table-body");
    const emptyMessage = document.getElementById("empty-message");

    tableBody.innerHTML = "";

    if (students.length === 0) {

        emptyMessage.style.display = "block";

        return;
    }

    emptyMessage.style.display = "none";


    students.forEach(student => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.email}</td>
            <td>${student.phone}</td>
            <td>${student.course}</td>
            <td>${student.department}</td>
            <td>${student.year}</td>

            <td>

                <button
                    class="action-button edit-button"
                    onclick="editStudent(${student.id})">
                    Edit
                </button>

                <button
                    class="action-button delete-button"
                    onclick="deleteStudent(${student.id})">
                    Delete
                </button>

            </td>
        `;

        tableBody.appendChild(row);

    });
}


// ===============================
// Add Student
// ===============================

document.getElementById("student-form").addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        const studentId =
            document.getElementById("student-id").value;


        const studentData = {

            name: document.getElementById("name").value.trim(),

            email: document.getElementById("email").value.trim(),

            phone: document.getElementById("phone").value.trim(),

            course: document.getElementById("course").value,

            department: document.getElementById("department").value,

            year: document.getElementById("year").value

        };


        try {

            let response;


            // ===============================
            // Update Student
            // ===============================

            if (studentId) {

                response = await fetch(
                    `${API_URL}/${studentId}`,
                    {
                        method: "PUT",

                        headers: {
                            "Content-Type": "application/json"
                        },

                        body: JSON.stringify(studentData)
                    }
                );

            }


            // ===============================
            // Create Student
            // ===============================

            else {

                response = await fetch(
                    API_URL,
                    {
                        method: "POST",

                        headers: {
                            "Content-Type": "application/json"
                        },

                        body: JSON.stringify(studentData)
                    }
                );

            }


            const result = await response.json();


            if (!response.ok) {

                alert(result.error || "Something went wrong");

                return;
            }


            alert(
                studentId
                    ? "Student updated successfully!"
                    : "Student added successfully!"
            );


            resetForm();

            loadStudents();

        } catch (error) {

            console.error("Error:", error);

            alert("Unable to connect to the Flask server.");
        }

    }
);


// ===============================
// Edit Student
// ===============================

function editStudent(id) {

    const student = allStudents.find(
        student => student.id === id
    );


    if (!student) {
        return;
    }


    document.getElementById("student-id").value =
        student.id;

    document.getElementById("name").value =
        student.name;

    document.getElementById("email").value =
        student.email;

    document.getElementById("phone").value =
        student.phone;

    document.getElementById("course").value =
        student.course;

    document.getElementById("department").value =
        student.department;

    document.getElementById("year").value =
        student.year;


    document.getElementById("form-title").textContent =
        "Edit Student";

    document.getElementById("submit-button").textContent =
        "Update Student";

    document.getElementById("cancel-button").style.display =
        "inline-block";


    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

}


// ===============================
// Delete Student
// ===============================

async function deleteStudent(id) {

    const confirmed = confirm(
        "Are you sure you want to delete this student?"
    );


    if (!confirmed) {
        return;
    }


    try {

        const response = await fetch(
            `${API_URL}/${id}`,
            {
                method: "DELETE"
            }
        );


        const result = await response.json();


        if (!response.ok) {

            alert(result.error || "Unable to delete student");

            return;
        }


        alert("Student deleted successfully!");

        loadStudents();


    } catch (error) {

        console.error("Error:", error);

        alert("Unable to connect to the Flask server.");
    }

}


// ===============================
// Search Students
// ===============================

function searchStudents() {

    const searchText =
        document.getElementById("search").value
        .toLowerCase()
        .trim();


    const filteredStudents =
        allStudents.filter(student =>

            student.name.toLowerCase().includes(searchText) ||

            student.email.toLowerCase().includes(searchText) ||

            student.phone.toLowerCase().includes(searchText) ||

            student.course.toLowerCase().includes(searchText) ||

            student.department.toLowerCase().includes(searchText)

        );


    displayStudents(filteredStudents);
}


// ===============================
// Cancel Edit
// ===============================

function cancelEdit() {

    resetForm();

}


// ===============================
// Reset Form
// ===============================

function resetForm() {

    document.getElementById("student-form").reset();

    document.getElementById("student-id").value = "";

    document.getElementById("form-title").textContent =
        "Add New Student";

    document.getElementById("submit-button").textContent =
        "Add Student";

    document.getElementById("cancel-button").style.display =
        "none";

}


// ===============================
// Start Application
// ===============================

document.addEventListener(
    "DOMContentLoaded",
    function() {

        document.getElementById("cancel-button").style.display =
            "none";

        loadStudents();

    }
);
