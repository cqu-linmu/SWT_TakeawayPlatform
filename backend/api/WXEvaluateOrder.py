# -*- coding: utf-8 -*-
from utils.MemberService import MemberService
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
    resp = {'code': 200, 'message': '操作成功~', 'data': {}}
    req = request.values

    # 解析请求参数
    order_id = int(req['order_id']) if 'order_id' in req else 0  # 菜品id
    score = float(req['score']) if 'score' in req else 0  # 点评分数
    # 拉取订单对象
    order = o.PyFind_OrderID(order_id)

    if not order:
        # 订单信息为空时拒绝评分请求
        resp['code'] = 400
        resp['message'] = '操作失败，请检查返回的订单ID -1'
        resp['data']['rate_status'] = 0
    elif order.OrderStatus != '待评价':
        # 订单状态不正确时拒绝评分请求
        resp['code'] = 400
        resp['message'] = '操作失败，请检查订单状态 -2'
        resp['data']['rate_status'] = 0
    else:
        dishList = order.Dishes.split("/")
        for dish in dishList[:-2]:
            # 解析这一订单中的菜品名称和数量
            dishPair = dish.split("|")
            dishID = dishPair[0]
            dishSold = int(dishPair[1])
            # 拉取菜品对象并更改评分
            dishObj = d.PyFind_ID(dishID)

            # print("___________")
            # print(dishID)
            # print(dishSold)
            # print(dishObj.DishName)
            # print("___________")

            dishObj.Score = ((dishObj.Sold - dishSold) * dishObj.Score + score) / dishSold
        # 状态更改为已完成
        order.OrderStatus = '已完成'
        resp['data']['rate_status'] = 1
    return jsonify(resp)
