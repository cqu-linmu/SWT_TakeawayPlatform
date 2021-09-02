const API = require("../../utils/api.js").API;

Page({
    /**
     * 页面的初始数据
     */
    data: {
        order_id: 1,
        firstTime: true,
        loading: false,
        totalMoney: 0,
        totalNum: 0,
        shopList: []
    },
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        console.log("装载支付页面");
        console.log("options:", options);

        if (options.postData == undefined) {
            //----------------从购物车读取数据---------------------------
            try {
                var cartData = wx.getStorageSync('cartData')
                this.setData({
                    shopList: cartData,
                    order_id: options.order_id
                })
            } catch (e) {
                console.log("没有找到对应缓存");
            }
            //----------------------------------------------------------
        } else {
            console.log('postdata: ',decodeURIComponent(options.postData));
            let tempData = JSON.parse(decodeURIComponent(options.postData));
            let orderId = JSON.parse(options.order_id);
            console.log(orderId);
            console.log(tempData);
            this.setData({
                shopList: tempData,
                order_id: orderId
            })
        }
    },
    /**
     * 生命周期函数--页面将被展示时调用
     */
    onShow: function () {
        if (this.data.firstTime) {
            this.setData({
                firstTime: false
            })
        } else {
            this.onLoad();
        }

        //计算支付订单总量
        let totalNum = 0,
            totalMoney = 0;
        for (const i in this.data.shopList) {
            const item = this.data.shopList[i];
            totalNum += item.dish_num;
            totalMoney += item.dish_num * item.dish_price;
        }
        this.setData({
            totalNum: totalNum,
            totalMoney: totalMoney
        })
    },
    //跳转到菜品列表
    goHome() {
        wx.switchTab({
            url: '/pages/home/home',
        })
    },
    cancel() {
        wx.navigateBack({
            delta: 0,
        })
    },
    signPay(e) {
        console.log('支付')
    },
    toPay(e) {
        wx.showToast({
            title: 'pay price',
        })
        let data = {
            order_id:this.data.order_id,
            money_amount:this.data.totalMoney
        };
        API.pay(data)
        .then(res=>{
            console.log("支付成功");
        })
        .catch(err=>{
            console.log("支付失败");
        });
        wx.switchTab({
            url: '../../pages/home/home',
        })
    },
})