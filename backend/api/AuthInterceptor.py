# -*- coding: utf-8 -*-
import re

from flask import request, g

# from common.models.User import (UserdataAll)
from DataBaseFolder.Interface.UserBaseModify import *
from application import app
from utils.user.UserService import (UserService)


@app.before_request
def before_request():
    '''
    请求前验证模块
    '''
    ignore_urls = app.config['IGNORE_URLS']
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']
    path = request.path

    # var = app.logger.info
    # 如果是静态文件就不要查询用户信息了
    pattern = re.compile('%s' % "|".join(ignore_check_login_urls))
    if pattern.match(path):
        return

    # 查询用户信息
    user_info = check_login()
    app.logger.info(user_info)
    g.current_user = None
    if user_info:
        g.current_user = user_info
    pattern = re.compile('%s' % "|".join(ignore_urls))

    if pattern.match(path):
        return
    return


def check_login():
    '''
    判断用户是否已经登录
    '''
    cookies = request.cookies
    auth_cookie = cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else None
    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False

    try:
        user_info = PyFind_ID(auth_info[1])
    except Exception:
        return False

    if user_info is None:
        return False

    if auth_info[0] != UserService.geneAuthCode(user_info):
        return False

    return user_info
