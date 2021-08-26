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
    '''
    菜品分类信息接口
    '''
    resp = {
        'code': 200,
        'message': '请求成功',
        'data': []
    }
    dishList = d.PyList()
    classList = []
    for item in dishList:
        classList.append(item.DishType)
    classList = list(set(classList))

    for dishClass in classList:
        resp['data'].append({
            'class_name': dishClass,
            'class_value': dishClass
        })
    return jsonify(resp)
