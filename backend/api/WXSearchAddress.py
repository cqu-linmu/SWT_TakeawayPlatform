# -*- coding: utf-8 -*-
from utils.MemberService import MemberService
from flask import Blueprint, request, jsonify
import DataBaseFolder.Interface.UserBaseModify as U

route_WXSearchAddress = Blueprint('WXSearchAddress', __name__)


@route_WXSearchAddress.route("/", methods=["POST", "GET"])
def searchAddress():
    """
    查询收获地址
    """
    resp = {'code': 200, 'message': '操作成功', 'data': {}}
    req = request.values
    user_id = req['user_id'] if 'user_id' in req else ' '  # 登录用户id

    # 查询用户信息
    member_info = U.PyFind_ID(user_id)
    member_address = member_info.Address

    # 地址不存在
    if not member_address:
        resp['code'] = 400
        resp['message'] = "不存在地址"
        return jsonify(resp)
    resp['data'] = {
        'user_address': member_address
    }
    return jsonify(resp)