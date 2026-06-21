from flask.views import MethodView
from flask_smorest import Blueprint, abort
# from models import StudentModel #todo: implement model
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
# from schemas import #todo: implement schemas

blp = Blueprint("student", __name__, description="Operations on students.")

#todo: add endpoints