# -*- coding: utf-8 -*-
from utils.MemberService import MemberService
from flask import Blueprint, request, jsonify
import DataBaseFolder.Interface.UserBaseModify as U

route_wxLogin = Blueprint('wx-login', __name__)


# 微信登录接口，包含用户创建功能
@route_wxLogin.route("/", methods=["GET", "POST"])
def login():
    resp = {'code': 200, 'message': '操作成功~', 'data': {}}

    req = request.values
    code = req['code'] if 'code' in req else ''

    if not code or len(code) < 1:
        resp['code'] = -1
        resp['message'] = "需要code -1"
        return jsonify(resp)

    openid = MemberService.getWeChatOpenId(code)
    if openid is None:
        resp['code'] = -1
        resp['message'] = "调用微信出错 -2"
        return jsonify(resp)

    # userInfo = U.PyFind_OpenID(openid)

    # 下面两个分支的成功情况都需要返回token和refresh_token，用MemberService.genAuthCode+id生成

    # if not userInfo:
    #   U.PyAdd(...)
    #   message="绑定现有账号成功"

    # else:
    #   检查传来的信息和找到的userinfo是否对应
    #   对应：返回登陆成功 ； 否则返回登陆失败
    return jsonify(resp)
