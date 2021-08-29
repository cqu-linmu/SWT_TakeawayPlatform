import hashlib
import json
import random
import string
import requests

from application import app


class MemberService:

    @staticmethod
    def geneAuthCode(member_info=None):
        '''
        生成验证码
        :param member_info:
        :return:
        '''
        m = hashlib.md5()
        str = "%s-%s-%s" % (member_info.id, member_info.salt, member_info.status)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def geneSalt(length=16):
        '''
        加盐提升秘钥强度
        :param length:
        :return:
        '''
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        # 产生16位随机的数字与字母组成的列表，然后用join拼接成字符串
        return ("".join(keylist))

    @staticmethod
    def getWeChatOpenId(code):
        '''
        从微信平台处获取openid
        :param code:
        :return:
        '''
        url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code" \
            .format(app.config['MINA_APP']['appid'], app.config['MINA_APP']['appkey'], code)
        """
        appid:小程序 appId
        secret:小程序 appSecret
        js_code:登录时获取的 code，前端传过来的code
        """
        r = requests.get(url)  # 根据官网的要求需要发送get请求，获取到响应对象
        res = json.loads(r.text)  # 从中取出内容
        openid = None  # openid:用户唯一标识
        if 'openid' in res:
            openid = res['openid']
        return openid  # 将其当成变量返回
