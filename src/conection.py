from os import getenv
from dotenv import load_dotenv

load_dotenv()

db_mongo = "mongodb://{}:{}@{}:{}/{}".format(
    getenv("MONGO_DB_USER"), getenv("MONGO_DB_PASSWORD"), getenv("MONGO_DB_HOST"), getenv("MONGO_DB_PORT"), getenv("MONGO_DB_SCHEMA")
)