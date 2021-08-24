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


route_dishList = Blueprint('dishList', __name__)

@route_dishList.route("/index", methods=['GET'])
def index():
     resp = {'code': 200, 'message': '获取餐品列表成功', 'data': [], 'total': 0}  # 提前定义返回信息
      req = request.values
      if req:
          pageNum = int(req['pageNum']) if ('page' in req and req['page']) else 1
          pageSize = int(req['pageSize'])
          dishList = d.PyList()
          listNum = len(dishList)
          pages = listNum / pageSize
          dishList = dishList[(pageNum - 1) * pageSize:pageNum * pageSize]
          resp['total'] = int(listNum / 3)
          for item in dishList:
              resp['data'].append(
                  {
                      "dish_id": item.DishID,
                      "dish_name": item.DishName,
                      "dish_class": item.DishType

                  }
              )
          return jsonify(resp)
