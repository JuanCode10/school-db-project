from flask.views import MethodView
from flask_smorest import Blueprint, abort
#todo: create model for input validation
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

