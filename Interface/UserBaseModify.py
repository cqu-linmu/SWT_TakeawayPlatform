from flask import Blueprint, jsonify, request, json
from Models.UserModels.UserBaseInfo import User
from DataBase import db

user=Blueprint('user',__name__)

@user.route('/t')
def ServerTest():
    print('Connect Success\nTarget')
    return jsonify('Test Success')

@user.route('/add/<username>/<pwd>')
def Add(username, pwd):
    print(username, pwd)
    userinfo = User(UserName=username,Gender='未知',HeadPortrait='NeedInit',Address='NeedInit',Telephone='NeedInit')
    userinfo.SetPassword(pwd)
    db.session.add(userinfo)
    db.session.commit()
    return jsonify("ADD_SUCCESS")

def PyAdd(username, pwd,Gender='未知',headportrait='NeedInit',address='NeedInit',telephone='NeedInit'):
    print(username, pwd)
    userinfo = User(UserName=username,Gender=Gender,HeadPortrait=headportrait,Address=address,Telephone=telephone)
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

def PyList():
    users = User.query.all()
    print(users)
    users_output = []
    for user in users:
        users_output.append(user)
    return users_output

@user.route('/find/id/<userid>')
def Find_ID(userid):
    userinfo = User.query.get(userid)
    return jsonify(userinfo.to_json())

def PyFind_ID(userid):
    userinfo = User.query.get(userid)
    return userinfo

@user.route('/find/name/<username>')
def Find_Name(username):
    userinfo = User.query.filter_by(UserName=username).first()
    return jsonify(userinfo.to_json())

def PyFind_Name(username):
    userinfo = User.query.filter_by(UserName=username).first()
    return userinfo
