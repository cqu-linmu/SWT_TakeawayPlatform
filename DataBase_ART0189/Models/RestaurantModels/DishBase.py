from ...DataBase import db

class Dish(db.Model):
    __tablename__ = 'OrderData'

    #BaseData
    DishID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    DishName = db.Column(db.String(10), nullable=False)
    Picture = db.Column(db.image, nullable=False)
    Description = db.Column(db.String(500),nullable=False)
    Price = db.Column(db.float,nullable=False)
    SourceRestaurant = db.relationship("Restaurant", back_populates="DishedDisplay")