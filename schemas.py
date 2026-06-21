from marshmallow import Schema, fields

class PlainSchoolSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainStudentSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    status = fields.Str()

class SchoolSchema(PlainSchoolSchema):
    students = fields.List(fields.Nested(PlainStudentSchema()), dump_only=True)

class StudentSchema(PlainStudentSchema):
    school_id = fields.Int(load_only=True)
    school = fields.Nested(PlainSchoolSchema(), dump_only=True)
