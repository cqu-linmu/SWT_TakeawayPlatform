from flask import Blueprint, request, jsonify, make_response, g, redirect
from DataBaseFolder.Models.RestaurantModels.DishBase import Dish
from common.libs.Helper import *
from application import app, db
route_stat = Blueprint('stat_page', __name__)


@route_stat.route("/index")
def index():
    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    token = req['token']
    token_check(token)

    query = Dish.query
    page_params = {
        'total': query.count(),
        'page_size': app.config['PAGE_SIZE'],
        'page': page,
        'display': app.config['PAGE_DISPLAY'],
        'url': request.full_path.replace("&p={}".format(page), "")
    }
    # 分页操作
    pages = iPagination(page_params)
    offset = (page - 1) * app.config['PAGE_SIZE']
    pay_list = query.order_by(Dish.id.desc()).offset(offset).limit(app.config['PAGE_SIZE']).all()
    data_list = []
    resp_data['sell_quantity'] = 0
    for item in pay_list:
        tmp_data = {
            "dish_id": item.DishID,
            "dish_name": item.DishName,
            "dish_number": item.Sold
        }
        resp_data['sell_quantity'] += item.Price*item.Sold

        data_list.append(tmp_data)

    resp_data['list'] = data_list
    resp_data['pages'] = pages
    resp_data['search_con'] = req
    resp_data['pay_status_mapping'] = app.config['PAY_STATUS_MAPPING']
    resp_data['current'] = 'index'

    return ops_render("stat/index.html", resp_data)
