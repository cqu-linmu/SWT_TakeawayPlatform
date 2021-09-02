// pages/personal-center/personal-center.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    isFirst:true,
    user_img: wx.getStorageSync('userInfo').avatarUrl,
    username: wx.getStorageSync('userInfo').nickName,
    user_id: 10086,
    userInfo: {},
    hasUserInfo: false,
    canIUseGetUserProfile: false,
    myOrder: "我的订单",
    myAddress: "我的地址"
  },
  onLoad: function () {
    app.checkout()
    if (wx.getStorageSync('isTokenUseful')) {
      if (wx.getUserProfile) {
        this.setData({
          canIUseGetUserProfile: true
        })
      }
      if (wx.getStorageSync('userInfo')) {
        try {
          var user_info = wx.getStorageSync('userInfo');
          var user_id = wx.getStorageSync('user_id');
          console.log("读取缓存中用户信息成功");
        } catch (e) {
          console.log("读取缓存中用户信息失败");
        }
        this.setData({
          hasUserInfo: true,
          userInfo: user_info,
          user_id: user_id
        })
      } else {
        this.setData({
          hasUserInfo: false
        })
      }
    } else {
      console.log("未授权登录正在前往授权登录页面");
      wx.navigateTo({
        url: '/pages/index/index', //授权页面
      })
    }
  },
  onShow:function() {
    if (!this.data.isFirst) {
      this.onLoad();
    }
    else {
      this.setData({
        isFirst:false
      });
    }
  },
  goLogin: function () {
    wx.redirectTo({
      url: '../../pages/index/index',
    })
  },
  goMyOrder: function () {
    wx.navigateTo({
      url: "../../pages/my-order/my-order?user_id=" + this.data.user_id
    })
  },
  goMyAddress: function () {
    wx.navigateTo({
      url: "../../pages/my-address/my-address?user_id=" + this.data.user_id
    })
  }
})