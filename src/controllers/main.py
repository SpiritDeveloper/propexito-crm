from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify
from ..dto.main_output_dto import responseSchema

main = Blueprint("Main", "main", url_prefix="/api", description="Main")


class Main(MethodView):
    @main.route("/", methods=["GET"])
    @main.response(200, responseSchema, content_type="application/json")
    def get():
        """Get status to server"""
        return jsonify(
            {
                "starting": "Running...",
                "name": "propexito-latam-cashier",
                "version": "V1.0.0",
            }
        )
