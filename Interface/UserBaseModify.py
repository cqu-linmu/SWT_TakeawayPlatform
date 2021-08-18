from flask import Blueprint, jsonify, request, json
from Models.UserModels.UserBaseInfo import User
from DataBase import db

user=Blueprint('user',__name__)

@user.route('/t')
def ServerTest():
    print('Connect Success')
    return jsonify('Test Success')

@user.route('/add/<username>/<pwd>')
def Add(username, pwd):
    print(username, pwd)
    userinfo = User(UserName=username)
    userinfo.SetPassword(pwd)
    db.session.add(userinfo)
    db.session.commit()
    return jsonify("ADD_SUCCESS")

@user.route('/list')
def List():
    users = User.query.all()
    print(users)
    users_output = []
    for user in users:
        users_output.append(user.to_json())
    return jsonify(users_output)

@user.route('/details/<userid>')
def Find(userid):
    user = User.query.get(userid)
    return jsonify(user.to_json())