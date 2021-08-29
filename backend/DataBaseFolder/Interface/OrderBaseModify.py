from flask import Blueprint, jsonify
from DataBaseFolder.Models.OrderData.OrderBase import Order
from DataBaseFolder.Models.RestaurantModels.RestaurantBase import Restaurant
from DataBaseFolder.Models.UserModels.UserBaseInfo import User
from DataBaseFolder.DataBase import db
import datetime

#order=Blueprint('order',__name__)

'''
@order.route('/t')
def ServerTest():
    print('Connect Success')
    return jsonify('Test Success')
'''

def PyDirectlyAdd(resid,uid, remark, address, dishes, price, carriage):
    '''
    You shouldn't use it! Add any order in restaurant instead
    :param resid: restaurant id
    :param uid: user id
    :param remark: user remark
    :param address: user address
    :param dishes: dishes
    :param price: order price
    :param carriage: order carriage
    :return: order object
    '''
    print(remark, address,dishes,price,carriage)
    orderinfo = Order(UserID=uid,Remark=remark,OrderAddress=address,Dishes=dishes,Price=price,Carriage=carriage)
    orderinfo.ConstructOthers()
    res = Restaurant.query.get(resid)
    user = User.query.get(uid)
    res.Orders.append(orderinfo)
    user.Orders.append(orderinfo)
    db.session.merge(res)
    db.session.merge(user)
    db.session.add(orderinfo)
    db.session.commit()
    return orderinfo

def PyList():
    '''
    :return: all orders
    '''
    return Order.query.all()

def PyFind_OrderID(orderid):
    '''
    Find a order matched input order id
    :param orderid: order id
    :return: order object
    '''
    return Order.query.get(orderid)

def PyFind_UserID(userid):
    '''
    Find orders matched input user id
    :param userid: user id
    :return: orders list
    '''
    return Order.query.filter_by(UserID=userid).all()

'''
@order.route('/find/dishid/<dishid>')
def PyFind_DishID(dishid):
    allorders=Order.query.all()
    returnorders=[]
    for filter in allorders :
        if(filter.Dishes.find(str(dishid))!=-1):
            returnorders.append(filter)

    return returnorders
'''

def PyFind_OrderStatusEnum(orderstatus):
    '''
    Find orders matched input order status
    :param orderstatus: order status
    :return: orders list
    '''
    return Order.query.filter_by(OrderStatus=orderstatus).all()

def PyFind_OrderTime(nowdate):
    '''
    Find orders matches this date(not time)
    :param nowdate: nowdate date, object including year, month an day
    :return: orders list
    '''
    datefilter=[nowdate.__getattribute__('year'),nowdate.__getattribute__('month'),nowdate.__getattribute__('day')]
    OrdersList=PyList()
    returnlist=[]

    for order in OrdersList:
        orderfilter=[order.OrderTime.__getattribute__('year'),order.OrderTime.__getattribute__('month'),
                     order.OrderTime.__getattribute__('day')]
        if(datefilter[0]==orderfilter[0] and datefilter[1]==orderfilter[1] and datefilter[2]==orderfilter[2]):
            returnlist.append(order)

    return returnlist
