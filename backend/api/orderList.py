from flask import Blueprint, request, jsonify, redirect
from DataBaseFolder.Models.OrderData.OrderBase import Order 
from DataBaseFolder.Interface import OrderBaseModify as o
from utils.Helper import *
from utils.UrlManager import UrlManager
from application import app, db
import json

route_orderList= Blueprint('order-list', __name__)


# 订单详情页面接口 [接口7]
@route_orderList.route("/", methods=['POST'])
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