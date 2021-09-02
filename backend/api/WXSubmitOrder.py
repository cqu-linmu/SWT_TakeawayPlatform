# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify

import DataBaseFolder.Interface.RestaurantBaseModify as r
import DataBaseFolder.Interface.UserBaseModify as u
import DataBaseFolder.Interface.DishBaseModify as d

route_WXSubmitOrder = Blueprint('WXSubmitOrder', __name__)


@route_WXSubmitOrder.route('/', methods=['GET', 'POST'])
def index():
    """
    提交订单接口
    :return:
    """
    # 预定义回复结构
    resp = {'statusCode': 200, 'message': '提交订单成功', 'data': {}}

    # 解析请求数据
    req = eval(request.values['data'])
    user_id = int(req['user_id']) if 'user_id' in req else ''

    # 根据id查找对应用户
    user = u.PyFind_ID(user_id)
    dishList = req['dish_data']
    dishAddress = user.Address.split("/")[0]
    print("dishList：" + str(dishList))
    print("dishAddress:", dishAddress)

    # 遍历处理订单信息：菜品id|菜品数量，总价格
    dishes = ""
    price = 0
    for dish in dishList:
        dish_id = int(dish["dish_id"])
        num_dish = dish["dish_num"]
        # 根据id查找对应价格
        dishPrice = d.PyFind_ID(dish_id).Price
        # 累加菜品价格
        price += dishPrice * num_dish
        # 将所有菜品id和数量连接为一个字符串:  '|' 分割数量 '/' 分割不同菜品
        dishes = dishes + str(dish_id) + "|" + str(num_dish) + "/"

    # 添加订单到数据库中
    remark = '无'  # 默认没有要求
    carriage = 0  # 默认未发货
    orderInfo = r.PyAddOrder(1, user_id, remark, dishAddress, dishes, price, carriage)

    # 返回订单信息：订单id，订单总价，订单地址，订单创建时间，订单状态
    order_data = {
        "order_id": orderInfo.OrderID,
        "order_price": orderInfo.Price,
        "order_address": orderInfo.OrderAddress,
        "order_time": orderInfo.OrderTime,
        "order_status": orderInfo.OrderStatus
    }
    resp['data'] = order_data

    return jsonify(resp)
