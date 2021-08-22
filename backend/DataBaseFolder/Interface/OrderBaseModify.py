from flask import Blueprint, jsonify
from DataBaseFolder.Models.OrderData.OrderBase import Order
from DataBaseFolder.Models.RestaurantModels.RestaurantBase import Restaurant
from DataBaseFolder.Models.UserModels.UserBaseInfo import User
from DataBaseFolder.DataBase import db

order=Blueprint('order',__name__)

@order.route('/t')
def ServerTest():
    print('Connect Success')
    return jsonify('Test Success')

def PyDirectlyAdd(resid,uid, remark, address, dishes, price, carriage):
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
    return Order.query.all()

def PyFind_OrderID(orderid):
    return Order.query.get(orderid)

def PyFind_UserID(userid):
    return Order.query.filter_by(UserID=userid).all()

@order.route('/find/dishid/<dishid>')
def PyFind_DishID(dishid):
    allorders=Order.query.all()
    returnorders=[]
    for filter in allorders :
        if(filter.Dishes.find(str(dishid))!=-1):
            returnorders.append(filter)

    return returnorders

def PyFind_OrderStatusEnum(orderstatus):
    return Order.query.filter_by(OrderStatus=orderstatus).all()
