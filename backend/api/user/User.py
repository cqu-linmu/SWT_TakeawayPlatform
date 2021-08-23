# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, make_response, g, redirect
from utils.user.UserService import (UserService)  # UserService：封装用户登录相关的方法
from utils.Helper import (ops_render)  # ops_render:渲染页面
from utils.UrlManager import (UrlManager)  # UrlManager：统一封装生成各种url的方法
from application import app, db
import json
from DataBaseFolder.Models.UserModels.UserBaseInfo import User # 导入数据库

route_user = Blueprint('user_page', __name__)


# 用户登录
@route_user.route("/login", methods=["GET", "POST"])
def login():
    # 当请求为GET是，直接跳转到登录页面
    if request.method == "GET":
        return ops_render("user/login.html")

    # 当请求为POST
    resp = {'code': 200, 'msg': '登录成功~~', 'data': {}}  # 返回信息
    req = request.values  # 前端传来的信息

    # 接口中使用的变量
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    # 用户登录验证
    if login_name is None or len(login_name) < 1:  # 用户名未输入或太短
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名 -1~~"  # 测试，正式版本中去除"-1"，下同
        return jsonify(resp)

    if login_pwd is None or len(login_pwd) < 1:  # 密码未输入或太短
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录密码 -2~~"
        return jsonify(resp)

    user_info = User.query.filter_by(UserName=login_name).first()  # 从数据库寻找登录名相同的帐号
    if not user_info:
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名和密码 -3~~"
        return jsonify(resp)

    if user_info._Password != login_pwd:
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名和密码 -4~~"
        return jsonify(resp)

    # uid：用户对应的编号
    response = make_response(json.dumps({'code': 200, 'msg': '登录成功~~'}))  # 返回登录成功的信息
    # 生成cookie
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
        UserService.geneAuthCode(user_info), user_info.UserID), 60 * 60 * 24 * 120)  # 保存120天
    return response


# 退出登录
@route_user.route("/logout")
def logout():
    response = make_response(redirect(UrlManager.buildUrl("/user/login")))  # 返回登录页面
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])  # 删除cookie
    return response
