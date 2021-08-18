from Main import db

#Unknown
#Used in Database Modules, for example, Class User(db.Model,EntityBase)
class EntityBase(object):
    def to_json(self):
        fields = self.__dict__
        if "_sa_instance_state" in fields:
            del fields["_sa_instance_state"]
        return fields

class User(db.Model):
    __tablename__ = 'UserData_ALL'  # 数据库表名

    #NaturalPerson
    ID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    UserName = db.Column(db.String(10), nullable=False)
    Password = db.Column(db.String(20), nullable=False)
    Gender = db.Column(db.INTEGER,nullable=False)

    #StaticInfo
    HeadPortrait = db.Column(db.image,nullable=False)   #Tp, db.image
    Address = db.Column(db.String(50), nullable=False)
    UserBind = db.relationship('UserBind',backref=db.backref('UserMainInfo'))

    #DynamicInfo
    UserExtraRelief = db.Column(db.List, default=[])
    HaveOrder = db.Column(db.bool,index=True,default=False)
    Orders = db.Column(db.List,default=[])
    Select = db.Column(db.List,default=[])

class UserBind(db.Model):
    __tablename__ = 'UserDataBind'

    HaveWechatBind = db.Column(db.Boolean,default=False)
    WechatBind_Name = db.Column(db.String(20),default='')
    WechatBind_Password = db.Column(db.String(20),default='')

class Dish(db.Model):
    __tablename__ = 'OrderData'

    #BaseData
    Picture = db.Column(db.image, nullable=False)
    Description = db.Column(db.String,nullable=False)
    Price = db.Column(db.float,nullable=False)
    SourceRestaurant = db.relationship("Restaurant", back_populates="DishedDisplay")

class Restaurant(db.Model):
    __tablename__ = 'RestaurantData'

    #StaticData
    HeadPortrait = db.Column(db.image, nullable=False)
    Address = db.Column(db.String, nullable=False)
    Dishes = db.relationship("Dish", back_populates="Source")
