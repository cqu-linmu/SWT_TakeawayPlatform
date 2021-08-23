from utils.UrlManager import *
from  DataBaseFolder.Models.UserModels.UserBaseInfo import User

# token 检查
def token_check(token):
    user_info = User.query.filter_by(Token=token).first()
    if not user_info:
        return UrlManager.buildUrl("/login")