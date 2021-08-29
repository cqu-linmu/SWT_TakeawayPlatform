# -*- coding: utf-8 -*-
from utils.MemberService import MemberService
from flask import Blueprint, request, jsonify
import DataBaseFolder.Interface.OrderBaseModify as o

route_WXEvaluateOrder = Blueprint('WXEvaluateOrder', __name__)


@route_WXEvaluateOrder.route("/", methods=["GET", "POST"])
def EvaluateOrder():
    '''

    :return:
    '''
    resp = {'code': 200, 'message': '操作成功~', 'data': {}}
    req = request.values

    order_id = int(req['order_id']) if 'order_id' in req else 0  # 菜品id
    score = int(req['score']) if 'score' in req else 0  # 点评分数

    order = o.PyFind_OrderID(order_id)
    if not order:
        resp['code'] = 400
        resp['message'] = '操作失败，请检查返回的订单ID'
        resp['data']['rate_status'] = 0
    else:
        resp['data']['rate_status'] = 1
        order.Remark = score

    return jsonify(resp)
