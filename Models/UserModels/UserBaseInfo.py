from DataBase import db
from ..ModelsParameter import EntityBase

class User(db.Model,EntityBase):
    __tablename__ = 'UserData_ALL'

    #NaturalPerson
    UserID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    UserName = db.Column(db.String(10), nullable=False)
    _Password = db.Column(db.String(20), nullable=False)
    Gender = db.Column(db.Enum('男','女','其他','未知'),nullable=False,default='未知')

    def SetPassword(self,InputPassword):
        self._Password=InputPassword
        return True

    def CheckPassword(self,InputPassword):
        return InputPassword == self._Password

    #StaticInfo
    HeadPortrait = db.Column(db.String(100),nullable=False,default='DefaultPath')
    Address = db.Column(db.String(50), nullable=False,default='NeedInit')
    Telephone = db.Column(db.String(20),nullable=False,default='NeedInit')

    #DynamicInfo
    _HaveLogin = db.Column(db.Boolean,default=False)
    UserExtraRelief = db.Column(db.String(100), default='')
    HaveOrder = db.Column(db.Boolean,default=False)
    Orders = db.Column(db.String(200),default='')    #String to simulate list, use '/' to divide
    Select = db.Column(db.String(200),default='')    #String to simulate list, use '/' to divide

    def Login(self):
        if(not self._HaveLogin):
            self._HaveLogin=not self._HaveLogin

        return not self._HaveLogin

    def Exit(self):
        if(self._HaveLogin):
            self._HaveLogin = not self._HaveLogin

        return self._HaveLogin

    #UserBind
    HaveAnyBind = db.Column(db.Boolean,default=False)

    HaveWechatBind = db.Column(db.Boolean,default=False)
    WechatBind_Name = db.Column(db.String(20),default='')
    WechatBind_Password = db.Column(db.String(20),default='')

    HaveQQBind = db.Column(db.Boolean, default=False)
    QQBind_Name = db.Column(db.String(20), default='')
    QQBind_Password = db.Column(db.String(20), default='')

    #Type=0,Bind Wechat;Type=1,Bind QQ
    def BindAny(self,Type,Name,Password):
        if(not self.HaveAnyBind):
            self.HaveAnyBind=True

        BindOut=False
        if(Type==0):
            BindOut=self.BindWechat(Name,Password)
        elif(Type==1):
            BindOut=self.BindQQ(Name,Password)

        return BindOut

    def BindWechat(self,Name,Password):
        self.WechatBind_Name=Name
        self.WechatBind_Password=Password
        self.HaveWechatBind=True

        return True

    def BindQQ(self,Name,Password):
        self.QQBind_Name=Name
        self.QQBind_Password=Password
        self.HaveQQBind=True

        return True

    def UnBindAny(self,Type):
        IfUnBind=True
        if(Type==0):
            self.UnBindWechat()
        elif(Type==1):
            self.UnBindQQ()
        else:
            IfUnBind=False

        self.HaveAnyBind=self.GetBind()

        return IfUnBind

    def GetBind(self):
        return self.HaveQQBind or self.HaveWechatBind

    def UnBindWechat(self):
        self.HaveWechatBind=False

    def UnBindQQ(self):
        self.HaveQQBind=False
