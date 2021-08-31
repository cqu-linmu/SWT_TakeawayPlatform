# database config

DEBUG = True
SQLALCHEMY_ECHO = True

# username = root
# password = 123456

# SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:132132@localhost:3306/testdb"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8"

# 过滤url
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]

# cookie名
AUTH_COOKIE_NAME = "Bearer"


# appid wx5a2a890bf53067c5
# appsecret 52d0e43d04372be26b5cd201b64bb312

# 后台上面改秘钥的密码 swtcqu123
MINA_APP = {
    'appid': 'wx5a2a890bf53067c5',
    'appkey': '52d0e43d04372be26b5cd201b64bb312'
}
