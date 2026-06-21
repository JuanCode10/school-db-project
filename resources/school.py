from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import SchoolModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from schemas import PlainSchoolSchema, SchoolSchema

blp = Blueprint("school", __name__, description="Operations on schools.")

@blp.route("/school")
class School(MethodView):

    @blp.response(200, SchoolSchema(many=True))
    def get(self):
        """Get all schools."""
        return SchoolModel.query.all()
    
    @blp.arguments(SchoolSchema)
    @blp.response(201, SchoolSchema)
    def post(self, school_data):
        """Crete a store."""
        school = SchoolModel(**school_data)
        try:
            db.session.add(school)
            db.session.commit()
        except IntegrityError:
            abort(400, message=f"School name \'{school.name}\' already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return school
    
@blp.route("/school/<int:school_id>")
class SpecificSchool(MethodView):

    @blp.response(200, SchoolSchema)
    def get(self, school_id):
        """Get school with specific id."""
        school = SchoolModel.query.get_or_404(school_id)
        return school
    
    # no response decoration
    def delete(self, school_id):
        """Delete school with specific id."""
        school = SchoolModel.query.get_or_404(school_id)
        deleted_school = {"id": school.id, "name": school.name}
        db.session.delete(school)
        db.session.commit()
        return {
            "message": "School deleted successfully.",
            "deleted_school": deleted_school,
        }