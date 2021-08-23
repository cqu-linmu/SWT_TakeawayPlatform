from flask import Blueprint, jsonify
from DataBaseFolder.Models.RestaurantModels.DishBase import Dish
from DataBaseFolder.Models.RestaurantModels.RestaurantBase import Restaurant
from DataBaseFolder.DataBase import db

dish=Blueprint('dish',__name__)

# database test route

@dish.route('/t')
def ServerTest():
    print('Connect Success')
    return jsonify('Test Success')

@dish.route('/list')
def List():
    dishes = Dish.query.all()
    print(dishes)
    dishes_output = []
    for dish in dishes:
        dishes_output.append(dish.to_json())
    return jsonify(dishes_output)

@dish.route('/find/id/<dishid>')
def Find_ID(dishid):
    return jsonify(Dish.query.get(dishid).to_json())

# given interfaces

def PyDirectlyAdd(resid, dishname, price, type, tag, picture, description):
    '''
    
    '''
    print(dishname, price)
    dishinfo = Dish(DishName=dishname,Price=price,DishType=type,DishTag=tag,Details_Picture=picture,Description=description)
    res = Restaurant.query.get(resid)
    res.Dishes.append(dishinfo)
    db.session.add(dishinfo)
    db.session.merge(res)
    db.session.commit()
    return dishinfo

def PyList():
    '''
    
    '''
    return Dish.query.all()

def PyFind_ID(dishid):
    '''
    
    '''
    return Dish.query.get(dishid)

def PyFind_Name(dishname):
    '''
    
    '''
    return Dish.query.filter_by(DishName=dishname).first()

def PyFind_Type(dishtype):
    '''
    
    '''
    return Dish.query.filter(DishType=dishtype).all()

def PyFind_Tag(dishtag):
    '''
    
    '''
    alldishes = Dish.query.all()
    returndishes = []
    for filter in alldishes:
        if (filter.DishTag.find(str(dishtag)) != -1):
            returndishes.append(filter)
    return returndishes

def PyFind_Score(score):
    '''
    
    '''
    return Dish.query.filter_by(Score=score).all()
