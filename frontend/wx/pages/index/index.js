const API = require("../../utils/api.js").API;
const app = getApp();

Page({
    data: {
        code: 1,
        userInfo: {},
        hasUserInfo: false,
        canIUseGetUserProfile: false,
    },

    onLoad: function () {
        if (wx.getUserProfile) {
            this.setData({
                canIUseGetUserProfile: true
            })
        }
    },
    bindGetUserProfile: function () {
        wx.login({
            success: res => {
                console.log("登录后获取的code：", res);

                // 发送 res.code 到后台换取 openId, sessionKey, unionId
                if (res.code) {
                    console.log('code', res.code)
                    this.setData({
                        code: res.code
                    });
                };
                wx.setStorageSync('isTokenUseful',true);
            }
        });
        wx.getUserProfile({
            lang: "zh_CN",
            desc: '用于完善会员资料', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
            //点击的“允许”
            success: (res) => {
                this.setData({
                    userInfo: res.userInfo,
                    hasUserInfo: true
                });
                wx.setStorageSync('userInfo', res.userInfo) // 存储用户信息
                //完成后端登录，并向后端传递信息
                let data = {
                    code: this.data.code,
                    nickName: this.data.userInfo.nickName,
                    avatarUrl: this.data.userInfo.avatarUrl,
                    gender: this.data.userInfo.gender,
                    country: this.data.userInfo.country,
                    province: this.data.userInfo.province,
                    city:this.data.userInfo.city,
                }
                API.login(data).
                then((res) => {
                    wx.setStorageSync('user_id', res.data.user_id);
                    wx.setStorageSync('token', res.data.token);
                }).
                catch((err) => {
                    console.log(err)
                })
                wx.navigateBack({
                  delta: 0,
                })
                wx.showToast({
                    title: '登录成功',
                    icon: 'success',
                    duration: 2000
                });
                // wx.switchTab({
                //     url: '../../pages/home/home', // 个人中心页面为my，名字随便起
                // })
            },
            //点击的“拒绝”
            fail: (err) => {
                wx.showModal({
                    title: '警告',
                    content: '您点击了拒绝授权，将无法进入小程序，请授权之后再进入!!!',
                    showCancel: false,
                    confirmText: '返回授权',
                    success: function (res) {
                        if (res.confirm) {}
                    }
                })
            }
        })
    }
})