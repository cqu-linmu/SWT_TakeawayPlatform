from flask import Blueprint, request, jsonify

# 相关数据库调用
from DataBaseFolder.Interface import OrderBaseModify as o
import DataBaseFolder.Interface.DishBaseModify as d

route_orderList = Blueprint('order-list', __name__)


@route_orderList.route("/", methods=['GET', 'POST'])
def index():
    '''
    订单管理页面接口
    '''
    resp = {'code': 200, 'msg': '获取订单列表成功', 'data': {}, 'total': 0}
    req = request.values
    pageNum = int(req['pageNum']) if ('pageNum' in req and req['pageNum']) else 1  # 当前页数
    page_size = int(req['pageSize'])  # 页面订单条数

    orderList = o.PyList()
    totalList = len(orderList)  # 订单总条数
    if pageNum == -1:  # 当pageNum=-1时，返回所有订单
        orderList = orderList
    else:
        orderList = orderList[(pageNum - 1) * page_size:pageNum * page_size]
    lic = []

    def bedict(a):
        for item in a:
            dishes = item.Dishes
            dishList = dishes.split('/')
            while '' in dishList:
                dishList.remove('')
            order_dish = ''
            for dish in dishList:
                dishID = int(dish.split('|')[0])
                dishNum = int(dish.split('|')[1])
                dishInfo = d.PyFind_ID(dishID)
                dishName = dishInfo.DishName
                order_dish += dishName+'*'+str(dishNum)+" "
            lic.append(
                {
                    "order_dish": order_dish,
                    "order_id": item.OrderID,
                    "order_price": item.Price,
                    "order_time": item.OrderTime,
                    "order_status": item.OrderStatus
                }
            )
        return lic

    resp['data'] = bedict(orderList)
    resp['total'] = totalList
    return jsonify(resp)
