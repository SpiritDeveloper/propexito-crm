from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify
from werkzeug.exceptions import BadRequest
from ..dto import (
    createUrlLatamcashierInput,
    createUrlLatamcashierInputSchema,
    getUserByExternalUserIdInput,
    getUserByExternalUserIdInputSchema,
    getTransactionByTransactionIdInput,
    getTransactionByTransactionIdInputSchema,
)
from ..service.propexito_service import PropexitoService

propexito = Blueprint(
    "propexito",
    "propexito",
    url_prefix="/api/propexito",
    description="Propexito Services",
)


class PropexitoController(MethodView):
    @propexito.errorhandler(404)
    def resource_not_found(e):
        return (
            jsonify(code=404, status=False, error=[str(e.description)]),
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

    @propexito.route("/get-transactions-by-transaction-id", methods=["GET"])
    @propexito.arguments(getTransactionByTransactionIdInputSchema, location="query")
    def get_transactions_by_transaction_id(body: getTransactionByTransactionIdInputSchema):
        """Get transactions by transaction id"""
        request = getTransactionByTransactionIdInput.create(body)
        response = PropexitoService().get_transactions_by_transaction_id(request)
        return response
    
    @propexito.route("/get-user-by-id", methods=["GET"], doc=False)
    @propexito.arguments(getUserByExternalUserIdInputSchema, location="query")
    def get_user_by_id(body: getUserByExternalUserIdInputSchema):
        """Get user by id"""
        request = getUserByExternalUserIdInput.create(body)
        response = PropexitoService().get_user_by_id(request)
        return response
