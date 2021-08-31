# -*- coding: utf-8 -*-
from utils.MemberService import MemberService
from flask import Blueprint, request, jsonify, g
import DataBaseFolder.Interface.UserBaseModify as U
from DataBaseFolder.Interface.InterfaceHelper import *
from application import app

route_WXRefreshAddress = Blueprint('WXRefreshAddress', __name__)


@route_WXRefreshAddress.route("/", methods=["GET", "POST"])
def refreshAddress():
    """
    添加/删除/修改收货地址
    request中传回的地址是
    :return:
    """
    resp = {'statusCode': 200, 'message': '修改地址成功', 'data': {}}
    req = request.values['data']
    new_address_lst = req['user_address_new'] if 'user_address_new' in req else ' '  # 新地址
    user_address_new = ''
    for address in new_address_lst:
        user_address_new += address + '/'

    user_id = req['user_id'] if 'user_id' in req else ' '  # 登录用户id

    # 获得用户信息
    member_info = U.PyFind_ID(user_id)
    user_id = member_info.UserID

    # 若新地址未输入,则意味着删除原地址
    if not user_address_new:
        GenericModify(1, user_id, 'User', 'Address', str('/'))
        resp['message'] = "删除地址成功"
        return jsonify(resp)

    # 获取原地址信息
    user_address = member_info.Address

    # 原地址不存在，则添加新地址
    if not user_address:
        GenericModify(1, user_id, 'User', 'Address', str(user_address_new))
        resp['statusCode'] = 200
        resp['message'] = "添加地址成功"
        return jsonify(resp)

    # 原地址存在，则修改未新输入的地址
    GenericModify(1, user_id, 'User', 'Address', str(user_address_new))

    return jsonify(resp)
