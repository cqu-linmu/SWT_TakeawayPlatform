from DataBaseFolder.DataBase import db
from DataBaseFolder.Interface.UserBaseModify import *
from DataBaseFolder.Interface.RestaurantBaseModify import *
from DataBaseFolder.Interface.DishBaseModify import *
from DataBaseFolder.Interface.OrderBaseModify import *

def GenericModify(ModifyType, DataID, DataBaseModelName, DataParameterName='', NewParameterValue=''):
    '''
    Be careful, please ensure you have input correct parameters\n
    ModifyType 1:Modify 2:Delete 3:MultiModify\n
    If you want to delete something DataParameterName must be XXXID\n
    If use multi modify, parameter names and values must be matched\n
    If use any string value, add additional ' and \\\ \n
    Example1 : GenericModify(1,1,User,Telephone,123456)\n
    Example2 : GenericModify(2,1,User)\n
    Example3 : GenericModify(3,1,'User',['Gender','Address'],['\'男\'','\'下北泽\''])\n
    '''
    try:
        TargetCommand = ''
        ModelName = str(DataBaseModelName)
        QueryID = str(DataID)
        ParamName = str(DataParameterName)
        NewValue = str(NewParameterValue)
        TempVarible = str('Tp_Info')

        if (ModifyType == 1):

            TargetCommand = '{}={}.query.get({})' \
                                .format(TempVarible, ModelName, QueryID) + '\n' \
                            + '{}.{}={}'.format(TempVarible, ParamName, NewValue) + '\n' \
                            + 'db.session.merge({})'.format(TempVarible)

        elif (ModifyType == 2):
            TargetCommand = '{}={}.query.get({})'.format(TempVarible, ModelName, QueryID) + '\n' \
                            + 'db.session.delete({})'.format(TempVarible)

        elif (ModifyType == 3):

            TargetCommand = '{}={}.query.get({})'.format(TempVarible, ModelName, QueryID)
            exec(TargetCommand)

            for i in range(len(DataParameterName)):
                TargetCommand = '{}.{}={}'.format(TempVarible, DataParameterName[i], NewParameterValue[i])
                exec(TargetCommand)

            TargetCommand = 'db.session.merge({})'.format(TempVarible)

        else:
            print('Modify Failed! No matched modify type!')

            return False

        exec(TargetCommand)

        db.session.commit()

        return True
    except BaseException:
        print('Invalid DataBaseModel/ParameterName/Value')

        return False

