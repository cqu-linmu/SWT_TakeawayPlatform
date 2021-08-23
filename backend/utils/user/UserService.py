# -*- coding: utf-8 -*-
# 此文件用于封装用户登录相关的方法
# geneAuthCode:生成授权码
# genePwd：根据用户登录密码和
# geneSalt:生成salt
#
import hashlib,base64,random,string

class UserService():

    # 生成授权码
    @staticmethod
    def geneAuthCode(user_info = None ):
        m = hashlib.md5()
        str = "%s-%s-%s" % (user_info.UserID, user_info.UserName, user_info._Password)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    # 根据登录密码和salt生成唯一的密钥，用于登录
    @staticmethod
    def genePwd( pwd,salt):
        m = hashlib.md5()
        str = "%s-%s" % ( base64.encodebytes( pwd.encode("utf-8") ) , salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    # 生成salt，用于上述方法
    @staticmethod
    def geneSalt( length = 16 ):
        keylist = [ random.choice( ( string.ascii_letters + string.digits ) ) for i in range( length ) ]
        return ( "".join( keylist ) )
