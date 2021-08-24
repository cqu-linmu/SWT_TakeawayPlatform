
from flask import Blueprint, request, jsonify, redirect
from DataBaseFolder.Models.OrderData.OrderBase import Order 
from DataBaseFolder.Interface import OrderBaseModify as o
from utils.Helper import *
from utils.UrlManager import UrlManager
from application import app, db
import json
route_order = Blueprint('route_order', __name__)


# 订单编辑接口 [接口8]
@route_order.route("/", methods=["POST"])
def orderOps():
    resp = {'code': 0, 'msg': '订单状态修改成功', 'data': {}}
    req = request.values
    order_id = req['order_id'] if 'order_id' in req else 0
    order_status = req['order_status'] if 'order_status' in req else 0
   

    pay_order_info = Order.query.filter_by(id=order_id).first()
    if not pay_order_info:
        resp['code'] = 1
        resp['msg'] = "订单状态修改失败，请联系用户支持"
        return jsonify(resp)

    pay_order_info.OrderStatus = order_status
    db.session.add(pay_order_info)
    db.session.commit()

    return jsonify(resp)
