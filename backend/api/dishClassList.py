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

route_dishClassList = Blueprint('dish_class-list', __name__)


@route_dishClassList.route('/', methods=['GET', 'POST'])
def return_classes():
    resp = {
        'code': 200,
        'message': '请求成功',
        'data': []
    }
    try:
        dishList = d.PyList()
        classList = []
        for item in dishList:
            if item.DishType not in classList:
                classList.append({
                    'class_name': item.DishType,
                    'class_value': item.DishType
                })
        resp['data'] = classList
    except:
        resp = {
            'code': 400,
            'message': '请求失败',
            'data': []
        }
    return jsonify(resp)
