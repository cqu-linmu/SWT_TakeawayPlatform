// app.js
const API = require("/utils/api.js").API;
App({
  onLaunch() {
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
    wx.setStorageSync('isTokenUseful',false)
  },
  //检验code
  checkout: function () {
    wx.checkSession({
      success: function () {
        //session_key 未过期，并且在本生命周期一直有效
        console.log("未过期", wx.getStorageSync('token'));
        wx.setStorageSync('isTokenUseful',true);
      },
      fail: function () {
        //session_key 已经失效，需要重新执行登录流程
        console.log("过期了", wx.getStorageSync('token'));
        wx.setStorageSync('isTokenUseful',false);
      }
    })
  },
  //检验授权的方法
  getSettings: function () {
    let that = this
    wx.getSetting({
      success: (res) => {
        if (res.authSetting['scope.userInfo']) { //授权了，可以获取用户信息了
          console.log("已经授权获取用户信息");
        } else { //未授权，跳到授权页面
          console.log("未授权获取用户信息");
          wx.redirectTo({
            url: '/pages/index/index', //授权页面
          })
        }
      }
    })
  },
  globalData: {
    userInfo: "", //用户信息
    user_id: "", //登录用户的唯一标识
    appid: '', //appid
    AppSecret: '', //secret秘钥
    token: ''
  },
  onHide: function () { //小程序退出时触发的事件
    console.log("小程序完全退出了")
  }
})