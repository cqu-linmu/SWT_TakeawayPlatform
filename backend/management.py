from application import app,manager
from flask_script import Server


from api.finance.Finance import route_finance
from api.food.Food import route_food
from api.stat.Stat import  route_stat
from api.user.User import route_user
from api.upload.Upload import route_upload


# host需修改为服务器ip

'''
web管理后台接口
'''
manager.add_command( "runserver", Server( host='0.0.0.0',port=5111,use_debugger = True ,use_reloader = True) )
# 接口1：登录
app.register_blueprint( route_login,url_prefix = "/login" )
# 接口2：获取登录商家信息
app.register_blueprint( route_userInfo,url_prefix = "/userinfo" )
# 接口12：单品销售量统计
app.register_blueprint( route_dishSaleList,url_prefix = "/dish-Sale-list" )
# 接口3：餐品管理
app.register_blueprint( route_dishList,url_prefix = "/dish-list" )
# 接口4：获取餐品分类
app.register_blueprint( route_dishClassList,url_prefix = "/dish_class-list" )
# 接口5,6：餐品编辑，餐品删除
app.register_blueprint( route_dish,url_prefix = "/dish" ) # func: add(/add); delete(/)
# 接口7：订单管理
app.register_blueprint( route_orderList,url_prefix = "/order-list" )
# 接口8,9：订单编辑，订单删除
app.register_blueprint( route_order,url_prefix = "/order" ) # func: edit(/edit); delete(/)
# 接口11：每日流水
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