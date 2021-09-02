# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
from DataBaseFolder.Interface import OrderBaseModify as o
from DataBaseFolder.Interface import UserBaseModify as u
from DataBaseFolder.Interface.InterfaceHelper import GenericModify

route_WXPay = Blueprint('WXPay', __name__)


@route_WXPay.route("/", methods=['GET', 'POST'])
def index():
    """
    付款接口
    :return:
    """
    # 预定义回复结构
    resp = {'statusCode': 200, 'message': "支付成功", 'pay_status': 1}

    # 解析请求参数
    req = eval(request.values['data'])
    order_id = req['order_id'] if 'order_id' in req else ''
    money_amount = float(req['money_amount'])

    # 查找id对应订单
    order = o.PyFind_OrderID(order_id)
    print("订单总额: " + str(order.Price))
    print("订单ID：" + str(order.OrderID))

    # 查找该订单对应用户
    user_id = order.UserID
    print("当前订单对应用户的ID: " + str(user_id))

    # 根据用户id查找用户相关信息
    user = u.PyFind_ID(user_id)
    print("当前订单对应的用户：" + user.UserName)

    # 当订单状态正确 且 用户支付成功 时，返回支付成功的信息
    if order.OrderStatus == '待付款' and user.Consumption(money_amount) :
        resp['message'] = "支付成功"
        resp['statusCode'] = 200
        GenericModify(1, order.OrderID, 'Order', 'OrderStatus', '\'待收货\'')
        print("--------付款成功--------")
    else:
        resp['message'] = "支付失败！请检查订单状态 -1"
        resp['statusCode'] = 400
        print("--------付款失败--------")

    return jsonify(resp)
