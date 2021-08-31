# -*- coding: utf-8 -*-
import json
import random
import requests
from flask import Blueprint, request, jsonify, make_response

from application import app
from utils.user.UserService import (UserService)  # UserService：封装用户登录相关的方法
from DataBaseFolder.Construct.ConstructHelper import RandomPwd, RandomTelephone  # 随机20位密码生成
import DataBaseFolder.Interface.UserBaseModify as U  # 用户编辑接口

route_WXLogin = Blueprint('WXLogin', __name__)


def getWeChatOpenId(code):
    '''
    从微信平台处获取openid
    :param code:
    :return:
    '''
    url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code" \
        .format(app.config['MINA_APP']['appid'], app.config['MINA_APP']['appkey'], code)
    """
    appid:小程序 appId
    secret:小程序 appSecret
    js_code:登录时获取的 code，前端传过来的code
    """
    r = requests.get(url)  # 根据官网的要求需要发送get请求，获取到响应对象
    res = json.loads(r.text)  # 从中取出内容
    openid = None  # openid:用户唯一标识
    if 'openid' in res:
        openid = res['openid']
    return openid  # 将其当成变量返回


# 微信登录接口，包含用户创建功能
# todo: 这个接口没法测试，只能等小程序好了之后在整了;根据变更修改了接口实现
@route_WXLogin.route("/", methods=["GET", "POST"])
def login():
    resp = {'statusCode': 200, 'message': '操作成功~', 'data': {}}
    req = request.values['data']

    # 解析传回的参数
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
    address = req['country'] + '-' + req['provience'] + '-' + req['city']

    # 当传回的code不合法时拒绝登陆
    if not code or len(code) < 1:
        resp['statusCode'] = 400
        resp['message'] = "需要code -1"
        return jsonify(resp)

    # 获取openid
    openid = getWeChatOpenId(code)

    # 当openid为空时拒绝登录
    if openid is None:
        resp['statusCode'] = 400
        resp['message'] = "调用微信出错 -2"
        return jsonify(resp)

    # 根据openid查询用户数据
    userInfo = U.PyFind_OpendID(openid)

    # 下面两个分支的成功情况都需要返回token和refresh_token，用UserService.genAuthCode+id生成

    token = random.randint(1, 99999)
    refresh_token = str(token + 1)

    if not userInfo:
        # 注册账号并传回自定义登录态
        U.PyAdd(user_name, RandomPwd(), openid, gender, head_portrait, address, RandomTelephone())
        new_user = U.PyFind_Name(user_name)
        new_user.Token = str(token)
        new_user.Login()
        resp['data']['token'] = token
        resp['data']['refresh_token'] = refresh_token
        resp['message'] = "创建并绑定账号成功！ 您的账户id是" + str(new_user.UserID)

    elif userInfo.UserName != user_name:
        # 传回的用户信息不正确时拒绝登录
        resp['statusCode'] = 400
        resp['message'] = "登陆失败！请检查传回的用户信息是否正确 -3"

    elif userInfo.GetLoginStatus():
        # 用户已经处于登录状态时拒绝登录
        resp['statusCode'] = 400
        resp['message'] = "登陆失败！您的账号已经在其他客户端登录 -4"

    else:
        # openid已经绑定到了现有账户且其他信息正确，则允许直接登陆
        userInfo.Token = str(token)
        resp['data']['token'] = token
        resp['data']['refresh_token'] = refresh_token
        resp['message'] = "登陆成功！"

    response = make_response(json.dumps(resp)).set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
        UserService.geneAuthCode(userInfo), userInfo.UserID), 60 * 60 * 24 * 120)  # 保存120天

    return response
