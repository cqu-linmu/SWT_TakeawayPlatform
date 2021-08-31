from application import app, manager
from flask_script import Server

# web后台接口导入
# 登录与用户信息
from api.login import route_login
from api.userInfo import route_userInfo
# 菜品信息
from api.dishSaleList import route_dishSaleList
from api.dishList import route_dishList
from api.dishClassList import route_dishClassList
from api.dish import route_dish
# 订单信息
from api.orderList import route_orderList
from api.order import route_order
# 统计信息
from api.saledaily import route_saledaily

# 微信小程序接口导入
# 登录信息
from api.WXLogin import route_WXLogin
# 菜品信息
from api.WXDishList import route_WXDishList
from api.WXDishInfo import route_WXDishInfo
# 订单信息
from api.WXConfirmOrder import route_WXConfirmOrder
from api.WXEvaluateOrder import route_WXEvaluateOrder
from api.WXSubmitOrder import route_WXSubmitOrder
from api.WXCheckOrder import route_WXCheckOrder
from api.WXCancelOrder import route_WXCancelOrder
# 支付信息
from api.WXPay import route_WXPay
# 地址信息
from api.WXSearchAddress import route_WXSearchAddress
from api.WXRefreshAddress import route_WXRefreshAddress
from api.WXRecommend import route_WXRecommend

# host需修改为服务器ip
manager.add_command("runserver", Server(host='0.0.0.0', port=5111, use_debugger=True, use_reloader=True))

'''
web管理后台接口
'''
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

'''
微信小程序接口
'''
# 接口1：微信登录
app.register_blueprint(route_WXLogin, url_prefix="/api/WXLogin")
# 接口2：获取菜品列表
app.register_blueprint(route_WXDishList, url_prefix="/api/WXDishList")
# 接口3：获取菜品详情
app.register_blueprint(route_WXDishInfo, url_prefix="/api/WXDishInfo")
# 接口4：确认收货
app.register_blueprint(route_WXConfirmOrder, url_prefix="/api/WXConfirmOrder")
# 接口5：评价订单
app.register_blueprint(route_WXEvaluateOrder, url_prefix="/api/WXEvaluateOrder")
# 接口6：提交订单
app.register_blueprint(route_WXSubmitOrder, url_prefix="/api/WXSubmitOrder")
# 接口7：伪支付
app.register_blueprint(route_WXPay, url_prefix="/api/WXPay")
# 接口8：查询各种状态的订单
app.register_blueprint(route_WXCheckOrder, url_prefix="/api/WXCheckOrder")
# 接口9：取消订单
app.register_blueprint(route_WXCancelOrder, url_prefix="/api/WXCancelOrder")
# 接口10：查询收货地址
app.register_blueprint(route_WXSearchAddress, url_prefix="/api/WXSearchAddress")
# 接口11：更新收货地址
app.register_blueprint(route_WXRefreshAddress, url_prefix="/api/WXRefreshAddress")
# 接口12：获取推荐菜品
app.register_blueprint(route_WXRecommend, url_prefix="/api/WXRecommend")


def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc()
