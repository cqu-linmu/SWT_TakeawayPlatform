from flask import Blueprint, request, jsonify, make_response, g, redirect
from DataBaseFolder.Models.RestaurantModels.DishBase import Dish
from DataBaseFolder.Interface import DishBaseModify as d
from utils.Helper import *
from application import app, db
import json
route_stat = Blueprint('stat_page', __name__)
app.register_blueprint(route_stat, url_prefix="/stat")

# 单品销量统计接口 [接口11]
@route_stat.route("/index",methods=['GET', 'POST'])
def index():
  
    req = request.values
    page = int(req['page']) if ('page' in req and req['page']) else 1
    page_size=int(req['pageSize']) if ('pageSize' in req and req['pageSize']) else 1
    dishList=d.PyList()
    listNum=len(dishList)
    pageNum=listNum/page_size
    dishList=dishList[(page-1)*page_size:page*page_size]
    lic = []
    lic.append({"pageNum":pageNum})
    def bedict(a):
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
    return jsonify(bedict(dishList) )
    


    