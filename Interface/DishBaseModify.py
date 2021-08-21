from flask import Blueprint, jsonify, request, json
from Models.RestaurantModels.DishBase import Dish
from DataBase import db

dish=Blueprint('dish',__name__)

@dish.route('/t')
def ServerTest():
    print('Connect Success')
    return jsonify('Test Success')

def PyDirectlyAdd(dishname, price, type, tag, picture, description):
    print(dishname, price)
    dishinfo = Dish(DishName=dishname,Price=price,DishType=type,DishTag=tag,Details_Picture=picture,Description=description)
    db.session.add(dishinfo)
    db.session.commit()
    return jsonify("ADD_SUCCESS")

@dish.route('/list')
def List():
    dishes = Dish.query.all()
    print(dishes)
    dishes_output = []
    for dish in dishes:
        dishes_output.append(dish.to_json())
    return jsonify(dishes_output)

def PyList():
    return Dish.query.all()

@dish.route('/details/<dishid>')
def Find_ID(dishid):
    dish = Dish.query.get(dishid)
    return jsonify(dish.to_json())

def PyFind_ID(dishid):
    return Dish.query.get(dishid)

def PyFind_Name(dishname):
    return Dish.query.filter_by(DishName=dishname)

def PyFind_Type(dishtype):
    return Dish.query.filter(DishType=dishtype).all()

def PyFind_Tag(dishtag):
    return Dish.query.filter(Dish.DishTag.__contains__(dishtag)).all()

