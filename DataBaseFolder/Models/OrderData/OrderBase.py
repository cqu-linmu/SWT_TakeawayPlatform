from DataBaseFolder.DataBase import db
import datetime
from DataBaseFolder.Models.RestaurantModels.RestaurantBase import Restaurant
from ..ModelsParameter import EntityBase

class Order(db.Model,EntityBase):
    __tablename__ = 'OrderData'

    #StaticData
    OrderID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    OrderTime = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    UserID = db.Column(db.INTEGER, nullable=False)
    Remark = db.Column(db.String(100), nullable=False,default='DefaultPath')
    OrderAddress = db.Column(db.String(50), nullable=False)
    Dishes = db.Column(db.String(500), default='')
    OrderStatus = db.Column(db.Enum('待付款','待发货','待收货','待评价','已完成','已取消'),nullable=False,default='待付款')
    Price = db.Column(db.Float, nullable=False)
    Carriage = db.Column(db.Float, nullable=False)

    SourceRestaurant = db.Column(db.INTEGER, db.ForeignKey('RestaurantData.RestaurantID'))
    SourceUser = db.Column(db.INTEGER, db.ForeignKey('UserData_ALL.UserID'))

    def ConstructOthers(self):
        self.OrderTime = datetime.datetime.now()

    def OrderFinish(self):
        '''
        Call when finish order
        '''
        res = Restaurant.query.get(self.SourceRestaurant)
        res.AddTotalBenefits(self.Price)
