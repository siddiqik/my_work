from flask import Flask, jsonify

app = Flask(__name__)

# some fake JSON data
students = [
    {"id": 1, "name": "Ava", "grade": 11},
    {"id": 2, "name": "Max", "grade": 12},
    {"id": 3, "name": "Zoe", "grade": 10}
]

@app.route("/")
def home():
    return "<h1>Welcome to the Student API</h1>"

@app.route("/students")
def get_students():
    return jsonify(students)

@app.route("/students/<int:student_id>")
def get_student(student_id):
    for s in students:
        if s["id"] == student_id:
            return jsonify(s)
    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
