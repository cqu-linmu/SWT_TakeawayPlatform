"""
统一封装辅助用的方法
iPagination：自定义分页类
ops_render：统一渲染方法
getCurrentDate：获取当前时间
getFormatDate：获取格式化的时间
getDictFilterField：
selectFilterObj：
token_check:token检查（已弃用）
"""

from flask import g, render_template
import datetime
from utils.UrlManager import *
from  DataBaseFolder.Models.UserModels.UserBaseInfo import User

# 自定义分页类
def iPagination(params):
    import math

    ret = {
        "is_prev": 1,
        "is_next": 1,
        "from": 0,
        "end": 0,
        "current": 0,
        "total_pages": 0,
        "page_size": 0,
        "total": 0,
        "url": params['url']
    }

    total = int(params['total'])
    page_size = int(params['page_size'])
    page = int(params['page'])
    display = int(params['display'])
    total_pages = int(math.ceil(total / page_size))
    total_pages = total_pages if total_pages > 0 else 1
    if page <= 1:
        ret['is_prev'] = 0

    if page >= total_pages:
        ret['is_next'] = 0

    semi = int(math.ceil(display / 2))

    if page - semi > 0:
        ret['from'] = page - semi
    else:
        ret['from'] = 1

    if page + semi <= total_pages:
        ret['end'] = page + semi
    else:
        ret['end'] = total_pages

    ret['current'] = page
    ret['total_pages'] = total_pages
    ret['page_size'] = page_size
    ret['total'] = total
    ret['range'] = range(ret['from'], ret['end'] + 1)
    return ret


# 统一渲染方法
def ops_render(template, context={}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template, **context)


# 获取当前时间
def getCurrentDate(format="%Y-%m-%d %H:%M:%S"):
    # return datetime.datetime.now().strftime( format )
    return datetime.datetime.now()


# 获取格式化的时间
def getFormatDate(date=None, format="%Y-%m-%d %H:%M:%S"):
    if date is None:
        date = datetime.datetime.now()

    return date.strftime(format)


# 根据某个字段获取一个dic出来
def getDictFilterField(db_model, select_filed, key_field, id_list):
    ret = {}
    query = db_model.query
    if id_list and len(id_list) > 0:
        query = query.filter(select_filed.in_(id_list))

    list = query.all()
    if not list:
        return ret
    for item in list:
        if not hasattr(item, key_field):
            break

        ret[getattr(item, key_field)] = item
    return ret


def selectFilterObj(obj, field):
    ret = []
    for item in obj:
        if not hasattr(item, field):
            break
        if getattr(item, field) in ret:
            continue
        ret.append(getattr(item, field))
    return ret


def getDictListFilterField(db_model, select_filed, key_field, id_list):
    ret = {}
    query = db_model.query
    if id_list and len(id_list) > 0:
        query = query.filter(select_filed.in_(id_list))

    list = query.all()
    if not list:
        return ret
    for item in list:
        if not hasattr(item, key_field):
            break
        if getattr(item, key_field) not in ret:
            ret[getattr(item, key_field)] = []

        ret[getattr(item, key_field)].append(item)
    return ret


# token 检查
def token_check(token):
    user_info = User.query.filter_by(Token=token).first()
    if not user_info:
        return UrlManager.buildUrl("/login")