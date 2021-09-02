# -*- coding: utf-8 -*-
from utils.MemberService import MemberService
from flask import Blueprint, request, jsonify
import DataBaseFolder.Interface.OrderBaseModify as o
import DataBaseFolder.Interface.DishBaseModify as d

route_WXCheckOrder = Blueprint('WXCheckOrder', __name__)


@route_WXCheckOrder.route("/", methods=['GET', 'POST'])
def index():
    '''
    查询各种状态订单接口
    '''
    resp = {'statusCode': 200, 'message': '获取订单列表成功', 'data': []}
    req = eval(request.values['data'])
    user_id = req['user_id'] if 'user_id' in req else ''
    status_req = req['status_req'] if 'status_req' in req else ''
    print(status_req)
    print(user_id)
    # 根据user_id查找对应订单
    userOrder = o.PyFind_UserID(user_id)

    orderList = []
    for order in userOrder:
        # 根据订单状态进行筛选
        if order.OrderStatus == status_req:
            orderList.append(order)
    for order in orderList:
        signalDishInfo = {"order_status": order.OrderStatus, "order_id": order.OrderID,
                          "order_time": order.OrderTime.strftime('%Y-%m-%d %H:%M:%S'),
                          "dish_data": [], "order_price": 0, "order_address": order.OrderAddress}
        dishes = order.Dishes
        dishList = dishes.split('/')
        for dish in dishList[:-2]:
            # 用 | 分割菜品数量
            dishID = int(dish.split('|')[0])
            dishNum = int(dish.split('|')[1])
            # 根据菜品名称取得菜品信息
            dishInfo = d.PyFind_ID(dishID)
            signalDishInfo['dish_data'].append(
                {
                    "dish_name": dishInfo.DishName,
                    "dish_num": dishNum,
                    "dish_price": dishInfo.Price,
                    "dish_img": dishInfo.Thumbnail
                }
            )
        resp['data'].append(signalDishInfo)
    return jsonify(resp)
