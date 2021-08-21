from DataBase import db
from Models.UserModels.UserBaseInfo import User
from Models.RestaurantModels.RestaurantBase import Restaurant
from Models.RestaurantModels.DishBase import Dish
from Models.OrderData.OrderBase import Order

def GenericModify(ModifyType, DataID, DataBaseModelName, DataParameterName, NewParameterValue=''):
    '''
    Be careful, please ensure you have input correct parameters\n
    ModifyType 1:Modify 2:Delete\n
    If you want to delete something DataParameterName must be XXXID\n
    Example1 : GenericModify(1,1,User,Telephone,123456)\n
    Example2 : GenericModify(2,1,User,UserID)\n
    '''
    try:
        TargetCommand=''
        ModelName=str(DataBaseModelName)
        QueryID=str(DataID)
        ParamName=str(DataParameterName)
        NewValue=str(NewParameterValue)
        TempVarible=str('Tp_Info')

        if(ModifyType==1):

            TargetCommand='{}={}.query.filter({}.{}=={}).first()'\
                .format(TempVarible,ModelName,ModelName,ParamName,QueryID)+'\n'\
                +'{}.{}={}'.format(TempVarible,ParamName,NewValue)+'\n'\
                +'db.session.merge({})'.format(TempVarible)

        elif(ModifyType==2):

            TargetCommand='{}={}.query.filter({}.{}=={}).delete()'.format(TempVarible,ModelName,ModelName,ParamName,DataID)

        exec(TargetCommand)

        db.session.commit()

        return True
    except BaseException:
        print('Invalid DataBaseModel/ParameterName/Value')

        return False
    else:
        print('Modify Success! No Return Value')

        return False
