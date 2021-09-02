// pages/dish/dish.js
const API = require("../../utils/api.js").API;
const app = getApp()
Page({

    /**
     * 页面的初始数据
     */
    data: {
        order_id: 1,
        dish_id: 0,
        dish_name: "",
        dish_img: "",
        dish_price: 0,
        dish_sold: 0,
        dish_score: 0,
        dish_num: 0
    },
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        let id = options.dish_id; //传递进来的菜品ID
        console.log("dish_id", id);
        parseInt(id);
        let data = {
            dish_id: id
        }
        API.getDishDetail(data)
            .then(res => {
                console.log("请求菜品详情的返回", res);
                this.setData({
                    dish_id: id,
                    dish_img: res.data.dish_img,
                    dish_name: res.data.dish_name,
                    dish_price: res.data.dish_price,
                    dish_score: res.data.dish_score,
                    dish_sold: res.data.dish_sold,
                    dish_num: 1
                });
            })
            .catch(err => {
                //请求失败
                console.log("请求失败");
                console.log(err);
            });
    },
    onShow: function () {
        let pages = getCurrentPages();
        let options = pages[pages.length - 1].options;
        console.log(options);
        // let data_params = Sting.parse(options.data_params);
        let id = options.dish_id; //传递进来的菜品ID
        parseInt(id);
        console.log("dish_id", id);
        let data = {
            dish_id: id
        }
        API.getDishDetail(data)
            .then(res => {
                this.setData({
                    dish_id: id,
                    dish_img: res.data.dish_img,
                    dish_name: res.data.dish_name,
                    dish_price: res.data.dish_price,
                    dish_score: res.data.dish_score,
                    dish_sold: res.data.dish_sold,
                    dish_num: 1
                });
            })
            .catch(err => {
                //请求失败
                console.log("请求失败");
                console.log(err);
            });
    },
    //输入选择数量
    input_number: function (e) {
        let value = this.validateNumber(e.detail.value)
        console.log(e.detail.value)
        this.setData({
            number: parseInt(value) //parseInt将数字字符串转换成数字
        })
    },
    validateNumber(val) {
        return val.replace(/\D/g, '') //正则表达式指定字符串只能为数字
    },
    //购买减一按钮函数
    sub_button: function () {
        if (this.data.dish_num <= 0) {
            this.setData({
                dish_num: 0
            })
        } else {
            this.setData({
                dish_num: this.data.dish_num - 1
            })
        }
    },
    //购买加一按钮函数
    add_button: function () {
        var value = this.data.dish_num
        this.setData({
            dish_num: value + 1
        })
    },
    // 跳到购物车
    toCart() {
        wx.switchTab({
            url: '../../pages/shopCart/shopCart'
        })
    },
    // 添加菜品到购物车
    addToCar() {
        // console.log(cartData);
        wx.showToast({
            title: '添加购物车成功',
            icon: 'success',
            duration: 2000
        });
        try {
            var cartData = wx.getStorageSync('cartData')
            console.log("从缓存中读取的购物车数据：", cartData);
            console.log(this.data);
            var index = -1;
            for (const i in cartData) {
                const item = cartData[i];
                if (this.dish_id == item.dish_id) {
                    index = i;
                    break;
                }
            }
            if (index == -1) {
                cartData.push({
                    dish_id: this.data.dish_id,
                    dish_img: this.data.dish_img,
                    dish_name: this.data.dish_name,
                    dish_price: this.data.dish_price,
                    dish_num: this.data.dish_num
                })
            } else {
                cartData[index].dish_num += this.dish_num;
            }
            try {
                wx.setStorageSync("cartData", cartData);
                console.log("订单信息：", cartData);
                console.log("订单写入缓存");
            } catch (e) {
                console.log("上传缓存失败");
            }
        } catch (e) {
            console.log("没有找到对应缓存");
        }
        try {
            const res = wx.getStorageInfoSync()
            console.log("目前占有大小:", res.currentSize)
            console.log("总大小:", res.limitSize)
        } catch (e) {
            console.log("获取当前缓存信息失败");
        }
        //跳转到菜品列表页
        wx.navigateBack({
            delta: 0,
        })
    },
    // 立即购买
    immeBuy() {
        app.checkout()
        if (wx.getStorageSync('isTokenUseful')) {
            let data = {
                user_id: wx.getStorageSync("user_id"),
                dish_data: [{
                    dish_id: this.data.dish_id,
                    dish_num: this.data.dish_num
                }]
            };
            API.submitOrder(data)
                .then(res => {
                    wx.showToast({
                        title: '提交订单成功',
                        icon: 'success',
                        duration: 2000
                    });
                    this.setData({
                        order_id: res.data.order_id
                    })
                    console.log(this.data.dish_img);
                    var postData = [{
                        dish_id: this.data.dish_id,
                        dish_img: this.data.dish_img,
                        dish_name: this.data.dish_name,
                        dish_price: this.data.dish_price,
                        dish_num: this.data.dish_num
                    }];
                    console.log(this);
                    // var postDataJsonString =  JSON.stringify(postData)
                    // console.log(postDataJsonString);
                    wx.navigateTo({
                        url: '../../pages/pay/pay?postData=' + encodeURIComponent(JSON.stringify(postData)) + "&order_id=" + this.data.order_id,
                    })
                })
                .catch(err => {
                    console.log("提交订单失败");
                });
        } else {
            console.log("未授权登录正在前往授权登录页面");
            wx.navigateTo({
                url: '/pages/index/index', //授权页面
            })
        }
    },
})