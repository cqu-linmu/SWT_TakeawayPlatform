from flask import Blueprint, jsonify
from DataBaseFolder.Models.RestaurantModels.DishBase import Dish
from DataBaseFolder.Models.RestaurantModels.RestaurantBase import Restaurant
from DataBaseFolder.DataBase import db

# dish=Blueprint('dish',__name__)
'''
#Connect test
@dish.route('/t')
def ServerTest():
    print('Connect Success')
    return jsonify('Test Success')
'''


def PyDirectlyAdd(resid, dishname, price, type, tag, picture, description):
    '''
    You shouldn't use it! Add any dish in restaurant instead
    :param resid: restaurant id
    :param dishname: dish name
    :param price: dish price
    :param type: dish type
    :param tag: dish tag
    :param picture: dish picture
    :param description: dish description
    :return: dish object
    '''
    print(dishname, price)
    dishinfo = Dish(DishName=dishname, Price=price, DishType=type, DishTag=tag, Details_Picture=picture,
                    Description=description)
    res = Restaurant.query.get(resid)
    res.Dishes.append(dishinfo)
    db.session.add(dishinfo)
    db.session.merge(res)
    db.session.commit()
    return dishinfo


'''
@dish.route('/list')
def List():
    dishes = Dish.query.all()
    print(dishes)
    dishes_output = []
    for dish in dishes:
        dishes_output.append(dish.to_json())
    return jsonify(dishes_output)
'''


def PyList():
    '''
    :return: All dishes
    '''
    return Dish.query.all()


'''
@dish.route('/find/id/<dishid>')
def Find_ID(dishid):
    return jsonify(Dish.query.get(dishid).to_json())
'''


def PyFind_ID(dishid):
    '''
    Find a dish matched input dish id
    :param dishid: dish id
    :return: a dish matched input id
    '''
    return Dish.query.get(dishid)


def PyFind_Name(dishname):
    '''
    Find a dish matched input dish name
    :param dishname: dish name
    :return: a dish matched input name
    '''
    return Dish.query.filter_by(DishName=dishname).first()


def PyFind_Type(dishtype):
    '''
    Find dishes matched input dish type
    :param dishtype: dish type
    :return: dishes list matched input type
    '''
    return Dish.query.filter(DishType=dishtype).all()


def PyFind_Tag(dishtag):
    '''
    Find dishes matched input dish tag
    :param dishtag: dish tag
    :return: dishes list matched input tag
    '''
    alldishes = Dish.query.all()
    returndishes = []
    for filter in alldishes:
        if (filter.DishTag.find(str(dishtag)) != -1):
            returndishes.append(filter)

    return returndishes


def PyFind_Score(score):
    '''
    Find dishes matched input score
    :param score: dish score
    :return: dishes list matched this score
    '''
    return Dish.query.filter_by(Score=score).all()
