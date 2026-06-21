from db import db

class SchoolModel(db.Model):

    __tablename__ = "schools"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    # Student realtionship: one-to-many
    students = db.relationship("StudentModel", back_populates="school", cascade="all, delete")