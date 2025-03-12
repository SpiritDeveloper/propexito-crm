from marshmallow import Schema, fields, ValidationError
from marshmallow.validate import Length

class createUrlLatamcashierInputSchema(Schema):
    name = fields.String(required=True, validate=Length(min=3))
    firstname = fields.String(required=True, validate=Length(min=3))
    lastname = fields.String(required=True, validate=Length(min=3))
    email = fields.String(required=True)
    country = fields.String(required=True, validate=Length(min=2, max=2))
    phone = fields.String(required=True)
    country_phone_code = fields.String(required=True)
    amount = fields.Float(required=True)
    client_id = fields.String(required=True)

    class Meta:
        ordered = True

class createUrlLatamcashierInput:
    def create(body: createUrlLatamcashierInputSchema):
        try:
            return createUrlLatamcashierInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
