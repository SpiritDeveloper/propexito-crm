from marshmallow import Schema, fields, ValidationError
from marshmallow.validate import Length


class getTransactionByTransactionIdInputSchema(Schema):
    transaction_id = fields.String(required=True, validate=Length(min=3))

    class Meta:
        ordered = True


class getTransactionByTransactionIdInput:
    def create(body: getTransactionByTransactionIdInputSchema):
        try:
            return getTransactionByTransactionIdInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
