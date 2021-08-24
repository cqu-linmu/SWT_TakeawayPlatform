from flask import Blueprint, request, jsonify, redirect
from DataBaseFolder.Models.OrderData.OrderBase import Order
from DataBaseFolder.Interface import OrderBaseModify as o
from utils.Helper import *
from utils.UrlManager import UrlManager
from application import app, db
import json

route_orderList = Blueprint('orderList', __name__)


# 订单管理页面接口 [接口7]
@route_orderList.route("/", methods=['GET'])
def index():
    resp = {'code': 200, 'msg': '获取订单列表成功', 'data': {}, 'total': 0}
    req = request.values
    pageNum = int(req['pageNum']) if ('pageNum' in req and req['pageNum']) else 1  # 当前页数
    page_size = int(req['pageSize'])  # 页面订单条数

    orderList = o.PyList()
    totalList = len(orderList)  # 订单总条数
    if pageNum == -1:  # 当pageNum=-1时，返回所有订单
        orderList = orderList
    else:
        orderList = orderList[(pageNum - 1) * page_size:pageNum * page_size]
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

    resp['data'] = bedict(orderList)
    resp['total'] = totalList
    return jsonify(resp)