from flask import Blueprint, jsonify, request, json
from Models.RestaurantModels.RestaurantBase import Restaurant
from DataBase import db
from .DishBaseModify import PyDirectlyAdd as DishAdd

restaurant=Blueprint('restaurant',__name__)

@restaurant.route('/t')
def ServerTest():
    print('Connect Success')
    return jsonify('Test Success')

@restaurant.route('/add/<resname>/<resadd>')
def Add(resname, resadd):
    print(resname, resadd)
    resinfo = Restaurant(RestaurantName=resname,Address=resadd)
    dishinfo = ('default', 0)
    resinfo.Dishes.append(dishinfo)
    db.session.add_all([resinfo,dishinfo])
    db.session.commit()
    return jsonify("ADD_SUCCESS")

def PyAdd(resname, resadd):
    print(resname, resadd)
    resinfo = Restaurant(RestaurantName=resname,Address=resadd)
    db.session.add(resinfo)
    db.session.commit()
    return resinfo

@restaurant.route('/<resid>/adddish/<dishname>/<price>/<type>/<tag>/<picture>/<description>')
def AddDish(resid,dishname,price,type,tag,picture='DefaultPath',description='None'):
    dishinfo = DishAdd(dishname,price,type,tag,picture,description)
    res = Restaurant.query.get(resid)
    res.Dishes.append(dishinfo)
    db.session.add([res,dishinfo])
    db.session.commit()
    return jsonify("ADD_DISH_SUCCESS")

def PyAddDish(resid,dishname,price,type,tag,picture='DefaultPath',description='None'):
    dishinfo = DishAdd(dishname,price,type,tag,picture,description)
    res = Restaurant.query.get(resid)
    res.Dishes.append(dishinfo)
    db.session.add([res,dishinfo])
    db.session.commit()
    return dishinfo

@restaurant.route('/list')
def List():
    ress = Restaurant.query.all()
    print(ress)
    ress_output = []
    for res in ress:
        ress_output.append(res.to_json())
    return jsonify(ress_output)

def PyList():
    ress = Restaurant.query.all()
    return  ress

@restaurant.route('/details/<resid>')
def Find_ID(resid):
    res = Restaurant.query.get(resid)
    return jsonify(res.to_json())

def PyFind_ID(resid):
    res = Restaurant.query.get(resid)
    return res

def PyFind_Name(resname):
    res = Restaurant.query.filter_by(RestaurantName=resname)
    return res
