DEBUG = True
SQLALCHEMY_ECHO = True
#username = root
#password = 123456
#SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/TestMySQLServer?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8"
