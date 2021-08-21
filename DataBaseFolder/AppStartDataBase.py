from flask import Flask
import DataBaseFolder.DataBaseConfig as DataBaseConfig

from DataBaseFolder.Interface.UserBaseModify import *
from DataBaseFolder.Interface.RestaurantBaseModify import *
from DataBaseFolder.Interface.DishBaseModify import *
from DataBaseFolder.Interface.OrderBaseModify import *
from DataBaseFolder.Interface.InterfaceHelper import GenericModify
from DataBaseFolder.Construct.ConstructHelper import *

app = Flask(__name__)
app.config.from_object(DataBaseConfig)
db.init_app(app)

app.register_blueprint(user,url_prefix="/user")
app.register_blueprint(restaurant,url_prefix="/restaurant")
app.register_blueprint(dish,url_prefix="/dish")
app.register_blueprint(order,url_prefix='/order')

@app.route('/')
def Start():
    '''
    db.drop_all()
    db.create_all()
    DataBaseConstruct_ALL()
    '''

    GenericModify(1,1,'User','Telephone',123456)

    return "hello"

if __name__ == '__main__':
    #LocalDataBase

    app.run(debug=True)
