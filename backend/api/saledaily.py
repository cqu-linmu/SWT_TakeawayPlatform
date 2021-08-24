from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
import DataBaseFolder.Interface.OrderBaseModify as o

route_saledaily = Blueprint('sale-daily', __name__)


@route_saledaily.route('/', methods=["GET", "POST"])
def saleDaily():
    resp = {'code': 200, 'message': '获取每日流水成功', 'data': []}  # 提前定义返回信息
    stTime = request.values['order_time_st']

    # 前端传回的时间数据格式：order_time_st : '2021-08-23' string类型。
    # 传回前三十天数据
    edDate = datetime(int(stTime[0:4]), int(stTime[5:7]), int(stTime[8:10]))

    # 访问数据库拉取利润记录数据
    orders = o.PyList()

    # 计算起始时间点
    stDate = (edDate - timedelta(days=30))
    if stDate < o.PyFind_OrderID(1).OrderTime:
        stDate = o.PyFind_OrderID(1).OrderTime

    stDateStr = str(stDate.year) + '-' + str(stDate.month) + '-' + str(stDate.day)
    edDateStr = str(edDate.year) + '-' + str(edDate.month) + '-' + str(edDate.day)

    if stDateStr == edDateStr:
        resp['data'].append({
            'sale-daily': 0,
            'order_time': str(stDate.year) + '-' + str(stDate.month) + '-' + str(stDate.day)
        })
        for order in orders:
            resp['data'][0]['sale-daily'] += order.Price
    else:
        # 用来标识一天的时间段
        deltaDate = timedelta(days=1) + stDate
        # 用来统计一天的订单总销售额
        tmpSumBenefit = 0

        # 使用滑动窗口统计30天营业额数据
        for order in orders:
            # 退出条件
            if stDate > edDate:
                break
            # 窗口体
            if stDate <= order.OrderTime <= deltaDate:
                # 加上该订单的价格
                tmpSumBenefit = tmpSumBenefit + order.Price
            elif order.OrderTime > deltaDate:
                # 如果日期超出，则记录昨天的数据，同时更新前后区间；更新当天营业额
                resp['data'].append({
                    'sale-daily': tmpSumBenefit,
                    'order_time': str(stDate.year) + '-' + str(stDate.month) + '-' + str(stDate.day)
                })
                stDate = order.OrderTime
                deltaDate = stDate + timedelta(days=1)
                tmpSumBenefit = order.Price

        # 记录最后一天的营业额
        resp['data'].append({
            'sale-daily': tmpSumBenefit,
            'order_time': str(stDate.year) + '-' + str(stDate.month) + '-' + str(stDate.day)
        })
    return jsonify(resp)
