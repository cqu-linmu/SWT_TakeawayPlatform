# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
import DataBaseFolder.Interface.UserBaseModify as u

route_WXSearchAddress = Blueprint('WXSearchAddress', __name__)


@route_WXSearchAddress.route("/", methods=["POST", "GET"])
def searchAddress():
    """
    查询收货地址
    :return:
    """
    # 预定义回复结构
    resp = {'statusCode': 200, 'message': '操作成功', 'data': {}}

    # 解析请求参数
    req = eval(request.values['data'])
    user_id = int(req['user_id']) if 'user_id' in req else ' '  # 登录用户id

    # 查询用户信息
    member_info = u.PyFind_ID(user_id)
    member_address = member_info.Address.split("/")
    while '' in member_address:
        member_address.remove('')

    # 地址不存在
    if not len(member_address):
        resp['statusCode'] = 400
        resp['message'] = "不存在地址"
        return jsonify(resp)

    # 返回正确信息
    resp['data'] = {
        'user_address': member_address
    }
    return jsonify(resp)
