from sqlalchemy import func
from model import Student

from model import connect_to_db, db
from server import app

def load_students():
    """Adds first 3 students listed in each house on frodo to students"""

    print('Students')

    Student.query.delete()

    #I copied everyone's names in the order they appear on the houses page, so
    #order/inclusion/spelling is not personal :)
    aj = Student(fname='Avarna',
                        lname='Jain')

    db.session.add(aj)

    sn = Student(fname='Sharimen',
                    lname='Newaz')

    db.session.add(sn)

    mps = Student(fname='Melissa',
                    lname='Paredes-Scampini')

    db.session.add(mps)

    kb = Student(fname='Kristen',
                    lname='Beneduce')

    db.session.add(kb)

    bc = Student(fname='Bonnie',
                    lname='Chen')

    db.session.add(bc)

    jj = Student(fname='Jessica',
                    lname='Jenkins')

    db.session.add(jj)

    db.session.commit()




#calls functions to create and seed tables
if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    load_students()