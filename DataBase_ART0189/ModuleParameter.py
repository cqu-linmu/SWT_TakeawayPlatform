# models.py

from sqlalchemy import Column, String

from DataBaseEngine import Base, Engine


class User(Base):
    __tablename__ = 'UserData_ALL'  # 数据库表名

    ID = Column(int, primary_key=True, autoincrement=True)
    UserName = Column(String(255), nullable=False)
    hash_pwd = Column(String(255), nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(Engine)