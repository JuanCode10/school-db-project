from marshmallow import Schema, fields

class PlainSchoolSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)