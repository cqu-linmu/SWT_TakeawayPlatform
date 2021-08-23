# -*- coding: utf-8 -*-
from flask import Blueprint,request
from utils.UploadService import UploadService
route_upload = Blueprint('upload_page', __name__)

'''
参考文章：https://segmentfault.com/a/1190000002429055
参考视频：同类教学视频 p48
'''

# 上传封面图
@route_upload.route("/pic",methods = [ "GET","POST" ])
def uploadPic():
	file_target = request.files
	upfile = file_target['pic'] if 'pic' in file_target else None  # pic上传图片处传输的信息
	callback_target = 'window.parent.upload'
	if upfile is None:
		return "<script type='text/javascript'>{0}.error('{1}')</script>".format( callback_target,"上传失败" )

	ret = UploadService.uploadByFile(upfile)
	if ret['code'] != 200:
		return "<script type='text/javascript'>{0}.error('{1}')</script>".format(callback_target, "上传失败：" + ret['msg'])

	return "<script type='text/javascript'>{0}.success('{1}')</script>".format(callback_target,ret['data']['file_key'] )
