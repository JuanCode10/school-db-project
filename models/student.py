from db import db

class StudentModel(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    last_name = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    enrolled = db.Column(db.Boolean(), nullable=False)
    
    # relationship with school: many-to-one
    school_id = db.Column(db.Integer, db.ForeignKey("schools.id"), unique=False, nullable=False)
    school = db.relationship("SchoolModel", back_populates="students")

    # todo: other entities to stablish relationships with
    # year
    # subjects