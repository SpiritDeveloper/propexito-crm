from os import getenv
from pymongo import MongoClient
from dotenv import load_dotenv
import logging

load_dotenv()

db = "mongodb://{}:{}@{}:{}/".format(getenv("MONGO_DB_USER"), getenv("MONGO_DB_PASSWORD"), getenv("MONGO_DB_HOST"), getenv("MONGO_DB_PORT"))

client = MongoClient(db, authSource="admin")

try:
    client.logs.command(
        "createUser",
        getenv("MONGO_DB_USER"),
        pwd=getenv("MONGO_DB_PASSWORD"),
        roles=[{"role": "readWrite", "db": getenv("MONGO_DB_SCHEMA")}],
    )
except Exception as error:
    logging.warning(error)

logging.warning("DB Created correctly")
