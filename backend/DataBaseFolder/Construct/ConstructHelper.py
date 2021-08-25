import DataBaseFolder.Interface.UserBaseModify as um
import DataBaseFolder.Interface.RestaurantBaseModify as rm
import random


def DataBaseConstruct_ALL(Seed=None, UserNum=100, ResNum=1, DishPerRes=10, OrderPerUser=10, MaxOrderLen=10):
    '''
    DataBase Construct/Init, call all the construct types
    :param Seed: static random seed to immobilize construct data
    :param UserNum:
    :param ResNum:
    :param DishPerRes:
    :param OrderPerUser:
    :param MaxOrderLen:
    :return:
    '''
    random.seed(Seed)
    DataBaseConstruct_User(UserNum)
    DataBaseConstruct_Restaurant(ResNum)
    DataBaseConstruct_Dish(ResNum, DishPerRes)
    DataBaseConstruct_Order(UserNum, DishPerRes, OrderPerUser, MaxOrderLen)


def DataBaseConstructType(Type, Num1, Num2):
    '''
    Choose type you want to Construct
    :param Type: Type: 1,User ; 2,Restaurant ; 3,Dish ; 4,Order
    :param Num1: Type X parameter 1
    :param Num2: Type X parameter 2
    :return:
    '''
    if (Type == 1):
        DataBaseConstruct_User(Num1)
    elif (Type == 2):
        DataBaseConstruct_Restaurant(Num1)
    elif (Type == 3):
        DataBaseConstruct_Dish(Num1, Num2)
    elif (Type == 4):
        DataBaseConstruct_Order(Num1, Num2)
    else:
        return False

    return True


def DataBaseConstruct_User(UserNum):
    '''
    Input UserNum to control UserInfo number
    :param UserNum: user number
    :return: if construct success
    '''
    LastName = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许']
    Name = ['澄邈', '德泽', '海超', '海逸', '海昌', '瀚钰', '瀚文', '涵亮', '涵煦', '明宇', '涵衍', '浩皛', '浩波', '浩博', '浩初', '浩宕', '浩歌',
            '冰真', '白萱', '友安', '海之', '又琴', '天风', '若松', '盼菡', '秋荷', '香彤', '语梦', '惜蕊', '迎彤', '沛白', '雁彬', '雪晴', '诗珊']

    for i in range(UserNum):
        um.PyAdd(LastName[random.randint(0, 19)] + Name[random.randint(0, len(Name) - 1)], 114514)

    return True


def DataBaseConstruct_Restaurant(ResNum):
    '''
    Input ResNum to control UserInfo number
    :param ResNum: restaurant number
    :return: if construct success
    '''
    rm.PyAdd('野兽餐馆', '下北泽')

    return True


def DataBaseConstruct_Dish(ResNum, DishPerRes):
    '''
    From Method and Object to auto construct dishes
    :param ResNum: use restaurant number to limit dishes number
    :param DishPerRes: every restaurant will construct the same
    :return: if construct success
    '''
    Method = ['煮', '炒', '炸', '拌']
    Object = ['苹果', '葡萄', '西瓜', '梨', '桃']

    for i in range(ResNum):
        for j in range(DishPerRes):
            rm.AddDish(i + 1, Method[int(j / 4) % 4] + Object[j % 5], random.randint(10, 100), 1, j % 5, 'pic', 'des')

    return True


def DataBaseConstruct_Order(UserNum, DishPerRes, OrderPerUser, MaxOrderLen):
    '''
    Construct orders from following parameters
    :param UserNum: user number
    :param DishPerRes: every restaurant will construct the same
    :param OrderPerUser: every user will construct this orders
    :param MaxOrderLen: any ordered dishes will be limited to no more than this length
    :return: if construct success
    '''
    res = rm.PyFind_ID(1)
    for i in range(UserNum):
        for j in range(OrderPerUser):
            price = random.randint(20, 100)
            rm.AddOrder(1, i + 1, '', 'Home', RandomDishesInOrder(DishPerRes, MaxOrderLen), price,
                        random.randint(0, 20))
            res.AddTotalBenefits(price)

    return True


def RandomDishesInOrder(DishPerRes, MaxOrderLen):
    '''
    Random dishes generator
    :param DishPerRes: every restaurant will construct the same
    :param MaxOrderLen: any ordered dishes will be limited to no more than this length
    :return: if construct success
    '''
    Tp_OrderLen = MaxOrderLen - random.randint(0, DishPerRes - 1)
    DishesStr = ''
    for i in range(Tp_OrderLen):
        DishesStr += str(random.randint(1, DishPerRes)) + '|' + str(random.randint(1, 10)) + '/'

    return DishesStr
