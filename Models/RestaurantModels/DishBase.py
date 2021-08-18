from DataBase import db

class Dish(db.Model):
    __tablename__ = 'OrderData'

    #BaseData
    DishID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    DishName = db.Column(db.String(10), nullable=False)
    Picture = db.Column(db.String(50), nullable=False,default='DefaultPath')
    Description = db.Column(db.String(500),nullable=False,default='None')
    Price = db.Column(db.Float,nullable=False)
    #SourceRestaurant = db.relationship("Restaurant", back_populates="DishedDisplay")