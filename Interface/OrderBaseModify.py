from flask import Blueprint, jsonify, request, json
from Models.OrderData.OrderBase import Order
from DataBase import db

order=Blueprint('order',__name__)

@order.route('/t')
def ServerTest():
    print('Connect Success')
    return jsonify('Test Success')

@order.route('/construct/<uid>/<remark>/<address>/<orders>/<price>/<carriage>')
def Add(uid,remark, address,orders,price,carriage):
    print(remark, address,orders,price,carriage)
    orderinfo = Order(UserID=uid,Remark=remark,OrderAddress=address,Orders=orders,Price=price,Carriage=carriage)
    orderinfo.ConstructOthers()
    db.session.add(orderinfo)
    db.session.commit()
    return jsonify("ADD_SUCCESS")

def PyAdd(uid,remark, address,orders,price,carriage):
    print(remark, address,orders,price,carriage)
    orderinfo = Order(UserID=uid,Remark=remark,OrderAddress=address,Orders=orders,Price=price,Carriage=carriage)
    orderinfo.ConstructOthers()
    db.session.add(orderinfo)
    db.session.commit()
    return orderinfo

def PyList():
    return Order.query.all()

def PyFind_OrderID(orderid):
    return Order.query.get(orderid)

def PyFind_UserID(userid):
    return Order.query.filter_by(UserID=userid)

def PyFind_DishID(dishid):
    return Order.query.filter(Order.Dishes.__contains__(dishid)).all()

def PyFind_OrderStatusEnum(orderstatus):
    return Order.query.filter_by(OrderStatus=orderstatus)
