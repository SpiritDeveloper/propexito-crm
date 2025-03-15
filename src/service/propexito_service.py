from ..dto import createUrlLatamcashierInput, getUserByExternalUserIdInput
import requests
from ..model.leads import Leads
from os import getenv
from dotenv import load_dotenv
import logging

load_dotenv()


class PropexitoService:
    def __init__(self):
        LATAMCASHIER = getenv("LATAMCASHIER")
        PAGE = getenv("PAGE")
        CONFIGURATION_MICROSERVICE = getenv("CONFIGURATION_MICROSERVICE")
        self.latamcashier = LATAMCASHIER
        self.page = PAGE
        self.configuration_microservice = CONFIGURATION_MICROSERVICE

    def generate_url_latamcashier(self, request: createUrlLatamcashierInput):
        logging.info("Generando URL para Latamcashier")
        logging.info(
            f"Register lead {request['name']} {request['firstname']} {request['lastname']}"
        )

        lead = Leads.find_by_email_and_phone(request["email"], request["phone"])

        if not lead:
            lead = Leads.save(request)

            if not lead:
                logging.error("Error al registrar el lead")
                return {"success": False, "message": "Error al registrar el lead"}

        logging.info(f"Lead registrado {lead}")

        response = {}
        response["success"] = True
        response["message"] = "Lead registrado correctamente"
        response["url"] = (
            f"{self.latamcashier}/payment?user={str(request['external_user_id'])}&page={self.page}&order={request['transaction_id']}&amount={request['amount']}"
        )

        return response

    def get_transactions_by_transaction_id(self, transaction_id: str):
        logging.info("Obteniendo transacciones")

        response = {}
        response["success"] = True
        response["message"] = "Transacciones obtenidas correctamente"
        response["transaction"] = {}

        import requests

        url = f"{self.configuration_microservice}/transactions/review/status/reference_transaction"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        data = {
            "reference_id": transaction_id
        }

        try:
            response_api = requests.post(url, headers=headers, json=data)
            response["transaction"] = response_api.json()
        except Exception as e:
            logging.error(f"Error al obtener transacciones: {str(e)}")
            response["success"] = False
            response["message"] = "Error al obtener transacciones"

        return response

    def get_user_by_id(self, request: getUserByExternalUserIdInput):
        logging.info("Obteniendo usuario por ID")

        user = Leads.find_by_external_user_id(request["external_user_id"])

        if not user:
            logging.error("Usuario no encontrado")
            return {"success": False, "message": "Usuario no encontrado", "user": {}}
        
        user["id"] = str(user["_id"])
        del user["_id"]

        response = {}
        response["success"] = True
        response["message"] = "Usuario obtenido correctamente"
        response["user"] = user

        return response
