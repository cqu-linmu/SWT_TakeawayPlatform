# -*- coding: utf-8 -*-
# 小程序拦截器
from application import app
from flask import request, g, jsonify

from DataBaseFolder.Interface import UserBaseModify as U
from utils.MemberService import MemberService
import re

'''
api认证
'''


@app.before_request
def before_request_api():
    api_ignore_urls = app.config['API_IGNORE_URLS']  # 需要根据具体进行修改

    path = request.path

    # 要求该path是小程序的，不是后台的
    if '/api' not in path:
        return

    member_info = check_member_login()
    g.member_info = None
    if member_info:
        g.member_info = member_info

    pattern = re.compile('%s' % "|".join(api_ignore_urls))
    if pattern.match(path):
        return

    if not member_info:
        resp = {'code': 400, 'message': '未登录~', 'data': {}}
        return jsonify(resp)

    return


'''
判断用户是否已经登录
'''


def check_member_login():
    auth_cookie = request.headers.get("Authorization")

    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False

    try:
        member_info = U.PyFind_ID(auth_info[1])
    except Exception:
        return False

    if member_info is None:
        return False

    if auth_info[0] != MemberService.geneAuthCode(member_info):
        return False

    if member_info.status != 1:
        return False

    return member_info
