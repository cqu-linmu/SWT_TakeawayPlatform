const API = require("../../utils/api.js").API;
Page({
  data: {
    user_id:wx.getStorageSync("user_id"),
    addresses:[]
  },

  onLoad: function(options) {
    console.log(options);
    let data = {
      user_id:wx.getStorageSync("user_id"),
    };
    API.getAddresses(data)
    .then(res=>{
      console.log(res.data);
      this.setData({
        user_id:options.user_id,
        addresses:res.data.user_address
      });
    })
    .catch(err=>{
      console.log("获取用户地址失败");
    });
  },
  newAddress(){
    wx.navigateTo({
      url: '../../pages/add-address/add-address?user_id='+this.data.user_id+'&addresses='+encodeURIComponent(JSON.stringify({addresses:this.data.addresses}))
    })
  },
})