# -*- coding: utf-8 -*-
from utils.MemberService import MemberService
from flask import Blueprint, request, jsonify

import DataBaseFolder.Interface.RestaurantBaseModify as r
import DataBaseFolder.Interface.UserBaseModify as u
import DataBaseFolder.Interface.DishBaseModify as d

route_WXSubmitOrder = Blueprint('WXSubmitOrder', __name__)


def index():
    '''
    提交订单接口
    '''

    resp = {'code': 200, 'message': '获取订单列表成功', 'data': {}}
    req = request.values
    # 解析请求数据
    user_id = req['user_id'] if 'order_id' in req else ''
    # 根据id查找对应用户
    user = u.PyFind_ID(user_id)
    dishList = req['dish_data']
    dishes = ""
    price = 0
    for dish in dishList:
        dish_id = dish["dish_id"]
        num_dish = dish["num_dish"]
        # 根据id查找对应价格
        dishPrice = d.PyFind_ID(dish_id).Price
        # 累加菜品价格
        price += dishPrice*num_dish
        # 将所有菜品id和数量连接为一个字符串:  '|' 分割数量 '/' 分割不同菜品
        dishes = dishes + str(dish_id) + "|" + str(num_dish) + "/"

    remark = ""  # 默认无此值
    carriage = 0  # 默认无此值
    orderInfo = r.PyAddOrder(1, user_id, remark, user.Address, dishes, price, carriage)

    order_data = {
        "order_id": orderInfo.OrderID,
        "order_price": orderInfo.Price,
        "order_address": orderInfo.address,
        "order_time": orderInfo.OrderTime,
        "order_status": orderInfo.OrderStatus
    }

    resp['data'] = order_data
    return jsonify(resp)
