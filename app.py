from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for Contact Us form
@app.route('/')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Log form data to the console
    print(f"Name: {name}, Email: {email}, Message: {message}")
    
    return "Success! Your message has been sent."

# Simple API for Courses
courses = []

@app.route('/courses', methods=['POST'])
def add_course():
    new_course = request.json
    courses.append(new_course)
    return jsonify({"message": "Course added!"}), 201

@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses), 200

@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    updated_course = request.json
    courses[course_id] = updated_course
    return jsonify({"message": "Course updated!"}), 200

@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    courses.pop(course_id)
    return jsonify({"message": "Course deleted!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
