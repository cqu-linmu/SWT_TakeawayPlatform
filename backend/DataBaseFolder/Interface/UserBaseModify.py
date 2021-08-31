from DataBaseFolder.Models.UserModels.UserBaseInfo import User
from DataBaseFolder.DataBase import db
from flask import Blueprint, jsonify

#user=Blueprint('user',__name__)

'''
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
'''

def PyAdd(username, pwd, openid,Gender='未知',headportrait='NeedInit',address='NeedInit',telephone='NeedInit'):
    '''
    Add new user
    :param username: user name
    :param pwd: password
    :param openid: user OpendID
    :param Gender: gender
    :param headportrait: head portrait
    :param address: address
    :param telephone: telephone
    :return: user object
    '''
    print(username, pwd)
    userinfo = User(UserName=username,Gender=Gender,OpenID=openid,HeadPortrait=headportrait,Address=address,Telephone=telephone)
    userinfo.SetPassword(pwd)
    db.session.add(userinfo)
    db.session.commit()
    return userinfo

'''
@user.route('/list')
def List():
    users = User.query.all()
    print(users)
    users_output = []
    for user in users:
        users_output.append(user.to_json())
    return jsonify(users_output)
'''

def PyList():
    '''
    :return: all orders list
    '''
    return User.query.all()

'''
@user.route('/find/id/<userid>')
def Find_ID(userid):
    userinfo = User.query.get(userid)
    return jsonify(userinfo.to_json())
'''

def PyFind_ID(userid):
    '''
    Find a user that matches input user id
    :param userid: user id
    :return: user object
    '''
    userinfo = User.query.get(userid)
    return userinfo

'''
@user.route('/find/name/<username>')
def Find_Name(username):
    userinfo = User.query.filter_by(UserName=username).first()
    return jsonify(userinfo.to_json())
'''

def PyFind_Name(username):
    '''
    Find a user that matches input user name
    :param username: user name
    :return: user object
    '''
    userinfo = User.query.filter_by(UserName=username).first()
    return userinfo

def PyFind_Token(token):
    '''
    Find a user that matches input user token
    :param token: user token
    :return: user object
    '''
    return User.query.filter_by(Token=token).first()

#@user.route('/find/openid/<openid>')
def PyFind_OpendID(openid):
    '''
    Find a user that matches input user open id
    :param openid: user open id
    :return: user object
    '''
    return User.query.filter_by(OpenID=openid).first()