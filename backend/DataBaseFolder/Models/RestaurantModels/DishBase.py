from DataBaseFolder.DataBase import db
from ..ModelsParameter import EntityBase

class Dish(db.Model, EntityBase):
    __tablename__ = 'DishData'

    # BaseData
    DishID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    DishName = db.Column(db.String(10), nullable=False)
    DishType = db.Column(db.INTEGER, default=False)
    DishTag = db.Column(db.String(100))
    Thumbnail = db.Column(db.String(500), nullable=False, default='DefaultPath')
    Details_Picture = db.Column(db.String(500), nullable=False)
    Description = db.Column(db.String(500), nullable=False)
    Price = db.Column(db.Float, nullable=False)
    Sold = db.Column(db.INTEGER, nullable=False, default=0)
    Shared = db.Column(db.INTEGER, nullable=False, default=0)
    Score = db.Column(db.Float, nullable=False, default=0)

    def IncreaseSelf_Sold(self):
        self.Sold += 1
        return True

    def Add_Sold(self, NewSold):
        self.Sold += NewSold
        return True

    def IncreaseSelf_Shared(self):
        self.Shared += 1
        return True

    def Add_Shared(self, NewShared):
        self.Shared += NewShared
        return True

    SourceRestaurant = db.Column(db.INTEGER, db.ForeignKey('RestaurantData.RestaurantID'))
