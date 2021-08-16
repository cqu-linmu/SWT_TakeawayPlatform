from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#'mysql+pymysql://<username>:<password>@localhost:3306/<db_name>?charset=utf8&auth_plugin=mysql_native_password'
#username = root
#password = 123456
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/forum?charset=utf8"

Engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()