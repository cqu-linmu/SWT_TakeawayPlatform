from flask import Blueprint, request, jsonify, redirect
from DataBaseFolder.Models.OrderData.OrderBase import Order 
from DataBaseFolder.Interface import OrderBaseModify as o
from utils.Helper import *
from utils.UrlManager import UrlManager
from application import app, db
import json

route_finance = Blueprint('finance_page', __name__)


# 财务管理页面接口 [接口7]
@route_finance.route("/index", methods=['POST'])
def index():
    req = request.values
    page = int(req['page']) if ('page' in req and req['page']) else 1
    
    page_size = int(req['pageSize'])
    orderList =o.PyList()
    listNum=len(orderList)
    pageNum=listNum/page_size
    orderList=orderList[(page-1)*page_size:page*page_size]
    lic = []
    
    def bedict(a):
        for item in a:
            lic.append(
                {
                    "order_dish": item.Dishes,
                    "order_id": item.OrderID,
                    "order_price": item.Price,
                    "order_time": item.OrderTime,
                    "order_status": item.OrderStatus
                }
            )
        return lic
    
    # 不用返回总页数
    return jsonify(bedict(orderList))  
    

# 订单详情
@route_finance.route("/pay-info", methods=['POST'])
def info():
    resp_data = {}
    req = request.values
    id = int(req['id']) if 'id' in req else 0

    reback_url = UrlManager.buildUrl("/finance/index")
    query = Order.query

    if id < 1:
        return redirect(reback_url)

    pay_order_info = o.PyFind_OrderID(id)
    if not pay_order_info:
        return redirect(reback_url)

    resp_data["order_id"]=pay_order_info.OrderID
    resp_data["order_price"]=pay_order_info.Price
    resp_data["user_id"]=pay_order_info.UserID
    resp_data["order_address"]=pay_order_info.OrderAddress
    resp_data["order_time"]=pay_order_info. OrderTime
    
    
    return jsonify(resp_data)


# 订单编辑接口 [接口8]
@route_finance.route("/ops", methods=["POST"])
def orderOps():
    resp = {'code': 0, 'msg': '订单状态修改成功', 'data': {}}
    req = request.values
    order_id = req['order_id'] if 'order_id' in req else 0
    order_status = req['order_status'] if 'order_status' in req else 0
    act = req['act']

    pay_order_info = Order.query.filter_by(id=order_id).first()
    if not pay_order_info:
        resp['code'] = 1
        resp['msg'] = "订单状态修改失败，请联系用户支持"
        return jsonify(resp)

    if act == "express":
        pay_order_info.OrderStatus = "待收货"
        db.session.add(pay_order_info)
        db.session.commit()

    return jsonify(resp)
