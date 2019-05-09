
"""Students server"""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                    session, jsonify)

#from flask_debugtoolbar import DebugToolbarExtension

from model import Student, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

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

@app.route('/students/<student_id>')
def student_page(student_id):
    """renders html template for student with specified id"""

    return render_template('student-page.html')

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

    print(students)

    #create empty list to store student dictionaries
    response = []

    #create a dictionary for each student object so it can be converted to JSON
    for student in students:
        #print(student.to_dict())

        response.append(student.to_dict())

    #convert list of python dicts to list of JSON objects
    return jsonify(response)

#@app.route('/new-student')


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