from os import getenv
from pymongo import MongoClient
from ..conection import db_mongo

client = MongoClient(db_mongo)
database = client[getenv("MONGO_DB_SCHEMA")]
collection = database["leads"]


class Leads:
    def save(data: object):
        try:
            return collection.insert_one(data)
        except Exception:
            return False

    def find_by_id(id: str):
        try:
            return collection.find_one({"id": id})
        except Exception:
            return False

    def find_by_email_and_phone(email: str, phone: str):
        try:
            return collection.find_one({"email": email, "phone": phone})
        except Exception:
            return False
        
    def find_by_external_user_id(external_user_id: str):
        try:
            return collection.find_one({"external_user_id": external_user_id})
        except Exception:
            return False
