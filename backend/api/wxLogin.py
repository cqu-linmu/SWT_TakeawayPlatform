# -*- coding: utf-8 -*-
import json
import random
import requests
from flask import Blueprint, request, jsonify, make_response

from application import app
from utils.user.UserService import (UserService)  # UserService：封装用户登录相关的方法
from DataBaseFolder.Construct.ConstructHelper import RandomPwd, RandomTelephone  # 随机20位密码生成

import DataBaseFolder.Interface.UserBaseModify as u  # 用户编辑接口
from DataBaseFolder.Interface.InterfaceHelper import GenericModify

route_WXLogin = Blueprint('WXLogin', __name__)


def getWeChatOpenId(code):
    """
    从微信平台处获取数据结构：
    {appid:小程序 appId
    secret:小程序 appSecret
    js_code:登录时获取的 code，前端传过来的code}
    :return: 用户的openid
    """
    url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code" \
        .format(app.config['MINA_APP']['appid'], app.config['MINA_APP']['appkey'], code)
    r = requests.get(url)  # 根据官网的要求需要发送get请求，获取到响应对象
    res = json.loads(r.text)  # 从中取出内容
    openid = None  # openid:用户唯一标识
    if 'openid' in res:
        openid = res['openid']
    return openid  # 将其当成变量返回


@route_WXLogin.route("/", methods=["GET", "POST"])
def login():
    """
    微信登录接口，包含用户创建功能
    :return:
    """
    # 预定义回复结构
    resp = {'statusCode': 200, 'message': '操作成功~', 'data': {}}

    # 解析并处理请求参数
    req = eval(request.values['data'])
    # code
    code = req['code'] if 'code' in req else ''
    # nickName
    user_name = req['nickName'] if 'nickName' in req else ''
    # gender
    gender = req['gender'] if 'gender' in req else ''
    if gender == 0:
        gender = '未知'
    elif gender == 1:
        gender = '男'
    else:
        gender = '女'
    # avatarUrl
    head_portrait = req['avatarUrl'] if 'avatarUrl' in req else ''
    print(head_portrait)
    address = req['country'] + '-' + req['province'] + '-' + req['city'] + '/'

    # 当传回的code不合法时拒绝登陆
    if not code or len(code) < 1:
        resp['statusCode'] = 400
        resp['message'] = "需要code -1"
        return jsonify(resp)

    # 获取openid
    openid = getWeChatOpenId(code)
    print(openid)

    # 当openid为空时拒绝登录
    if openid is None:
        resp['statusCode'] = 400
        resp['message'] = "调用微信出错 -2"
        return jsonify(resp)

    # 根据openid查询用户数据
    userInfo = u.PyFind_OpendID(openid)

    # 下面两个分支的成功情况都需要返回token和refresh_token，用UserService.genAuthCode+id生成

    token = random.randint(1, 99999)
    refresh_token = str(token + 1)

    # 用户信息为空，说明该用户是第一次登录，执行注册流程
    if not userInfo:
        # 注册账号
        u.PyAdd(user_name, RandomPwd(), openid, gender, head_portrait, address, RandomTelephone())

        # 新建的用户对象
        new_user = u.PyFind_Name(user_name)
        new_user_id = new_user.UserID

        # 执行初始化设置
        GenericModify(1, new_user_id, 'User', 'Balance', str(random.randint(100, 1000)))
        GenericModify(1, new_user_id, 'User', 'Token', str(token))

        # 将登录态设置为已登录
        new_user.Login()

        # 设置data中的相关信息：user_id,token,refresh_token
        resp['data']['user_id'] = str(new_user_id)
        resp['data']['token'] = str(token)
        resp['data']['refresh_token'] = str(refresh_token)
        resp['message'] = "创建并绑定账号成功！ 您的账户id是" + str(new_user_id)

        # 设置响应体：信息和cookie
        response = make_response(json.dumps(resp))  # 返回登录成功的信息
        response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
            UserService.geneAuthCode(new_user), new_user_id), 60 * 60 * 24 * 120)  # 保存120天

        return response

    # 传回的用户信息不正确时拒绝登录;用户已经处于登录状态时拒绝登录
    elif userInfo.UserName != user_name or userInfo.GetLoginStatus():
        resp['statusCode'] = 400
        resp['message'] = "登陆失败！检查您的账号状态 -3, -4"

        return jsonify(resp)

    # openid已经绑定到了现有账户且其他信息正确，则允许直接登陆
    GenericModify(1, userInfo.UserID, 'User', 'Token', str(token))
    userInfo.Login()

    # 设置data中的相关信息：user_id,token,refresh_token
    resp['data']['user_id'] = str(userInfo.UserID)
    resp['data']['token'] = str(token)
    resp['data']['refresh_token'] = str(refresh_token)
    resp['message'] = "登陆成功！"

    # 置响应体：信息和cookie
    response = make_response(json.dumps(resp))  # 返回登录成功的信息
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
        UserService.geneAuthCode(userInfo), userInfo.UserID), 60 * 60 * 24 * 120)  # 保存120天

    return response
