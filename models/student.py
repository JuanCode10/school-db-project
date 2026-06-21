from db import db

class StudentModel(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(), nullable=False)
    
    # relationship with school: many-to-one
    school_id = db.Column(db.Integer, db.ForeignKey("schools.id"), unique=False, nullable=False)
    school = db.relationship("SchoolModel", back_populates="students")

    # todo:other entities to stablish relationships with
    # year
    # subjects_enrolled