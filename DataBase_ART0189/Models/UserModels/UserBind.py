from ...DataBase import db

class UserBind(db.Model):
    __tablename__ = 'UserDataBind'

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
