from flask import Blueprint, request, jsonify, make_response, g, redirect
from DataBaseFolder.Models.RestaurantModels.DishBase import Dish
from DataBaseFolder.Interface.DishBaseModify import *
from utils.Helper import *
from application import app, db
import json
route_stat = Blueprint('stat_page', __name__)
app.register_blueprint(route_stat, url_prefix="/stat")

@route_stat.route("/index",methods=['GET', 'POST'])
def index():
  
    req = request.values
    page = int(req['page']) if ('page' in req and req['page']) else 1
    page_size=int(req['pageSize']) if ('pageSize' in req and req['pageSize']) else 1
    token = req['token']
    token_check(token)
    pages=db.session.quary(Dish).filter(Dish.OrderID.panginate(page,page_size))
    def bedict(a):
        lic =[]
        for item in a:
            lic.append(
                {
                "dish_id": item.DishID,
                "dish_name": item.DishName,
                "dish_number": item.Sold,
                "dish_score" :item.Score
                }
            )
        return lic
    return jsonify(bedict(pages) )
    


    