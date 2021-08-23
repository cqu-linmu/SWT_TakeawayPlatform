from flask import Flask
import config.DataBaseConfig as DataBaseConfig
from DataBaseFolder.DataBase import db
import datetime

import DataBaseFolder.Interface.UserBaseModify as um
import DataBaseFolder.Interface.RestaurantBaseModify as rm
import DataBaseFolder.Interface.DishBaseModify as dm
import DataBaseFolder.Interface.OrderBaseModify as om
from DataBaseFolder.Interface.InterfaceHelper import GenericModify
from DataBaseFolder.Construct.ConstructHelper import *

#init
#Init application from DataBaseConfig by flask
app = Flask(__name__)
app.config.from_object(DataBaseConfig)
db.init_app(app)

#register
#register on json by blueprint, use url_prefix to define the type that called by url
#they are uesd in interfaces which contains functions without the prefix 'Py', and just for test and frontend call
'''
app.register_blueprint(um.user,url_prefix="/user")
app.register_blueprint(rm.restaurant,url_prefix="/restaurant")
app.register_blueprint(dm.dish,url_prefix="/dish")
app.register_blueprint(om.order,url_prefix='/order')
'''

#start
#called when open localhost if database use localhost as uri config
#do database base construct or other database init operations
#can remove if use database manager or .sql
@app.route('/')
def Start():
    '''
    db.drop_all()
    db.create_all()
    DataBaseConstruct_ALL()
    '''

    #om.PyFind_OrderTime(datetime.date.today())
    #GenericModify(1,1,'User','Telephone',123456)

    #Tp_DishList=dm.PyList()
    #print(Tp_DishList)

    return "hello"

#launch
#launch databse local debug
if __name__ == '__main__':
    #LocalDataBase

    app.run(debug=True)
