import DataBaseFolder.Interface.UserBaseModify as um
import DataBaseFolder.Interface.RestaurantBaseModify as rm
import DataBaseFolder.Interface.DishBaseModify as dm
import random
import string
import datetime

def DataBaseConstruct_ALL(Seed=None, UserNum=100, ResNum=1, DishPerRes=10, OrderPerUser=10, MaxOrderLen=10,
                          OrderDateLen=100):
    '''
    DataBase Construct/Init, call all the construct types
    :param Seed: static random seed to immobilize construct data
    :param UserNum: user number
    :param ResNum: restaurant number
    :param DishPerRes: every restaurant has how many dishes
    :param OrderPerUser: every user payed how many orders
    :param MaxOrderLen: dishes upper limit in every order
    :param OrderDateLen: order date range, in days
    :return: void
    '''
    random.seed(Seed)
    DataBaseConstruct_User(UserNum)
    DataBaseConstruct_Restaurant(ResNum)
    DataBaseConstruct_Dish(ResNum,DishPerRes)
    DataBaseConstruct_Order(UserNum,DishPerRes,OrderPerUser,MaxOrderLen,OrderDateLen)

def DataBaseConstructType(Type,Num1,Num2):
    '''
    Choose type you want to Construct
    :param Type: Type: 1,User ; 2,Restaurant ; 3,Dish ; 4,Order
    :param Num1: Type X parameter 1
    :param Num2: Type X parameter 2
    :return:
    '''
    if(Type==1):
        DataBaseConstruct_User(Num1)
    elif(Type==2):
        DataBaseConstruct_Restaurant(Num1)
    elif(Type==3):
        DataBaseConstruct_Dish(Num1,Num2)
    elif(Type==4):
        DataBaseConstruct_Order(Num1,Num2)
    else:
        return False

    return True

def DataBaseConstruct_User(UserNum):
    '''
    Input UserNum to control UserInfo number
    :param UserNum: user number
    :return: if construct success
    '''
    LastName=['赵','钱','孙','李','周','吴','郑','王','冯','陈','褚','卫','蒋','沈','韩','杨','朱','秦','尤','许']
    Name=['澄邈','德泽','海超','海逸','海昌','瀚钰','瀚文','涵亮','涵煦','明宇','涵衍','浩皛','浩波','浩博','浩初','浩宕','浩歌',
          '冰真','白萱','友安','海之','又琴','天风','若松','盼菡','秋荷','香彤','语梦','惜蕊','迎彤','沛白','雁彬','雪晴','诗珊']
    GenderList=['男','女','其他']

    for i in range(UserNum):
        TpUserInfo=um.PyAdd(LastName[random.randint(0,19)]+Name[random.randint(0,len(Name)-1)],114514)
        TpUserInfo.Gender=GenderList[random.randint(0,2)]
        TpUserInfo.Telephone=RandomTelephone()
        TpUserInfo.SetPassword(RandomPwd())
        TpUserInfo.Address=RandomAddress()

    return True

def RandomTelephone():
    '''
    Random telephone generator
    :return: telephone
    '''
    TeleBegin=[134,135,136,137,138,139,147,150,151,152,157,158,159,172,178,182,183,184,187,188,195,197,198,
               130,131,132,145,155,156,166,175,176,185,186,196,
               133,149,153,180,181,189,173,177,190,191,193,199]
    TpTele=''
    TpTele+=str(TeleBegin[random.randint(0,len(TeleBegin)-1)])
    for i in range(8):
        TpTele+=string.digits[random.randint(0,9)]

    return TpTele

def RandomPwd():
    '''
    Random password generator
    :return: password
    '''
    TpPwd=''
    for i in range(20):
        TpSelect=random.randint(0,3)
        if(TpSelect==0):
            TpPwd+=string.digits[random.randint(0,9)]
        elif(TpSelect==1):
            TpPwd+=string.ascii_lowercase[random.randint(0,25)]
        elif(TpSelect==2):
            TpPwd+=string.ascii_uppercase[random.randint(0,25)]
        else:
            TpPwd+=string.punctuation[random.randint(0,30)]

    return TpPwd

def RandomAddress():
    '''
    Random address generator
    :return: address
    '''
    AddressBegin=['鸿恩怡园','万科金色悦城','富州新城','溯源居','天骄俊园']
    TpAddress='{}{}栋{}-{}'.format(str(AddressBegin[random.randint(0,4)]),str(random.randint(1,8)),
                                               str(random.randint(1,31)),str(random.randint(1,10)))

    return TpAddress

