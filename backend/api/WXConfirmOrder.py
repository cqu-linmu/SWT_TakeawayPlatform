# -*- coding: utf-8 -*-
from utils.MemberService import MemberService
from flask import Blueprint, request, jsonify
import DataBaseFolder.Interface.RestaurantBaseModify as r
import DataBaseFolder.Interface.OrderBaseModify as o
import DataBaseFolder.Interface.DishBaseModify as d

route_WXConfirmOrder = Blueprint('WXConfirmOrder', __name__)


@route_WXConfirmOrder.route("/", methods=["GET", "POST"])
def confirmOrder():
    '''
    确认收货
    :return:
    '''
    resp = {'code': 200, 'message': '操作成功~', 'data': {}}
    req = request.values['data']

    # 解析请求参数
    order_id = int(req['order_id']) if 'order_id' in req else 0  # 菜品id

    # 拉取订单对象
    order = o.PyFind_OrderID(order_id)

    if not order:
        # 当不存在此订单时拒绝确认收货
        resp['code'] = 400
        resp['message'] = '操作失败，请检查返回的订单ID是否正确 -1'
        resp['data']['receive_status'] = 0
    elif order.OrderStatus != '待收货':
        # 订单状态不正确时拒绝评分请求
        resp['code'] = 400
        resp['message'] = '操作失败，请检查订单状态 -2'
        resp['data']['rate_status'] = 0
    else:
        # 当存在对应的订单时接受确认操作
        try:
            dishList = order.Dishes.split("/")
            for dish in dishList[:-2]:
                # 解析这一订单中的菜品名称和数量
                dishPair = dish.split("|")
                dishID = dishPair[0]
                dishSold = int(dishPair[1])
                # 拉取菜品对象并更改评分
                dishObj = d.PyFind_ID(dishID)
                restaurantObj = r.PyFind_ID(dishObj.SourceRestaurant)
                # 更改销售数量
                dishObj.Sold += dishSold
                # 更改销售额
                for i in range(dishSold):
                    restaurantObj.TotalBenefits += dishObj.Price
            # 状态更改为待评价
            order.OrderStatus = '待评价'
            resp['data']['receive_status'] = 1
        except:
            resp['code'] = 400
            resp['message'] = '确认收货异常，请联系后台人员确认数据状态 -3'
            resp['data']['receive_status'] = 0

    return jsonify(resp)
