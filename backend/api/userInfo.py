from flask import Blueprint, request, jsonify, make_response, g, redirect
from utils.user.UserService import (UserService)  # UserService：封装用户登录相关的方法
from utils.Helper import (ops_render)  # ops_render:渲染页面
from utils.UrlManager import (UrlManager)  # UrlManager：统一封装生成各种url的方法
from application import app, db
import json
from DataBaseFolder.Interface.UserBaseModify import *  # 导入数据库修改接口

route_login = Blueprint('login', __name__)

# 用户登录接口  [接口1]
@route_login.route("/userinfo", methods=["GET"])
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
