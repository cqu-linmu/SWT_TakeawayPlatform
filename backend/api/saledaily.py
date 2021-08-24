from flask import Blueprint, request, jsonify, redirect
from utils.Helper import ops_render, getCurrentDate, iPagination, getDictFilterField
from application import app, db
from utils.UrlManager import UrlManager
from decimal import Decimal
from sqlalchemy import or_

route_saledaily = Blueprint('sale-daily', __name__)


@route_saledaily.route('/', methods=["GET", "POST"])
def saleDaily():
    resp = {'code': 200, 'message': '获取每日流水成功', 'data': {}}  # 提前定义返回信息
    stTime = request.values['order_time_st']

    return
