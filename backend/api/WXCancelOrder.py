# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
from DataBaseFolder.Interface import OrderBaseModify as o
from DataBaseFolder.Interface.InterfaceHelper import GenericModify

route_WXCancelOrder = Blueprint('WXCancelOrder', __name__)


@route_WXCancelOrder.route("/", methods=['GET', 'POST'])
def index():
    """
    取消订单接口
    """
    # 预定义回复结构
    resp = {'statusCode': 200, 'message': '取消成功', 'data': {}}

    # 解析请求数据
    req = eval(request.values['data'])
    order_id = req['order_id'] if 'order_id' in req else ''

    # 根据id查找对应订单
    curOrder = o.PyFind_OrderID(order_id)

    # 修改订单状态
    if curOrder.OrderStatus == '已取消':
        resp['statusCode'] = 400
        resp['message'] = '取消失败：不能重复取消订单 -1'
    else:
        GenericModify(1, curOrder.OrderID, 'Order', 'OrderStatus', '\'已取消\'')

    return jsonify(resp)
