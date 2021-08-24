from application import app, manager
from flask_script import Server

from api.login import route_login
from api.userInfo import route_userInfo
from api.dishSaleList import route_dishSaleList
from api.dishList import route_dishList
from api.dishClassList import route_dishClassList
from api.dish import route_dish
from api.orderList import route_orderList
from api.order import route_order
from api.saledaily import route_saledaily

# host需修改为服务器ip

'''
web管理后台接口
'''
manager.add_command("runserver", Server(host='0.0.0.0', port=5111, use_debugger=True, use_reloader=True))
# 接口1：登录
app.register_blueprint(route_login, url_prefix="/api/login")
# 接口2：获取登录商家信息
app.register_blueprint(route_userInfo, url_prefix="/api/userinfo")
# 接口12：单品销售量统计
app.register_blueprint(route_dishSaleList, url_prefix="/api/dish-Sale-list")
# 接口3：餐品管理
app.register_blueprint(route_dishList, url_prefix="/api/dish-list")
# 接口4：获取餐品分类
app.register_blueprint(route_dishClassList, url_prefix="/api/dish_class-list")
# 接口5,6：餐品编辑，餐品删除
app.register_blueprint(route_dish, url_prefix="/api/dish")  # func: add(/add); delete(/)
# 接口7：订单管理
app.register_blueprint(route_orderList, url_prefix="/api/order-list")
# 接口8,9：订单编辑，订单删除
app.register_blueprint(route_order, url_prefix="/api/order")  # func: edit(/edit); delete(/)
# 接口11：每日流水
app.register_blueprint(route_saledaily, url_prefix="/api/sale-daily")


def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc()
