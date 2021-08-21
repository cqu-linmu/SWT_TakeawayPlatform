from flask import Blueprint, request, jsonify, make_response, g, redirect
from Models.OrderData.OrderBase import Order
from common.libs.Helper import *
from common.libs.UrlManager import UrlManager
import json
from application import app, db

route_finance = Blueprint('finance_page', __name__)


# 财务管理页面
@route_finance.route("/index")
def index():
    resp_data = {}
    req = request.values
    page = int(req['page']) if ('page' in req and req['page']) else 1
    token = req['token']
    page_size = req['pageSize']
    token_check(token)

    query = Order.query
    page_params = {
        'total': query.count(),
        'page_size': page_size,
        'page': page,
        'display': app.config['PAGE_DISPLAY'],
        'url': request.full_path.replace("&p={}".format(page), "")
    }
    # 分页操作
    pages = iPagination(page_params)
    offset = (page - 1) * pageSize
    pay_list = query.order_by(Order.id.desc()).offset(offset).limit(pageSize).all()
    data_list = []

    for item in pay_list:
        tmp_data = {
            "order_id": item.OrderID,
            "order_status": item.OrderStatus,
            "order_price": item.Price,
            "order_dish": item.Disehes
        }
        data_list.append(tmp_data)

    resp_data['list'] = data_list
    resp_data['pages'] = pages
    resp_data['search_con'] = req
    resp_data['pay_status_mapping'] = app.config['PAY_STATUS_MAPPING']
    resp_data['current'] = 'index'

    return ops_render("finance/index.html", resp_data)


# 订单详情
@route_finance.route("/pay-info")
def info():
    resp_data = {}
    req = request.values
    id = int(req['id']) if 'id' in req else 0
    token = req['token']
    token_check(token)

    reback_url = UrlManager.buildUrl("/finance/index")
    query = Order.query

    if id < 1:
        return redirect(reback_url)

    pay_order_info = query.filter_by(id=id).first()
    if not pay_order_info:
        return redirect(reback_url)

    address_info = {}
    if pay_order_info.OrderAddress:
        address_info = json.loads(pay_order_info.OrderAddress)

    resp_data['pay_order_info'] = pay_order_info
    resp_data['address_info'] = address_info
    resp_data['current'] = 'index'
    return ops_render("finance/pay_info.html", resp_data)


# 点击确认发货按钮，将订单状态改为“待收货”
@route_finance.route("/ops", methods=["POST"])
def orderOps():
    resp = {'code': 0, 'msg': '发货成功', 'data': {}}
    req = request.values
    id = req['id'] if 'id' in req else 0
    act = req['act'] if 'act' in req else ''
    token = req['token']
    token_check(token)

    pay_order_info = Order.query.filter_by(id=id).first()
    if not pay_order_info:
        resp['code'] = 1
        resp['msg'] = "发货失败，请联系用户支持"
        return jsonify(resp)

    if act == "express":
        pay_order_info.OrderStatus = "待收货"
        db.session.add(pay_order_info)
        db.session.commit()

    return jsonify(resp)
