# -*- coding: utf-8 -*-
import random
from flask import Blueprint, request, jsonify

import DataBaseFolder.Interface.DishBaseModify as d

route_WXRecommend = Blueprint('WXRecommend', __name__)


@route_WXRecommend.route('/', methods=['GET', 'POST'])
def recommend():
    resp = {'code': 200, 'message': '操作成功~', 'data': []}
    recommended_dish_id = []
    for i in range(3):
        dish_id = random.randint(1, 10)
        if dish_id not in recommended_dish_id:
            recommended_dish_id.append(dish_id)
            dish = d.PyFind_ID(dish_id)
            resp['data'].append(
                {
                    'dish_id': dish.DishID,
                    'dish_img': dish.Details_Picture
                }
            )
    return jsonify(resp)
