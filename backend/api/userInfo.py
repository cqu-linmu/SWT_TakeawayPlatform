import json
from flask import Blueprint, make_response
# 相关数据库调用
from DataBaseFolder.Interface import RestaurantBaseModify as r

route_userInfo = Blueprint('userinfo', __name__)


@route_userInfo.route('/', methods=["GET"])
def userInfo():
    '''
    用户信息接口
    '''
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
