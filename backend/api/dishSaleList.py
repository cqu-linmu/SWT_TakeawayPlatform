from flask import Blueprint, request, jsonify, make_response, g, redirect
from DataBaseFolder.Models.RestaurantModels.DishBase import Dish
from utils.Helper import *
from application import app, db
import json

# 相关数据库调用
from DataBaseFolder.Interface import DishBaseModify as d

route_dishSaleList = Blueprint('dish-Sale-list', __name__)

@route_dishSaleList.route("/", methods=['GET', 'POST'])
def index():
    '''
    餐品销售情况列表接口
    '''
    req = request.values
    resp = {'code': 200, 'msg': '获取餐品列表成功', 'data': {}, 'total': 0}
    pageNum = int(req['pageNum']) if ('pageNum' in req and req['pageNum']) else 1
    page_size = int(req['pageSize']) if ('pageSize' in req and req['pageSize']) else 1
    dishList = d.PyList()
    totalList = len(dishList)
    if pageNum == -1:  # 当pageNum=-1时，返回所有订单
        dishList = dishList
    else: # 否则返回对应页面的订单
        dishList = dishList[(pageNum - 1) * page_size:pageNum * page_size]

    def bedict(a):
        lic = []
        for item in a:
            lic.append(
                {
                    "dish_id": item.DishID,
                    "dish_name": item.DishName,
                    "dish_price": item.Price,
                    "dish_number": item.Sold,
                    "dish_score": item.Score
                }
            )
        return lic

    resp['data'] = bedict(dishList)
    resp['total'] = totalList
    return jsonify(resp)
