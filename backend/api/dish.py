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

route_dish = Blueprint('dish', __name__)


# 餐品删除接口
@route_dish.route("/", methods=["GET", "POST"])
def delDish():
    resp = {'code': 200, 'message': '删除成功', 'data': {}}
    req = request.values
    dish_id = req['dish_id'] if 'dish_id' in req else ''
    if not GenericModify(2, dish_id, 'Dish'):
        resp['code'] = 400
        resp['message'] = "删除失败"
        return jsonify(resp)

    app.logger.info(dish_id)
    return jsonify(resp)


# 添加餐品
@route_dish.route("/add", methods=["GET", "POST"])

def addDish():
    resp = {'code': 200, 'message': '添加菜品成功', 'data': {}}  # 提前定义返回信息
    req = request.values

    # 修改数据中菜品的信息
    dish_id = req['dish_id'] if 'dish_id' in req else ''  # 菜品编号
    dish_class = req['dish_class'] if 'dish_class' in req else ''  # 菜品分类
    dish_name = req['dish_name'] if 'dish_name' in req else ''  # 菜品名
    dish_price = req['dish_price'] if 'dish_price' in req else ''  # 菜品价格
    dish_description = req['dish_description'] if 'dish_description' in req else ''  # 菜品描述

    # 检查菜品名是否合理
    if dish_name is None or len(dish_name) < 1:
        resp['code'] = 400
        resp['message'] = "请输入符合规范的名称"
        return jsonify(resp)

    dish_info = d.PyFind_Name(dish_name)
    if dish_info:
        resp['code'] = 400
        resp['message'] = "已存在同名餐品"
        return jsonify(resp)

    # 检查菜品价格是否合理
    if not dish_price or len(dish_price) < 1:
        resp['code'] = 400
        resp['message'] = "请输入符合规范的售卖价格"
        return jsonify(resp)

    price = Decimal(dish_price).quantize(Decimal('0.00'))
    if price <= 0:
        resp['code'] = 400
        resp['message'] = "请输入符合规范的售卖价格"
        return jsonify(resp)

    # 检查菜品描述是否合理
    if dish_description is None or len(dish_description) < 3:
        resp['code'] = 400
        resp['message'] = "请输入描述，并不能少于10个字符"
        return jsonify(resp)

    if not dish_info:
        r.PyAddDish(
            resid=1,
            dishname=dish_name,
            price=dish_price,
            type=dish_class,
            description=dish_description
        )
    return jsonify(resp)


@route_dish.route("/edit", methods=["GET", "POST"])
def editDish():
    resp = {'code': 200, 'message': '修改菜品成功', 'data': {}}  # 提前定义返回信息
    req = request.values

    # 修改数据中菜品的信息
    dish_id = req['dish_id'] if 'dish_id' in req else ''  # 菜品编号 int
    dish_class = int(req['dish_class']) if 'dish_class' in req else ''  # 菜品分类 int
    dish_name = req['dish_name'] if 'dish_name' in req else ''  # 菜品名 str
    dish_price = int(req['dish_price']) if 'dish_price' in req else ''  # 菜品价格 float
    dish_description = req['dish_description'] if 'dish_description' in req else ''  # 菜品描述 str

    # 检查菜品名是否合理
    if dish_name is None or len(dish_name) < 1:
        resp['code'] = 400
        resp['message'] = "请输入符合规范的名称"
        return jsonify(resp)

    dish_info = d.PyFind_ID(dish_id)

    # 检查菜品价格是否合理
    if not dish_price:
        resp['code'] = 400
        resp['message'] = "请输入符合规范的售卖价格"
        return jsonify(resp)

    price = Decimal(dish_price).quantize(Decimal('0.00'))
    if price <= 0:
        resp['code'] = 400
        resp['message'] = "请输入符合规范的售卖价格"
        return jsonify(resp)

    # 检查菜品描述是否合理
    if dish_description is None or len(dish_description) < 3:
        resp['code'] = 400
        resp['message'] = "请输入描述，并不能少于10个字符"
        return jsonify(resp)
    if not GenericModify(3, dish_id, 'Dish',
                         ['DishName', 'Price', 'DishType', 'Description'],
                         [str(dish_name), str(dish_price), str(dish_class), str(dish_description)]):
        resp['code'] = 400
        resp['message'] = "编辑失败"
        return jsonify(resp)

    if not dish_info:
        r.PyAddDish(
            dishname=dish_name,
            price=dish_price,
            type=dish_class,
            description=dish_description
        )
    return jsonify(resp)
