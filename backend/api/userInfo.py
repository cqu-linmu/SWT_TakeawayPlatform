from flask import Blueprint, request, jsonify, redirect
from utils.Helper import ops_render, getCurrentDate, iPagination, getDictFilterField
from application import app, db
from utils.UrlManager import UrlManager
from decimal import Decimal
from sqlalchemy import or_

from DataBaseFolder.Interface import RestaurantBaseModify as r

route_userInfo = Blueprint('userinfo', __name__)


@route_userInfo.route('/', methods=["GET", "POST"])
def userInfo():
    userItem = r.PyFind_ID(1)
    resp = {'code': 200, 'message': '获取用户信息成功', 'data': {
        'id': 1,
        'name': userItem.RestaurantName,
        'role': 'admin',
        'avatar': userItem.HeadPortrait
    }}  # 提前定义返回信息
    return jsonify(resp)
