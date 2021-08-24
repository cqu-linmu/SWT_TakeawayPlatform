# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, make_response, g, redirect
from utils.user.UserService import (UserService)  # UserService：封装用户登录相关的方法
from utils.Helper import (ops_render)  # ops_render:渲染页面
from utils.UrlManager import (UrlManager)  # UrlManager：统一封装生成各种url的方法
from application import app, db
import json
from DataBaseFolder.Interface.UserBaseModify import *  # 导入数据库修改接口

route_login = Blueprint('login', __name__)


# 用户登录接口  [接口1]
@route_login.route("/login", methods=["GET", "POST"])
def login():

   # 当请求为POST
    resp = {'code': 200, 'message': '登录成功', 'data': {}}  # 返回信息

    req = request.values  # 前端传来的信息

    # 接口中使用的变量
    userName = req['userName'] if 'userName' in req else ''
    password = req['password'] if 'password' in req else ''

    user_info = PyFind_Name(userName)  # 从数据库寻找登录名相同的帐号
    if not user_info:
        resp['code'] = 400
        resp['message'] = "用户名或密码错误-1"
        return jsonify(resp)

    if not user_info.CheckPassword(password):
        resp['code'] = 400
        resp['message'] = "用户名或密码错误-2"
        return jsonify(resp)

    token = random.randint(1, 99999)
    refresh_token = token + 1
    user_info.Token = token

    response = make_response(
        json.dumps({'code': 200, 'msg': '登录成功', 'data': {'token': token, 'refresh_token': refresh_token}}))  # 返回登录成功的信息
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
        UserService.geneAuthCode(user_info), user_info.UserID), 60 * 60 * 24 * 120)  # 保存120天
    return response
