# -*- coding: utf-8 -*-
from utils.MemberService import MemberService
from flask import Blueprint, request, jsonify
import DataBaseFolder.Interface.UserBaseModify as U

route_WXSearchAddress = Blueprint('WXSearchAddress', __name__)


@route_WXSearchAddress.route("/", methods=["POST", "GET"])
def searchAddress():
    """
    查询收货地址
    """
    resp = {'statusCode': 200, 'message': '操作成功', 'data': {}}
    req = eval(request.values['data'])
    print(req,type(req))
    user_id = int(req['user_id']) if 'user_id' in req else ' '  # 登录用户id

    # 查询用户信息
    member_info = U.PyFind_ID(user_id)
    member_address = member_info.Address.split("/")

    # 地址不存在
    judge = False  # 判断member_address是否为空，False为空，True为非空
    for item in member_address:
        if item != "":
            judge = True
            break
    if not judge:
        resp['statusCode'] = 400
        resp['message'] = "不存在地址"
        return jsonify(resp)
    resp['data'] = {
        'user_address': member_address[:-2]
    }
    return jsonify(resp)
