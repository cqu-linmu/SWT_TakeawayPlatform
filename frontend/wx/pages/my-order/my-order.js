const API = require("../../utils/api.js").API;
Page({
 
  /**
   * 页面的初始数据
   */
  data: {
    user_id:wx.getStorageSync("user_id"),
    currtab: 0,
    swipertab: [{ name: '待付款', index: 0 },{ name: '待收货', index: 1 },{ name: '待评价', index: 2 },{ name: '已完成', index: 3 } , { name: '已取消', index: 4 }],
  },
 
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
 
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    // 页面渲染完成
    this.getDeviceInfo()
    this.orderShow()
  },
 
  getDeviceInfo: function () {
    let that = this
    wx.getSystemInfo({
      success: function (res) {
        that.setData({
          deviceW: res.windowWidth,
          deviceH: res.windowHeight
        })
      }
    })
  },
 
  /**
  * @Explain：选项卡点击切换
  */
  tabSwitch: function (e) {
    var that = this
    if (this.data.currtab === e.target.dataset.current) {
      return false
    } else {
      that.setData({
        currtab: e.target.dataset.current
      })
    }
  },
 
  tabChange: function (e) {
    this.setData({ currtab: e.detail.current });
    console.log("currtab:",this.data.currtab);
    this.orderShow();
  },
 
  orderShow: function () {
    let that = this
    switch (this.data.currtab) {
      case 0:
        that.waitPayShow()
        break
      case 1:
        that.waitDeliShow()
        break
      case 2:
        that.waitCommShow()
        break
      case 3:
        that.alreadyShow()
        break
      case 4:
        that.lostShow()
        break
    }
  },
  waitPayShow:function(){
    let data = {
      user_id:wx.getStorageSync("user_id"),
      status_req:"待付款"
    };
    API.getOrderList(data)
    .then(res=>{
      this.setData({
        waitPayOrder: res.data,
      })
    })
    .catch(err=>{
      console.log("调用接口失败");
    });  
  },
  waitDeliShow:function(){
    let data = {
      user_id:this.data.user_id,
      status_req:"待收货"
    };
    API.getOrderList(data)
    .then(res=>{
      this.setData({
        waitDeliOrder: res.data,
      })
    })
    .catch(err=>{
      console.log("调用接口失败");
    }); 
  },
  alreadyShow: function(){
    let data = {
      user_id:this.data.user_id,
      status_req:"已完成"
    };
    API.getOrderList(data)
    .then(res=>{
      this.setData({
        alreadyOrder: res.data,
      })
    })
    .catch(err=>{
      console.log("调用接口失败");
    }); 
  },
  waitCommShow:function(){
    let data = {
      user_id:this.data.user_id,
      status_req:"待评价"
    };
    API.getOrderList(data)
    .then(res=>{
      this.setData({
        waitCommOrder: res.data,
      })
    })
    .catch(err=>{
      console.log("调用接口失败");
    }); 
  },
  lostShow: function () {
    console.log("已调用lostShow");
    let data = {
      user_id:this.data.user_id,
      status_req:"已取消"
    };
    API.getOrderList(data)
    .then(res=>{
      this.setData({
        lostOrder: res.data,
      })
    })
    .catch(err=>{
      console.log("调用接口失败");
    }); 
  },
  //响应取消订单按钮
  cancelOrder:function(event) {
    let data = {
      order_id:event.target.dataset.id
    }
    API.cancelOrder(data)
    .then(res=>{
      console.log("取消订单成功");
      this.orderShow();
    })
    .catch(err=>{
      console.log("取消订单失败");
    });
  },
  receive:function (event) {
    let data = {
      order_id:event.target.dataset.id
    }
    API.receiveOrder(data)
    .then(res=>{
      console.log("确认收货成功");
      this.orderShow();
    })
    .catch(err=>{
      console.log("确认收货失败");
    });
  },
  goPay:function(event) {
    let data = event.currentTarget.dataset.data;
    console.log("data:",data);
    let postData = [];
    for (const i in data.dish_data) {
        const item = data.dish_data[i];
        postData.push({
          dish_name:item.dish_name,
          dish_img:item.dish_img,
          dish_num:item.dish_num,
          dish_price:item.dish_price,
        });
    }
    
    console.log(postData);
    wx.navigateTo({
      url: '../../pages/pay/pay?postData='+encodeURIComponent(JSON.stringify(postData))+"&order_id="+data.order_id,
    })
    this.orderShow()
  },
  goEvaluate:function (event) {
    wx.navigateTo({
      url: '../../pages/evaluate/evaluate?order_id='+event.target.dataset.id,
    })
    this.orderShow()
  }
})