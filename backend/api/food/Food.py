# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, redirect
from utils.Helper import ops_render, getCurrentDate, iPagination, getDictFilterField
from application import app, db
from utils.UrlManager import UrlManager
from decimal import Decimal
from sqlalchemy import or_

# 相关数据库
# from common.models.Food import Dishdatum
from DataBaseFolder.Models.RestaurantModels.DishBase import Dish

route_food = Blueprint('food_page', __name__)


# 餐品管理首页显示
@route_food.route("/index")
def index():
    resp_data = {}  # 返回数据

    req = request.values
    page = int(req['page']) if ('page' in req and req['page']) else 1
    query = Dish.query

    # 利用前端传来'mix_kw'进行搜索（名称或许要修改）
    # 根据菜名DishName搜索
    if 'mix_kw' in req:
        rule = or_(Dish.DishName.ilike("%{0}%".format(req['mix_kw'])))
        query = query.filter(rule)

    # 分页
    page_params = {
        'total': query.count(),
        'page_size': app.config['PAGE_SIZE'],
        'page': page,
        'display': app.config['PAGE_DISPLAY'],
        'url': request.full_path.replace("&p={}".format(page), "")
    }
    pages = iPagination(page_params)
    offset = (page - 1) * app.config['PAGE_SIZE']
    list = query.order_by(Dish.DishID.desc()).offset(offset).limit(app.config['PAGE_SIZE']).all()

    resp_data['list'] = list
    resp_data['pages'] = pages
    resp_data['search_con'] = req

    resp_data['current'] = 'index'
    return ops_render("food/index.html", resp_data)


# 餐品的具体信息显示
@route_food.route("/info")
def info():
    resp_data = {}  # 返回信息
    req = request.args
    DishID = int(req.get("DishID", 0))  # 获取菜品编号，根据菜品编号获取菜品的全部信息
    reback_url = UrlManager.buildUrl("/food/index")  # 跳转的网址

    if DishID < 1:
        return redirect(reback_url)

    info = Dish.query.filter_by(DishID=DishID).first()
    if not info:
        return redirect(reback_url)

    resp_data['info'] = info  # 返回菜品信息
    resp_data['current'] = 'index'
    return ops_render("food/info.html", resp_data)


# 餐品编辑
@route_food.route("/set", methods=['GET', 'POST'])
def set():
    # 当前端请求为GET，显示菜品信息
    if request.method == "GET":
        resp_data = {}
        req = request.args
        DishID = int(req.get('DishID', 0))
        info = Dish.query.filter_by(DishID=DishID).first()
        resp_data['info'] = info
        resp_data['current'] = 'index'
        return ops_render("food/set.html", resp_data)

    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}  # 提前定义返回信息
    req = request.values

    # 修改数据中菜品的信息
    DishID = int(req['DishID']) if 'DishID' in req and req['DishID'] else 0  # 菜品编号
    dish_class = req['dish_class'] if 'dish_class' in req else ''  # 菜品分类
    dish_name = req['dish_name'] if 'dish_name' in req else ''  # 菜品名
    dish_price = req['dish_price'] if 'dish_price' in req else ''  # 菜品价格
    Details_Picture = req['Details_Picture'] if 'Details_Picture' in req else ''  # 菜品图片
    dish_description = req['dish_description'] if 'dish_description' in req else ''  # 菜品描述
    DishTag = req['DishTag'] if 'DishTag' in req else ''  # 菜品标签

    # 检查菜品分类是否合理
    if dish_class is None or len(dish_class) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的分类~~"
        return jsonify(resp)

    # 检查菜品名是否合理
    if dish_name is None or len(dish_name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的名称~~"
        return jsonify(resp)

    # 检查菜品价格是否合理
    if not dish_price or len(dish_price) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的售卖价格~~"
        return jsonify(resp)

    price = Decimal(dish_price).quantize(Decimal('0.00'))
    if price <= 0:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的售卖价格~~"
        return jsonify(resp)

    # 检查菜品图片是否合理
    if Details_Picture is None or len(Details_Picture) < 3:
        resp['code'] = -1
        resp['msg'] = "请上传封面图~~"
        return jsonify(resp)

    # 检查菜品描述是否合理
    if dish_description is None or len(dish_description) < 3:
        resp['code'] = -1
        resp['msg'] = "请输入图书描述，并不能少于10个字符~~"
        return jsonify(resp)

    # 检查菜品标签是否合理
    if DishTag is None or len(DishTag) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入标签，便于搜索~~"
        return jsonify(resp)

    food_info = Dish.query.filter_by(DishID=DishID).first()
    if food_info:
        model_food = food_info
    else:
        model_food = Dish()

    model_food.DishType = dish_class
    model_food.name = dish_name
    model_food.Price = dish_price
    model_food.Details_Picture = Details_Picture
    model_food.Description = dish_description
    model_food.DishTag = DishTag

    db.session.add(model_food)
    db.session.commit()

    return jsonify(resp)


# 餐品的删除
@route_food.route("/ops", methods=["POST"])
def ops():
    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values

    DishID = req['DishID'] if 'DishID' in req else 0
    act = req['act'] if 'act' in req else ''  # 前端传来的操作指令

    if not id:
        resp['code'] = -1
        resp['msg'] = "请选择要操作的账号~~"
        return jsonify(resp)

    food_info = Dish.query.filter_by(DishID=DishID).first()
    if not food_info:
        resp['code'] = -1
        resp['msg'] = "指定美食不存在~~"
        return jsonify(resp)

    if act == "remove":
        food_info.status = 0

    # 直接删除该条记录（待改）
    db.session.delete(food_info)
    db.session.commit()
    return jsonify(resp)
