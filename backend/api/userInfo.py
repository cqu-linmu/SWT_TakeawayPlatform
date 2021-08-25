import json

from flask import Blueprint, request, jsonify, redirect, make_response
from utils.Helper import ops_render, getCurrentDate, iPagination, getDictFilterField
from application import app, db
from utils.UrlManager import UrlManager
from decimal import Decimal
from sqlalchemy import or_

from DataBaseFolder.Interface import RestaurantBaseModify as r

route_userInfo = Blueprint('userinfo', __name__)


@route_userInfo.route('/', methods=["GET"])
def userInfo():
    userItem = r.PyFind_ID(1)
    response = make_response(
        json.dumps({'code': 200,
                    'data': {
                        'id': 1,
                        'name': userItem.RestaurantName,
                        'role': 'visitor',
                        'avatar': userItem.HeadPortrait
                    }}))

    return response
