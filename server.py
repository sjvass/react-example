
"""Students server"""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, jsonify)

#from flask_debugtoolbar import DebugToolbarExtension

from model import Student, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
# app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_homepage():
    """render's html template for hompage"""

    return render_template('index.html')

@app.route('/students')
def student_list():
    """renders html template for list of students"""

    return render_template('student-list.html')

@app.route('/api/students')
def send_student_list():
    """returns a list of JSON objects with student info"""

    """When implementing React, the only way for the client (browser, html, 
    js, ect.) and server to communicate is be sending JSON objects back and 
    fourth. Anything you would have previously passed to Jinja using the session
    or template arguments now needs to be sent out as a JSON object in a route.
    Your jsx files will be able to access the information returned by that route
    by making a get request to the route"""

    #get all students
    students = Student.query.all()

    #create empty list to store student dictionaries
    response = []

    #create a dictionary for each student object so it can be converted to JSON
    for student in students:

        student_dict = {'student_id': student.student_id,
                        'fname': student.fname,
                        'lname': student.lname}

        response.append(student_dict)

    #convert list of python dicts to list of JSON objects
    return jsonify(response)


@app.route('/new-student', methods=['GET'])
def new_student_form():
    """renders html template form for creating a new student"""

    return render_template('new-student.html')

@app.route('/new-student', methods=['POST'])
def add_new_student():
    """uses posted information to add a new student to student"""

    #get posted information
    fname = request.json['fname']
    lname = request.json['lname']

    #add new student to students
    new_student = Student(fname=fname,
                            lname=lname)

    db.session.add(new_student)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be5000 True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')