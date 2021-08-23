# database config

# start debug mode
DEBUG = True

# sql echo
SQLALCHEMY_ECHO = True

'''
    username = root
    password = 123456
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8"
                .format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

'''

# DataBase url 
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost/testdb"

# sql track modify
SQLALCHEMY_TRACK_MODIFICATIONS = False

# sql encoding
SQLALCHEMY_ENCODING = "utf8"
