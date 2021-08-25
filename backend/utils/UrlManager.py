# -*- coding: utf-8 -*-
"""
作用：封装各种生成url的方法
buildUrl:传入path，生成path
buildStaticUrl：传入path，返回静态url，
buildImageUrl：生成上传图片的存放地址，传入path，生成图片存储的URL
"""

import time
from application import app


class UrlManager(object):
    def __init__(self):
        pass

    # 生成url
    @staticmethod
    def buildUrl(path):
        return path

    # 生成静态地址
    @staticmethod
    def buildStaticUrl(path):
        release_version = app.config.get('RELEASE_VERSION')
        ver = "%s" % (int(time.time())) if not release_version else release_version
        path = "/static" + path + "?ver=" + ver
        return UrlManager.buildUrl(path)

    # 生成图片上传后存放的地址
    @staticmethod
    def buildImageUrl(path):
        app_config = app.config['APP']
        url = app_config['domain'] + app.config['UPLOAD']['prefix_url'] + path
        return url
