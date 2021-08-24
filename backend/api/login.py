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
    resp = {'code': 1, 'msg': '登录成功', 'data': {}}  # 返回信息
    req = request.values  # 前端传来的信息

    # 接口中使用的变量
    login_name = req['userName'] if 'userName' in req else ''
    login_pwd = req['password'] if 'password' in req else ''

    # 用户登录验证
    if login_name is None or len(login_name) < 1:  # 用户名未输入或太短
        resp['code'] = 0
        resp['msg'] = "用户名或密码错误"
        return jsonify(resp)

    if login_pwd is None or len(login_pwd) < 1:  # 密码未输入或太短
        resp['code'] = 0
        resp['msg'] = "用户名或密码错误"
        return jsonify(resp)

    user_info = PyFind_Name(login_name)  # 从数据库寻找登录名相同的帐号
    if not user_info:
        resp['code'] = 0
        resp['msg'] = "用户名或密码错误"
        return jsonify(resp)

    if user_info._Password != login_pwd:
        resp['code'] = 0
        resp['msg'] = "用户名或密码错误"
        return jsonify(resp)

    # uid：用户对应的编号
    response = make_response(json.dumps({'code': 1, 'msg': '登录成功'}))  # 返回登录成功的信息
    # 生成cookie
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
        UserService.geneAuthCode(user_info), user_info.UserID), 60 * 60 * 24 * 120)  # 保存120天
    return response
