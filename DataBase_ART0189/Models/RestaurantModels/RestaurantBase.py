from ...DataBase import db

class Restaurant(db.Model):
    __tablename__ = 'RestaurantData'

    #StaticData
    RestaurantID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    RestaurantName = db.Column(db.String(10), nullable=False)
    HeadPortrait = db.Column(db.String(100), nullable=False)
    Address = db.Column(db.String(50), nullable=False)
    Description = db.Column(db.String(500), nullable=False)

    #DynamicData
    Dishes = db.Column(db.String(), nullable=True)
