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


route_dishList = Blueprint('dish-list', __name__)

@route_dishList.route("/", methods=['GET'])
def index():
    
    req = request.values
    pageNum = int(req['page']) if ('page' in req and req['page']) else 1
    page_size = int(req['pageSize'])
    dishList = d.PyList()
    listNum = len(dishList)
    dishList = dishList[(pageNum - 1) * page_size:pageNum * page_size]
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