from flask import Flask
import DataBaseConfig

from Interface.UserBaseModify import *
from Interface.RestaurantBaseModify import *
from Interface.DishBaseModify import *

app = Flask(__name__)
app.config.from_object(DataBaseConfig)
db.init_app(app)

app.register_blueprint(user,url_prefix="/user")
app.register_blueprint(restaurant,url_prefix="/restaurant")
app.register_blueprint(dish,url_prefix="/dish")

@app.route('/')
def Start():
    db.create_all()
    return "hello"

if __name__ == '__main__':
    #LocalDataBase

    app.run(debug=True)