# -*- coding: utf-8 -*-
from random import choice
from flask import Blueprint, jsonify

import DataBaseFolder.Interface.DishBaseModify as d

route_WXRecommend = Blueprint('WXRecommend', __name__)


@route_WXRecommend.route('/', methods=['GET', 'POST'])
def recommend():
    # 预定义回复结构
    resp = {'statusCode': 200, 'message': '操作成功~', 'data': []}

    # 记录已经推荐过的菜品id
    recommended_dish_id = []

    # 所有菜品的清单
    dishList = d.PyList()

    # 所有菜品的id
    dishIDS = [i.DishID for i in dishList]

    # 随机选三个菜返回推荐信息：菜品ID，菜品图片
    while len(recommended_dish_id) < 3:

        # 随机生成1-10之间的订单id
        dish_id = choice(dishIDS)

        # 如果这个菜没有推荐过，将信息加入回复体
        if dish_id not in recommended_dish_id:
            recommended_dish_id.append(dish_id)

            # 拉取菜品对象
            dish = d.PyFind_ID(dish_id)
            resp['data'].append(
                {
                    'dish_id': dish.DishID,
                    'dish_img': dish.Details_Picture
                }
            )
        else:
            # 如果已经推荐过或者这个菜不存在，则跳过这个菜
            continue

    return jsonify(resp)
