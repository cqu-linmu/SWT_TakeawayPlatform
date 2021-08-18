from flask import Blueprint, jsonify, request, json
from Models.RestaurantModels.RestaurantBase import Restaurant
from DataBase import db

restaurant=Blueprint('restaurant',__name__)

@restaurant.route('/t')
def ServerTest():
    print('Connect Success')
    return jsonify('Test Success')

@restaurant.route('/add/<resname>/<resadd>')
def Add(resname, resadd):
    print(resname, resadd)
    resinfo = Restaurant(RestaurantName=resname,Address=resadd)
    db.session.add(resinfo)
    db.session.commit()
    return jsonify("ADD_SUCCESS")

@restaurant.route('/list')
def List():
    ress = Restaurant.query.all()
    print(ress)
    ress_output = []
    for res in ress:
        ress_output.append(res.to_json())
    return jsonify(ress_output)

@restaurant.route('/details/<resname>')
def find_user(resname):
    res = Restaurant.query.get(resname)
    return jsonify(res.to_json())