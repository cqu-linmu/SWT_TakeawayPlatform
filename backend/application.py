from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Blueprint, request, jsonify
from config import BaseConfig

# start debug mode
DEBUG = True

# config application
app = Flask(__name__)
app.config.from_object(BaseConfig)

CORS(app, resources={r'/*': {'origins': '*', 'supports_credentials': True, 'Access-Control-Allow-Origin': '*'}})

db = SQLAlchemy(app)
manager = Manager(app)

route_index = Blueprint('api', __name__)


@route_index.route("/")
def index():
    return "SWT"


app.register_blueprint(route_index, url_prefix="/")
