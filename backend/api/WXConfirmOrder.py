# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
import DataBaseFolder.Interface.RestaurantBaseModify as r
import DataBaseFolder.Interface.OrderBaseModify as o
import DataBaseFolder.Interface.DishBaseModify as d
from DataBaseFolder.Interface.InterfaceHelper import GenericModify

route_WXConfirmOrder = Blueprint('WXConfirmOrder', __name__)


@route_WXConfirmOrder.route("/", methods=["GET", "POST"])
def confirmOrder():
    """
    确认收货
    :return:
    """
    # 预定义回复结构
    resp = {'statusCode': 200, 'message': '操作成功~', 'data': {}}

    # 解析请求参数
    req = eval(request.values['data'])
    order_id = int(req['order_id']) if 'order_id' in req else 0  # 菜品id

    # 拉取订单对象
    order = o.PyFind_OrderID(order_id)

    # 分支选择判断如何反应：拒绝确认收货
    if not order:
        # 当不存在此订单时拒绝确认收货
        resp['statusCode'] = 400
        resp['message'] = '操作失败，请检查返回的订单ID是否正确 -1'
        resp['data']['receive_status'] = 0
    elif order.OrderStatus != '待收货':
        # 订单状态不正确时拒绝收货请求
        resp['statusCode'] = 400
        resp['message'] = '操作失败，请检查订单状态 -2'
        resp['data']['rate_status'] = 0
    else:
        # 订单正常时接受确认收货请求
        # 使用try-expect结构处理可能的异常情况以增强稳定性
        try:
            # 解析菜品数据并丢掉无效数据
            dishList = order.Dishes.split("/")
            while '' in dishList:
                dishList.remove('')

            # 处理所有菜品的相关数据
            for dish in dishList:
                # 解析这一订单中的菜品ID和数量
                dishPair = dish.split("|")
                dishID = int(dishPair[0])
                dishSold = int(dishPair[1])
                # 拉取菜品对象与餐馆对象
                dishObj = d.PyFind_ID(dishID)
                restaurantObj = r.PyFind_ID(dishObj.SourceRestaurant)
                # 更改该菜品的销售数量
                GenericModify(1, dishID, 'Dish', 'Sold', str(dishObj.Sold + dishSold))
                # 更改餐馆的总销售额
                for i in range(dishSold):
                    GenericModify(1, restaurantObj.RestaurantID, 'Restaurant', 'TotalBenefits',
                                  str(restaurantObj.TotalBenefits + dishObj.Price))
            # 该订单状态更改为待评价
            GenericModify(1, order.OrderID, 'Order', 'OrderStatus', '\'待评价\'')
            # 返回信息表示该订单已被正常接收
            resp['data']['receive_status'] = 1
        except:
            # 当有任何异常情况在此处发生时，要求用户联系技术支持检查后端数据库情况
            resp['statusCode'] = 400
            resp['message'] = '确认收货异常，请联系后台人员确认数据状态 -3'
            resp['data']['receive_status'] = 0

    return jsonify(resp)
