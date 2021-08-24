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

route_dish = Blueprint('finance_page', __name__)


# 餐品删除接口
@route_dish.route("/", methods=["POST"])
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
