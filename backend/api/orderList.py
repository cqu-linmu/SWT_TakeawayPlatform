from flask import Blueprint, request, jsonify, redirect
from DataBaseFolder.Models.OrderData.OrderBase import Order
from DataBaseFolder.Interface import OrderBaseModify as o
from utils.Helper import *
from utils.UrlManager import UrlManager
from application import app, db
import json

route_orderList = Blueprint('order-list', __name__)


# 订单详情页面接口 [接口7] 
@route_orderList.route("/", methods=['POST', 'GET'])
def index():
    # 获取请求结果
    req = request.values

    # 解析参数
    pageNum = int(req['pageNum']) if ('pageNum' in req and req['pageNum']) else 1
    pageSize = int(req['pageSize'])

    # 查询数据库订单数据
    orderList = o.PyList()

    # 计算分页情况
    listNum = len(orderList)
    orderList = orderList[(pageNum - 1) * pageSize:pageNum * pageSize]
    lic = []

    # 数据为空时查询失败
    if listNum < 1 or pageNum > listNum:
        lic = {
            'code': 400,
            'message': '请求失败,检查当前页数或者联系后台检查数据库',
            'data': []
        }
        return jsonify(lic)

    # 数据有效时，创建响应体
    lic = {
        'code': 200,
        'message': '请求成功',
        'data': [],
        'total': listNum
    }

    # 加入菜品数据
    def bedict(dataList):
        for item in dataList:
            lic['data'].append(
                {
                    "order_dish": item.Dishes,
                    "order_id": item.OrderID,
                    "order_price": item.Price,
                    "order_time": item.OrderTime,
                    "order_status": item.OrderStatus
                }
            )
        return lic

    return jsonify(bedict(orderList))
