# -*- coding: utf-8 -*-
from utils.MemberService import MemberService
from flask import Blueprint, request, jsonify
from DataBaseFolder.Interface import OrderBaseModify as o
from DataBaseFolder.Interface import UserBaseModify as u
from DataBaseFolder.Interface.InterfaceHelper import GenericModify

route_WXPay = Blueprint('WXPay', __name__)


@route_WXPay.route("/", methods=['GET', 'POST'])
def index():
    '''
    付款页面接口
    '''
    resp = {'statusCode': 200, 'message': "支付成功", 'pay_status': 1}
    req = request.values['data']
    order_id = req['order_id'] if 'order_id' in req else ''
    money_amount = float(req['money_amount'])

    # 查找id对应订单
    order = o.PyFind_OrderID(order_id)
    print("订单总额: " + str(order.Price))
    # 查找该订单对应用户
    user_id = order.UserID
    print("当前订单对应用户的ID: " + str(user_id))
    # 根据用户id查找用户相关信息
    user = u.PyFind_ID(user_id)
    print("当前订单对应的用户："+user.UserName)
    # 调用user自动扣费函数
    if user.Consumption(money_amount) and order.OrderStatus == '待付款':
        resp['message'] = "支付成功"
        resp['statusCode'] = 200
        # todo: 泛型
        # order.OrderStatus='待发货'
        GenericModify(1,order.OrderID,'Order','OrderStatus','待发货')
    else:
        resp['message'] = "支付失败！请检查订单状态 -1"
        resp['statusCode'] = 400

    return jsonify(resp)
