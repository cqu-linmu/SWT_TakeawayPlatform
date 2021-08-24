# -*- coding: utf-8 -*-
from flask import Blueprint, request, g, jsonify, make_response, redirect
from common.libs.user.UserService import ( UserService )
from utils.UrlManager import (UrlManager)  # UrlManager：统一封装生成各种url的方法
from application import app, db
import json
from DataBaseFolder.Interface.UserBaseModify import *  # 导入数据库修改接口
import random

route_user = Blueprint('user_page', __name__)


# 用户登录
@route_user.route("/login", methods=["POST"])
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

    if user_info._Password != password:
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


# 登录用户的信息
@route_user.route("/userinfo", methods=["GET"])
def userinfo():
    resp = {'code': 200, 'message': '获取用户信息成功', 'data': {}}  # 返回信息
    if g.current_user:
        user_info = g.current_user
        resp['data'] = {'id': user_info.UserID, 'name': user_info.UserName, 'role': 'admin',
                        'avatar': "http://dummyimage.com/48x48/fb0a2a"}
        return jsonify(resp)
    resp['code'] = 400
    resp['message'] = "获取用户信息失败，请重新登录"
    return jsonify(resp)


# 退出登录
@route_user.route("/logout", methods=["GET", "POST"])
def logout():
    response = make_response(json.dumps(redirect(UrlManager.buildUrl("/user/login"))))  # 返回登录页面
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])  # 删除cookie
    return response