def DataBaseConstruct_Restaurant(ResNum):
    '''
    Input ResNum to control UserInfo number
    :param ResNum: restaurant number
    :return: if construct success
    '''
    rm.PyAdd('野兽餐馆','下北泽')
    um.PyAdd('野兽餐馆','1919810','男','ResNA','下北泽')

    return True

def DataBaseConstruct_Dish(ResNum,DishPerRes):
    '''
    From Method and Object to auto construct dishes
    :param ResNum: use restaurant number to limit dishes number
    :param DishPerRes: every restaurant will construct the same
    :return: if construct success
    '''
    Method=['煮','炒','炸','拌']
    Object=['苹果','葡萄','西瓜','梨','桃']

    for i in range(ResNum):
        for j in range(DishPerRes):
            TpDishInfo=rm.PyAddDish(i+1,Method[int(j/4)%4]+Object[j%5],random.randint(10,100),random.randint(1,3),j%5,'pic','des')
            TpDishInfo.Score=random.random()
            TpDishInfo.Add_Shared(random.randint(100,5000))
            TpDishInfo.Thumbnail=RandomDishPicture(j)
            TpDishInfo.Details_Picture=RandomDishPicture(j)
            TpDishInfo.DishName=RewriteDishName(j)
            TpDishInfo.Description=RandomDishADJ()+TpDishInfo.DishName

    return True

def RewriteDishName(index):
    '''
    Rewrite dish name
    :param index: dish index
    :return: new dish name
    '''
    DishName=['羊肉串','黑椒牛排','烤羊腿','香烤鸡胸','牛肉汉堡','蔬菜沙拉','香烤韭菜','熔岩蛋糕','鲜榨橙汁','茉莉花茶']

    return DishName[index]

def RandomDishADJ():
    '''
    Random dish adj generator
    :return: adj str
    '''
    Adj=['好吃的','美味的','可口的','爽口的','精致的']

    return Adj[random.randint(0,4)]

def RandomDishPicture(index):
    '''
    Random dish picture generator
    :param index: dish index
    :return: picture url
    '''
    PicUrl=['https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi2.chuimg.com%2F74ff11e14fa64672b79e14bc94916cdf_960w_1200h.jpg%3FimageView2%2F2%2Fw%2F600%2Finterlace%2F1%2Fq%2F90&refer=http%3A%2F%2Fi2.chuimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1632707496&t=9013abdaa584b8a872725d55f1cb250b',
            'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg1.juimg.com%2F180428%2F330807-1P42Q11Q478.jpg&refer=http%3A%2F%2Fimg1.juimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1632707542&t=7e2bce4a8463150a8beac3b94cfd544d',
            'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FaGIwf2s2RWlb7g8wUwh1MOpfxH9VHQ8yF1aJ6nbD8GgdWSJCWibre4GO4iczx5yspNWIHJrc0Hib5gsWsNiavmibS8w%2F0%3Fwx_fmt%3Djpeg&refer=http%3A%2F%2Fmmbiz.qpic.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1632707633&t=6df01d20656e0807c059fe9418713c7e',
            'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.yzcdn.cn%2Fupload_files%2F2016%2F10%2F03%2FFuMPuI52icSRQcS7UXjGWLtp05Pt.jpg%21730x0.jpg&refer=http%3A%2F%2Fimg.yzcdn.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1632707686&t=3837b9f183cb936c1f2742648868c8a6',
            'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg1.juimg.com%2F150629%2F330451-15062Z9493478.jpg&refer=http%3A%2F%2Fimg1.juimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1632707714&t=a07dcfe93ac4ea3dace4a1d6a6681f0c',
            'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.168mh.com%2Fwp-content%2Fuploads%2F2019%2F04%2F630e48a5bc6b2c8.jpg&refer=http%3A%2F%2Fwww.168mh.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1632707584&t=67ee122f27bc7b1694260896a05f7383',
            'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fphoto.tuchong.com%2F15841554%2Ff%2F404873370.jpg&refer=http%3A%2F%2Fphoto.tuchong.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1632707734&t=40f930aa10fe1e171d37a623bb08e54f',
            'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.liansuo.com%2Fhtml%2Fimages%2F20160113%2Fcom_14526643427254.jpg&refer=http%3A%2F%2Fimg.liansuo.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1632707762&t=2515bf03b641b96cc5fdd49744d2ad84',
            'https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20170729%2Fbe68d826bde84ee09b41e16fe9e685a4.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1632707781&t=74f88dfc91e6b42bee4c8d47a547bd1d',
            'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.xplian.net%2FtuxpJDEwLmFsaWNkbi5jb20vaTMvMjA4OTcwOTY3OS9UQjI5Nk5QYzJmTThLSmpTWlBmWFhia2xYWGFfISEyMDg5NzA5Njc5JDk.jpg&refer=http%3A%2F%2Fwww.xplian.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1632707809&t=6ceee7f13b31a04b13d4de6ce0542bed']

    return PicUrl[index]

