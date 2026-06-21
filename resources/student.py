from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import StudentModel, SchoolModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from schemas import PlainStudentSchema, StudentSchema, NewStudentSchoolNameSchema

blp = Blueprint("student", __name__, description="Operations on students.")

@blp.route("/student")
class StudentOperations(MethodView):

    @blp.response(200, StudentSchema(many=True))
    def get(self):
        """Get all students."""
        return StudentModel.query.all()
    
    @blp.arguments(NewStudentSchoolNameSchema)
    @blp.response(201, StudentSchema)
    def post(self, student_data):
        """Create a student in a specific school."""
        school = SchoolModel.query.filter_by(name=student_data.pop("school_name")).first_or_404()
        student = StudentModel(**student_data, school_id=school.id)

        try:
            db.session.add(student)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error ocurred while inserting the item.")
        
        return student
    
@blp.route("/student/<int:student_id>")
class SpecificStudentOperations(MethodView):
    
    @blp.response(200, StudentSchema)
    def get(self, student_id):
        """Get specific student with student id."""
        student = StudentModel.query.get_or_404(student_id)
        return student
    
    def delete(self, student_id):
        """Delete a specific student with id."""
        student = StudentModel.query.get_or_404(student_id)
        deleted_student = {
                    "id": student.id, 
                    "name": f"{student.last_name}, {student.first_name}"
                    }
        db.session.delete(student)
        db.session.commit()
        return {
            "message": "Student deleted successfully",
            "deleted_student": deleted_student
                }