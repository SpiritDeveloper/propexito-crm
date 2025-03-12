# Import controllers
from .controllers import main, propexito
import coloredlogs, logging
from dotenv import load_dotenv
from flask import Flask
from flask_smorest import Api
from flask_cors import CORS

# load configuration .env
load_dotenv()

# configuration
class Config:
    TESTING = False
    JSON_SORT_KEYS = False
    API_VERSION = 0.1
    API_TITLE = "Proexito Documentation"
    OPENAPI_VERSION = "3.0.0"  # Cambié la versión aquí a una válida
    OPENAPI_URL_PREFIX = "/api"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    )
    OPENAPI_SWAGGER_UI_PATH = "/documentation"
    OPENAPI_SWAGGER_UI_URL = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"
    API_SPEC_OPTIONS = {
        "info": {"description": "Proexito Documentation"}
    }
    SECRET_KEY = "secret"


# Flask start
app = Flask(__name__)
app.debug = True

# Add configuration
app.config.from_object(Config)


# register cors
api = Api(app)
CORS(
    app,
    resources={
        r"/*": {
            "origins": "*",
            "allow_headers": "*",
            "expose_headers": "*"
        }
    },
)
  
# register modules
api.register_blueprint(main)
api.register_blueprint(propexito)

logging.basicConfig(format="%(asctime)s %(message)s")
coloredlogs.install(level="WARNING", logger=logging.getLogger(), isatty=True)
coloredlogs.install(level="INFO", logger=logging.getLogger(), isatty=True)
