from application import app,manager
from flask_script import Server


from api.finance.Finance import route_finance
from api.food.Food import route_food
from api.stat.Stat import  route_stat
from api.user.User import route_user
from api.upload.Upload import route_upload


#host需修改为服务器ip
manager.add_command( "runserver", Server( host='0.0.0.0',port=5111,use_debugger = True ,use_reloader = True) )

app.register_blueprint( route_userInfo,url_prefix = "/userinfo" )

app.register_blueprint( route_dishSaleList,url_prefix = "/dish-Sale-list" )
app.register_blueprint( route_dishList,url_prefix = "/dish-list" )
app.register_blueprint( route_dishClassList,url_prefix = "/dish_class-list" )
app.register_blueprint( route_dish,url_prefix = "/dish" ) # func: add(/add); delete(/)

app.register_blueprint( route_orderList,url_prefix = "/order-list" )
# to fix
app.register_blueprint( route_order,url_prefix = "/order" ) # func: edit(); delete(/)

app.register_blueprint( route_saledaily,url_prefix = "/sale-daily" )

def main():
    manager.run( )

if __name__ == '__main__':
    try:
        import sys
        sys.exit( main() )
    except Exception as e:
        import traceback
        traceback.print_exc()