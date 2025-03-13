from marshmallow import Schema, fields, ValidationError


class getUserByExternalUserIdInputSchema(Schema):
    external_user_id = fields.String(required=True)

    class Meta:
        ordered = True

class getUserByExternalUserIdInput:
    def create(body: getUserByExternalUserIdInputSchema):
        try:
            return getUserByExternalUserIdInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
