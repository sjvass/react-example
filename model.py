"""Models and database functions for react example"""

#import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

#connection to PostgreSQL database
db = SQLAlchemy()


"""class that will represent a table that stores information about hackbright
    students"""
class Student(db.Model):
    """Images related to lost and found items"""

    __tablename__ = "students"

    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    house = db.Column(db.String(100), nullable=False)
    advisor = db.Column(db.String(100), nullable=False)

    def __repr__(self): 
        """ Provide helpful representation when printed """

        return f"""<Student student_id={self.student_id},
                    fname={self.fname},
                    lname={self.lname},
                    house={self.house},
                    advisor={self.advisor}>"""

    def to_dict(self):
        """Creates dictionary representation of Student instance"""

        student_dict = {'student_id': self.student_id,
                        'fname': self.fname,
                        'lname': self.lname,
                        'house': self.house,
                        'advisor': self.advisor}

        return student_dict






##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    # database must be called students
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///students'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")