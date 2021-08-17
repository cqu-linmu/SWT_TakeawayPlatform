from ...DataBase import db

class User(db.Model):
    __tablename__ = 'UserData_ALL'

    #NaturalPerson
    UserID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    UserName = db.Column(db.String(10), nullable=False)
    _Password = db.Column(db.String(20), nullable=False)
    Gender = db.Column(db.INTEGER,nullable=False)

    def SetPassword(self,InputPassword):
        self._Password=InputPassword
        return True

    def CheckPassword(self,InputPassword):
        return InputPassword == self._Password

    #StaticInfo
    HeadPortrait = db.Column(db.String(100),nullable=False)
    Address = db.Column(db.String(50), nullable=False)
    Telephone = db.Column(db.String(20),nullable=False)
    UserBind = db.relationship('UserBind',backref=db.backref('UserMainInfo'))

    #DynamicInfo
    _HaveLogin = db.Column(db.Boolean,default=False)
    UserExtraRelief = db.Column(db.List, default=[])
    HaveOrder = db.Column(db.bool,default=False)
    Orders = db.Column(db.String,default=[])    #String to simulate list, use '/' to divide
    Select = db.Column(db.String,default=[])    #String to simulate list, use '/' to divide

    def Login(self):
        if(not self._HaveLogin):
            self._HaveLogin=not self._HaveLogin

        return not self._HaveLogin

    def Exit(self):
        if(self._HaveLogin):
            self._HaveLogin = not self._HaveLogin

        return self._HaveLogin
