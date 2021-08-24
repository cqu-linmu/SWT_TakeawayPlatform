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

route_dishClassList= Blueprint('dishClassList', __name__)
# 展示分类信息
@route_dishClassList.route("/", methods=["GET"])
def getClass():
    resp = {'code': 200, 'message': '获取餐品分类列表成功', 'data': []}
    resp['data'].append({'className': '主食', 'class_value': '主食'})
    resp['data'].append({'className': '小吃', 'class_value': '小吃'})
    resp['data'].append({'className': '饮品', 'class_value': '饮品'})

    return jsonify(resp)
