from DataBaseFolder.DataBase import db
from ..ModelsParameter import EntityBase


class Restaurant(db.Model, EntityBase):
    __tablename__ = 'RestaurantData'

    # StaticData
    RestaurantID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    RestaurantName = db.Column(db.String(10), nullable=False)
    HeadPortrait = db.Column(db.String(100), nullable=False, default='DefaultPath')
    Address = db.Column(db.String(50), nullable=False)
    Description = db.Column(db.String(500), nullable=False, default='None')
    Benefits = db.Column(db.String(1000), nullable=False, default='')
    OrderNum = db.Column(db.String(1000), nullable=False, default='')

    # DynamicData
    TotalBenefits = db.Column(db.Float, nullable=False, default=0)
    Dishes = db.relationship("Dish", backref='RestaurantData')
    Orders = db.relationship('Order', backref='RestaurantData')

    def AddTotalBenefits(self, NewBenefits):
        self.TotalBenefits += NewBenefits
        return self.Benefits
