from flask import Blueprint, jsonify, request, json
from Models.RestaurantModels.DishBase import Dish
from DataBase import db

dish=Blueprint('dish',__name__)

@dish.route('/t')
def ServerTest():
    print('Connect Success')
    return jsonify('Test Success')

@dish.route('/add/<dishname>/<price>')
def Add(dishname, price):
    print(dishname, price)
    dishinfo = Dish(DishName=dishname,Price=price)
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

@dish.route('/details/<dishid>')
def Find(dishid):
    dish = Dish.query.get(dishid)
    return jsonify(dish.to_json())