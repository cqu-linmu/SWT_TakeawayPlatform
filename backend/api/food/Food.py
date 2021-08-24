# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, redirect
from utils.Helper import ops_render, getCurrentDate, iPagination, getDictFilterField
from application import app, db
from utils.UrlManager import UrlManager
from decimal import Decimal
from sqlalchemy import or_
# 相关数据库调用
from DataBaseFolder.Interface import DishBaseModify as d
from DataBaseFolder.Interface import RestaurantBaseModify as r
from DataBaseFolder.Interface.InterfaceHelper import *

route_food = Blueprint('food_page', __name__)


# 餐品管理接口 [接口3]
@route_food.route("/index", methods=['POST'])
def index():
    req = request.values
    page = int(req['page']) if ('page' in req and req['page']) else 1
    page_size = int(req['pageSize'])
    dishList = d.PyList()
    listNum = len(dishList)
    pageNum = listNum / page_size
    dishList = dishList[(page - 1) * page_size:page * page_size]
    lic = []

    def bedict(dataList):
        for item in dataList:
            lic.append(
                {
                    "dish_id": item.DishID,
                    "dish_name": item.DishName,
                    "dish_class": item.DishType

                }
            )
        return lic

    return jsonify(bedict(dishList))


# 餐品编辑接口 [接口5]
@route_food.route("/set", methods=['POST'])
def set():
    resp = {'code': 1, 'msg': '编辑成功', 'data': {}}  # 提前定义返回信息
    req = request.values

    # 修改数据中菜品的信息
    dish_class = req['dish_class'] if 'dish_class' in req else ''  # 菜品分类
    dish_name = req['dish_name'] if 'dish_name' in req else ''  # 菜品名
    dish_price = req['dish_price'] if 'dish_price' in req else ''  # 菜品价格
    dish_description = req['dish_description'] if 'dish_description' in req else ''  # 菜品描述

    ## 检查菜品名是否合理【已请求过了分类，没有必要】
    #if dish_name is None or len(dish_name) < 1:
    #    resp['code'] = 0
    #    resp['msg'] = "请输入符合规范的名称~~"
    #    return jsonify(resp)

    # 检查菜品价格是否合理
    if not dish_price or len(dish_price) < 1:
        resp['code'] = 0
        resp['msg'] = "请输入符合规范的售卖价格~~"
        return jsonify(resp)

    price = Decimal(dish_price).quantize(Decimal('0.00'))
    if price <= 0:
        resp['code'] = 0
        resp['msg'] = "请输入符合规范的售卖价格~~"
        return jsonify(resp)

    # 检查菜品描述是否合理
    if dish_description is None or len(dish_description) < 3:
        resp['code'] = 0
        resp['msg'] = "请输入描述，并不能少于10个字符~~"
        return jsonify(resp)

    dish_info = d.PyFind_Name(dish_name)


    if not dish_info:
        r.PyAddDish(
            dishname=dish_name,
            price=dish_price,
            type=dish_class,
            description=dish_description
        )
    else:
        dish_id = dish_info.DishID
        GenericModify(3, dish_id, Dish, ['DishName', 'Price', 'DishType', 'Description'], ['\'dish_name\'', \
                                                                                           '\'dish_price\'',
                                                                                           '\'dish-class\'',
                                                                                           '\'dish_description\'', ])

    return jsonify(resp)


# 餐品删除接口
@route_food.route("/ops", methods=["POST"])
def ops():
    resp = {'code': 1, 'msg': '编辑成功', 'data': {}}
    req = request.values

    dish_class = req['dish_class'] if 'dish_class' in req else ''  # 菜品分类
    dish_name = req['dish_name'] if 'dish_name' in req else ''  # 菜品名
    dish_price = req['dish_price'] if 'dish_price' in req else ''  # 菜品价格
    dish_description = req['dish_description'] if 'dish_description' in req else ''  # 菜品描述
    dish_info = d.PyFind_Name(dish_name)
    dish_id = dish_info.DishID

    GenericModify(2, dish_id, Dish, 'dish_id')

    return jsonify(resp)
