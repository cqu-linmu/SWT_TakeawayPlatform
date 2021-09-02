// pages/add-address/add-address.js
const API = require("../../utils/api.js").API;
Page({

  /**
   * 页面的初始数据
   */
  data: {
    user_id: 1,
    address: "",
    addresses: [],
    save: "保存"
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      user_id: options.user_id,
      addresses: JSON.parse(decodeURIComponent(options.addresses)).addresses,
    });
    console.log("addresses的type:",typeof(this.data.addresses));
  },
  saveAddress: function (e) {
    this.setData({
      address: e.detail.value,
    })
  },
  submitAddress: function () {
    let tempAddresses = [];
    tempAddresses.push(this.data.address);
    for (const i in this.data.addresses) {
      const item = this.data.addresses[i];
      tempAddresses.push(item);
      // console.log("tempAddresses:",tempAddresses);
    }
    let data = {
      user_id: wx.getStorageSync("user_id"),
      user_address_new: tempAddresses
    };
    console.log("输入的data:",data);
    API.submitAddress(data)
      .then(res => {
        console.log("更新地址成功");
      })
      .catch(err => {
        console.log("更新地址失败");
      })
    wx.navigateBack({
      delta: 0,
    })
  },
})