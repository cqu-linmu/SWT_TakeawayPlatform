# -*- coding: utf-8 -*-
from flask import request
import DataBaseFolder.Interface.UserBaseModify as u
from DataBaseFolder.Interface.InterfaceHelper import *

route_WXRefreshAddress = Blueprint('WXRefreshAddress', __name__)


# todo：地址默认选取第一个地址；更新地址时前端会传回一个以/分割的字符串，直接对其重新赋值即可
@route_WXRefreshAddress.route("/", methods=["GET", "POST"])
def refreshAddress():
    """
    添加/删除/修改收货地址
    :return:
    """
    # 预定义回复结构
    resp = {'statusCode': 200, 'message': '修改地址成功', 'data': {}}

    # 解析请求参数
    req = eval(request.values['data'])
    new_address_lst = req['user_address_new'] if 'user_address_new' in req else ' '  # 新地址
    user_id = int(req['user_id']) if 'user_id' in req else ' '  # 登录用户id
    print(new_address_lst)
    print(user_id)

    # 从前端传回的地址列表中生成新的地址字符串，以/分割不同地址
    user_address_new = ''
    for address in new_address_lst:
        user_address_new += address + '/'
    print("user_address_new:",user_address_new)
    # # 获得用户信息
    # member_info = u.PyFind_ID(user_id)

    # # 若新地址未输入,则意味着删除原地址
    # if not user_address_new:
    #     GenericModify(1, user_id, 'User', 'Address', str('/'))
    #     resp['message'] = "删除地址成功"
    #     return jsonify(resp)
    #
    # # 获取原地址信息
    # user_address = member_info.Address
    #
    # # 原地址不存在，则添加新地址
    # if not user_address:
    #     GenericModify(1, user_id, 'User', 'Address', str(user_address_new))
    #     resp['statusCode'] = 200
    #     resp['message'] = "添加地址成功"
    #     return jsonify(resp)

    # 修改新输入的地址
    GenericModify(1, user_id, 'User', 'Address', '\''+str(user_address_new)+'\'')
    print("修改后的用户地址：", u.PyFind_ID(user_id).Address)

    return jsonify(resp)
