# -*- coding: utf-8 -*-
from utils.MemberService import MemberService
from flask import Blueprint, request, jsonify
from DataBaseFolder.Interface import DishBaseModify as d

route_WXDishList = Blueprint('WXDishList', __name__)


@route_WXDishList.route("/", methods=["GET", "POST"])
def foodIndex():
    '''
    首页菜品显示(finish)
    '''
    resp = {'statusCode': 200, 'message': '操作成功~', 'data': {}}

    # 菜品显示
    food_list = d.PyList()

    data_food_list = []
    if food_list:
        for item in food_list:
            tmp_data = {
                'dish_id': item.DishID,
                'dish_name': item.DishName,
                'dish_price': item.Price,
                'dish_type': item.DishType,
                'dish_tag': item.DishTag,
                'dish_img': item.Thumbnail
            }
            data_food_list.append(tmp_data)

    resp['data'] = data_food_list
    return jsonify(resp)
