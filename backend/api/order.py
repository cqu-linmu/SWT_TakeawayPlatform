from flask import Blueprint, request, jsonify, redirect
from DataBaseFolder.Models.OrderData.OrderBase import Order
from DataBaseFolder.Interface import OrderBaseModify as o
from utils.Helper import *
from utils.UrlManager import UrlManager
from application import app, db
import json

# 相关数据库调用
from DataBaseFolder.Interface import InterfaceHelper as interfecehelper

route_order = Blueprint('order', __name__)

@route_order.route("/edit", methods=["GET", "POST"])
def edit():
    '''
    订单编辑接口
    '''
    resp = {'code': 200, 'message': '订单状态修改成功', 'data': {}}
    req = request.values
    order_id = req['order_id'] if 'order_id' in req else 0
    order_status = req['order_status'] if 'order_status' in req else 0

    pay_order_info = o.PyFind_OrderID(order_id)

    if not pay_order_info:
        resp['code'] = 1
        resp['message'] = "订单状态修改失败，请联系用户支持"
        return jsonify(resp)

    pay_order_info.OrderStatus = order_status
    db.session.add(pay_order_info)
    db.session.commit()

    return jsonify(resp)


# 订单删除接口

@route_order.route("/", methods=["GET", "POST"])
def delete():
    resp = {'code': 200, 'msg': '删除成功', 'data': {}}
    req = request.values
    order_id = req['order_id'] if 'order_id' in req else 0

    if not interfecehelper.GenericModify(2, order_id, "Order"):
        resp['code'] = 400
        resp['msg'] = '删除失败'

    return jsonify(resp)