def DataBaseConstruct_Order(UserNum,DishPerRes,OrderPerUser,MaxOrderLen,OrderDateLen):
    '''
    Construct orders from following parameters
    :param UserNum: user number
    :param DishPerRes: every restaurant will construct the same
    :param OrderPerUser: every user will construct this orders
    :param MaxOrderLen: any ordered dishes will be limited to no more than this length
    :return: if construct success
    '''
    res=rm.PyFind_ID(1)
    for i in range(UserNum):
        for j in range(OrderPerUser):
            price=random.randint(20,100)
            orderinfo=rm.PyAddOrder(1,random.randint(1,UserNum),'','Home',RandomDishesInOrder(DishPerRes,MaxOrderLen),price,random.randint(0,20))
            res.AddTotalBenefits(price)
            RandomOrdersDate(orderinfo,i*OrderPerUser+j+1,OrderDateLen,UserNum*OrderPerUser)
            RandomOrderStatus(orderinfo)
            RandomOrderRemark(orderinfo)
            TpUserInfo=um.PyFind_ID(orderinfo.UserID)
            orderinfo.OrderAddress=TpUserInfo.Address

    return True

def RandomOrderRemark(OrderObj):
    '''
    Random order remark generator
    :param OrderObj: order object
    :return: void
    '''
    RemarkList=['无','加辣','不要辣','加饭','加菜','不要葱','不要芹菜','不要折耳根']
    RemarkStr=''
    if(random.randint(0,1)):
        if (random.randint(0, 1)):
            RemarkStr+=RemarkList[random.randint(1,2)]+' '

        RemarkLen=random.randint(1,4)
        RemarkPreStrIndex=random.sample(range(3,7),RemarkLen)
        for i in range(len(RemarkPreStrIndex)):
            RemarkStr+=RemarkList[RemarkPreStrIndex[i]]+' '
    else:
        RemarkStr=RemarkList[0]

    OrderObj.Remark=RemarkStr

def RandomOrdersDate(OrderObj,OrderIndex,OrderDateLen,TotalOrder):
    '''
    Random order date generator
    :param OrderObj: order object
    :param OrderIndex: order index in time
    :param OrderDateLen: max generate length
    :param TotalOrder: order number
    :return: if construct success
    '''

    OrdersPerDay=TotalOrder/OrderDateLen
    RandomDay=OrderObj.OrderTime.__getattribute__('day')-int(OrderDateLen-OrderIndex/OrdersPerDay)
    RandomMonth=OrderObj.OrderTime.month+int(RandomDay/30)

    while(True):
        if(RandomDay<=0):
            RandomDay+=30
        elif(RandomDay>30):
            RandomDay-=30
        else:
            break

    HourInterval=24/OrdersPerDay
    RandomHourLowerLimit=(OrderIndex % OrdersPerDay) * HourInterval
    RandomTime= RandomHourLowerLimit + random.random() * HourInterval
    RandomHour=int(RandomTime)
    RandomMinute=int((RandomTime-RandomHour)*60)

    OrderObj.OrderTime = datetime.datetime.strptime\
        ('{}-{}-{} {}:{}:{}'
         .format(OrderObj.OrderTime.year,RandomMonth,RandomDay,RandomHour,RandomMinute,random.randint(0,59)),
         '%Y-%m-%d %H:%M:%S')

def RandomOrderStatus(OrderObj):
    '''
    Random status generator
    :param OrderObj: order object
    :return: void
    '''
    StatusEnum=['待付款','待发货','待收货','待评价','已完成','已取消']
    OrderObj.OrderStatus=StatusEnum[random.randint(0,5)]

def RandomDishesInOrder(DishPerRes,MaxOrderLen):
    '''
    Random dishes generator
    :param DishPerRes: every restaurant will construct the same
    :param MaxOrderLen: any ordered dishes will be limited to no more than this length
    :return: if construct success
    '''
    Tp_OrderLen=MaxOrderLen-random.randint(0,DishPerRes-1)
    DishesStr=''
    for i in range(Tp_OrderLen):
        TpDishID=random.randint(1,DishPerRes)
        TpDishNum=random.randint(1,10)
        DishesStr+=str(TpDishID)+'|'+str(TpDishNum)+'/'
        dm.PyFind_ID(TpDishID).Add_Sold(TpDishNum)

    return DishesStr
