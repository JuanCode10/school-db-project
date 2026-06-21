from marshmallow import Schema, fields

class PlainSchoolSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainStudentSchema(Schema):
    id = fields.Int(dump_only=True)
    last_name = fields.Str(required=True)
    first_name = fields.Str(required=True)
    enrolled = fields.Bool(required=True)

class SchoolSchema(PlainSchoolSchema):
    students = fields.List(fields.Nested(PlainStudentSchema()), dump_only=True)

class StudentSchema(PlainStudentSchema):
    school_id = fields.Int(load_only=True)
    school = fields.Nested(PlainSchoolSchema(), dump_only=True)

class NewStudentSchoolNameSchema(PlainStudentSchema):
    school_name = fields.Str(required=True, load_only=True)
