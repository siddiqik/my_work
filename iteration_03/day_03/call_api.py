from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Alice", "age": 17},
    {"id": 2, "name": "Bob", "age": 18},
    {"id": 3, "name": "Charlie", "age": 16}
]

@app.route("/")
def home():
    return "<h1>Welcome to the Student API!</h1>"

@app.route("/students")
def get_students():
    return jsonify(students)

@app.route("/students/<int:student_id>")
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)


