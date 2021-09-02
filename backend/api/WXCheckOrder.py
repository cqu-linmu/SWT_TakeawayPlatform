# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
import DataBaseFolder.Interface.OrderBaseModify as o
import DataBaseFolder.Interface.DishBaseModify as d

route_WXCheckOrder = Blueprint('WXCheckOrder', __name__)


@route_WXCheckOrder.route("/", methods=['GET', 'POST'])
def index():
    """
    查询各种状态订单接口
    """
    # 预定义回复结构
    resp = {'statusCode': 200, 'message': '获取订单列表成功', 'data': []}

    # 解析请求数据
    req = eval(request.values['data'])
    user_id = int(req['user_id']) if 'user_id' in req else ''
    status_req = req['status_req'] if 'status_req' in req else ''
    print(status_req)
    print(user_id)

    # 根据user_id查找对应订单，筛选出状态对应正确的订单
    userOrder = o.PyFind_UserID(user_id)
    orderList = []
    for order in userOrder:
        # 根据订单状态进行筛选，如果状态与请求的状态相对应，则将该订单加入候选订单列表
        if order.OrderStatus == status_req:
            orderList.append(order)
            print(order.Dishes)

    # 处理计算订单中所包含的信息：
    # 订单状态，订单id，订单时间，菜品信息，订单总价，订单地址
    for order in orderList:
        # 预定义单个订单的信息结构
        signalDishInfo = {"order_status": order.OrderStatus, "order_id": order.OrderID,
                          "order_time": order.OrderTime.strftime('%Y-%m-%d %H:%M:%S'),
                          "dish_data": [], "order_price": 0, "order_address": order.OrderAddress}
        # 解析菜品信息：菜品用/分割种类，|分割数量
        dishes = order.Dishes
        dishList = dishes.split('/')
        while '' in dishList:
            dishList.remove('')
        print(dishList)

        # 订单总价，随着菜品的遍历自增并在最后被赋值给order_price
        orderPrice = 0
        # 遍历菜品并填充dish_data的信息：菜品名称，菜品数量，菜品价格，菜品预览图
        for dish in dishList:
            # 解析菜品ID和菜品数量
            dishID = int(dish.split('|')[0])
            dishNum = int(dish.split('|')[1])
            print(dishID)
            print(dishNum)
            # 根据菜品名称取得菜品信息
            dishInfo = d.PyFind_ID(dishID)
            # 填充信息
            signalDishInfo['dish_data'].append(
                {
                    "dish_name": dishInfo.DishName,
                    "dish_num": dishNum,
                    "dish_price": dishInfo.Price,
                    "dish_img": dishInfo.Thumbnail
                }
            )
            # 订单总价自增
            orderPrice += dishNum * dishInfo.Price
        # 订单总价赋值
        signalDishInfo["order_price"] = orderPrice
        # 将这一个订单的信息加入回复体中
        resp['data'].append(signalDishInfo)

    return jsonify(resp)
