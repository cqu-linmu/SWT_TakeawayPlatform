from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Blueprint, request, jsonify
DEBUG = True
app = Flask(__name__)
#*****为数据库密码
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:*****@127.0.0.1/test_db?charset=utf8mb4'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
db = SQLAlchemy(app)
manager = Manager(app)
route_index = Blueprint( 'index_page',__name__ )
@route_index.route("/")
def index():
    return "SWT"

app.register_blueprint(route_index, url_prefix="/")