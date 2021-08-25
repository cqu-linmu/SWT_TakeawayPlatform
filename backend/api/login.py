# -*- coding: utf-8 -*-
import random
import json
from flask import Blueprint, request, jsonify, make_response, g, redirect
from utils.user.UserService import (UserService)  # UserService：封装用户登录相关的方法
from application import app, db

from DataBaseFolder.Interface.UserBaseModify import *  # 导入数据库修改接口

route_login = Blueprint('login', __name__)


# 用户登录接口  [接口1]
@route_login.route("", methods=["GET", "POST"])
def login():
    # 当请求为POST
    resp = {'code': 200, 'message': '登录成功', 'data': {}}  # 返回信息

    tst = request.data.decode('utf-8')

    tstSplit = tst.split(',')
    userName = (tstSplit[0].split(':')[1]).replace('"', '')  # string
    password = (tstSplit[1].split(':')[1]).replace('"', '').strip('}')  # string

    user_info = PyFind_Name(userName)  # 从数据库寻找登录名相同的帐号

    if not user_info:
        resp['code'] = 400
        resp['message'] = "用户名或密码错误 -1"
        return jsonify(resp)

    if not user_info.CheckPassword(password):
        resp['code'] = 400
        resp['message'] = "用户名或密码错误-2"
        return jsonify(resp)

    token = random.randint(1, 99999)
    refresh_token = str(token + 1)
    user_info.Token = str(token)

    response = make_response(
        json.dumps({'code': 200,
                    'data': {'token': str(token), 'refresh_token': refresh_token},
                    'message': '登录成功'}))  # 返回登录成功的信息
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
        UserService.geneAuthCode(user_info), user_info.UserID), 60 * 60 * 24 * 120)  # 保存120天
    return response
