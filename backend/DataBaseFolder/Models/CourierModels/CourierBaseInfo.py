from DataBaseFolder.DataBase import db

class Courier(db.Model):
    __tablename__ = 'CourierData_ALL'

    #NaturalPerson
    CourierID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    UserName = db.Column(db.String(10), nullable=False)
    _Password = db.Column(db.String(20), nullable=False)
    Gender = db.Column(db.INTEGER,nullable=False)

    def SetPassword(self,InputPassword):
        self._Password=InputPassword
        return True

    def CheckPassword(self,InputPassword):
        return InputPassword == self._Password

    #StaticInfo
    Telephone = db.Column(db.String(20),nullable=False)

    #DynamicInfo
    _HaveLogin = db.Column(db.Boolean, default=False)
    Status = db.Column(db.Enum('空闲中','取餐中','送餐中'),nullable=False)

    def Login(self):
        if (not self._HaveLogin):
            self._HaveLogin = not self._HaveLogin

        return not self._HaveLogin

    def Exit(self):
        if (self._HaveLogin):
            self._HaveLogin = not self._HaveLogin

        return self._HaveLogin
