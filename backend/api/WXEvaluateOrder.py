# -*- coding: utf-8 -*-
from DataBaseFolder.Interface.InterfaceHelper import GenericModify
from flask import Blueprint, request, jsonify
import DataBaseFolder.Interface.OrderBaseModify as o
import DataBaseFolder.Interface.DishBaseModify as d

route_WXEvaluateOrder = Blueprint('WXEvaluateOrder', __name__)


@route_WXEvaluateOrder.route("/", methods=["GET", "POST"])
def EvaluateOrder():
    '''
    对订单下所有菜品进行评分
    :return:
    '''
    # 预定义回复结构
    resp = {'statusCode': 200, 'message': '操作成功~', 'data': {}}

    # 解析请求参数
    req = eval(request.values['data'])
    order_id = int(req['order_id']) if 'order_id' in req else 0  # 菜品id
    score = float(req['score']) if 'score' in req else 0  # 点评分数

    # 拉取订单对象
    order = o.PyFind_OrderID(order_id)

    # 分支处理是否应该接受评分请求
    if not order:
        # 订单信息为空时拒绝评分请求
        resp['statusCode'] = 400
        resp['message'] = '操作失败，请检查返回的订单ID -1'
        resp['data']['rate_status'] = 0
    elif order.OrderStatus != '待评价':
        # 订单状态不正确时拒绝评分请求
        resp['statusCode'] = 400
        resp['message'] = '操作失败，请检查订单状态 -2'
        resp['data']['rate_status'] = 0
    else:
        # 订单状态正确时，接受评价请求
        # 解析菜品数据并丢掉无效数据
        dishList = order.Dishes.split("/")
        while '' in dishList:
            dishList.remove('')

        # 对订单中所有的菜品执行评分操作
        for dish in dishList:
            # 解析这一订单中的菜品名称和数量
            dishPair = dish.split("|")
            dishID = int(dishPair[0])
            dishSold = int(dishPair[1])

            # 拉取菜品对象
            dishObj = d.PyFind_ID(dishID)

            # print("___________")
            # print(dishID)
            # print(dishSold)
            # print(dishObj.DishName)
            # print("___________")

            # 更改菜品评分
            new_Score = ((dishObj.Sold - dishSold) * dishObj.Score + score) / dishSold
            GenericModify(1, dishID, 'Dish', 'Score', str(new_Score))

        # 状态更改为已完成
        GenericModify(1, order.OrderID, 'Order', 'OrderStatus', '\'已完成\'')
        # 返回评分状态成功
        resp['data']['rate_status'] = 1
    return jsonify(resp)
