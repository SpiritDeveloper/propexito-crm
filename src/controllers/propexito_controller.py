from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify
from werkzeug.exceptions import BadRequest
from ..dto import (
    createUrlLatamcashierInput,
    createUrlLatamcashierInputSchema,
)
from ..service.propexito_service import PropexitoService

propexito = Blueprint("propexito", "propexito", url_prefix="/api/propexito", description="Propexito Services")

class PropexitoController(MethodView):
    @propexito.errorhandler(404)
    def resource_not_found(e):
        return (
            jsonify(code=404, status=False,  error=[str(e.description)]),
            404,
        )

    @propexito.errorhandler(BadRequest)
    def handle_bad_request(e):
        return (
            jsonify(code=402, message="Bad Input", error=str(e.exc), status=False),
            422,
        )
    
    propexito.register_error_handler(422, handle_bad_request)

    @propexito.route("/generate-url-latamcashier", methods=["GET"])
    @propexito.arguments(createUrlLatamcashierInputSchema, location="query")
    def post(body: createUrlLatamcashierInputSchema):
        """Generate Payment URL for Latamcashier"""
        request = createUrlLatamcashierInput.create(body)
        response = PropexitoService().generate_url_latamcashier(request)
        return response
    
    @propexito.route("/get-transactions", methods=["GET"])
    def get():
        """Get transactions"""
        response = PropexitoService().get_transactions()
        return response
    
