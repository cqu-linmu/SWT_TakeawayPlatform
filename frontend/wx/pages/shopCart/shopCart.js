const API = require("../../utils/api").API;
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    cart: [],
    isAllChecked: false, //是否全选
    checkedArrId: [], //复选框选中的值
    totalPrice: 0,
    totalCount: 0,
    status: 'pay', //pay结算，delete删除编辑状态
  },
  onLoad: function () {
    app.checkout()
    if (wx.getStorageSync('isTokenUseful')) {
      this.setData({
        cart: [],
        isAllChecked: false,
        checkedArrId: [],
        totalPrice: 0,
        totalCount: 0,
        status: 'pay',
      })
      console.log("加载购物车页面");
      try {
        var cartData = wx.getStorageSync('cartData')
        this.setData({
          cart: cartData
        })
      } catch (e) {
        console.log("没有找到对应缓存");
      }
      for (let i = 0; i < this.data.cart.length; i++) {
        const item = this.data.cart[i];
        item["checked"] = true;
      }
    } else {
      console.log("未授权登录正在前往授权登录页面");
      wx.navigateTo({
        url: '/pages/index/index', //授权页面
      })
    }
  },
  onShow: function () {
    this.onLoad();
  },
  //选择购物车商品
  handleShopChange(e) {
    let {
      cart,
      isAllChecked
    } = this.data
    let values = e.detail.value
    for (let i = 0; i < cart.length; i++) {
      const item = cart[i];
      //有时候id可能是number也有可能是string，这里做统一string处理
      let dishId = String(i)
      // 如果要检索的字符串值没有出现，则返回 -1。
      values.indexOf(dishId) >= 0 ? item.checked = true : item.checked = false
    }
    // console.log(values);
    let checkArr = [];
    for (let i = 0; i < cart.length; i++) {
      const item = cart[i];
      if (item.checked) {
        checkArr.push(item.dish_id)
      }
    }
    this.setData({
      checkedArrId: checkArr
    })
    let length = values.length
    // 如果选择的数组中有值，并且长度等于列表长度，就是全选
    length > 0 && length === cart.length ? isAllChecked = true : isAllChecked = false
    this.setData({
      isAllChecked
    })
    this.calTotalCountPrice()
  },
  //加减数量
  handleCountChange(e) {
    const {
      type,
      id
    } = e.currentTarget.dataset

    let {
      cart
    } = this.data
    if (type === 'add') {
      //最大数量显示10个
      if (cart[id].dish_num >= 10) return
      cart[id].dish_num++
    } else {
      //最小数量限制一个
      if (cart[id].dish_num === 1) return
      cart[id].dish_num--
    }
    this.setData({
      cart
    })
    this.calTotalCountPrice()
  },
  //全选
  onSelectAll(e) {
    let {
      cart,
      isAllChecked
    } = this.data
    let values = e.detail.value
    for (let i = 0; i < cart.length; i++) {
      cart[i].checked = false
      if (values[0] === 'all') {
        isAllChecked = true
        cart[i].checked = true
      } else {
        isAllChecked = false
        cart[i].checked = false
      }
    }
    this.setData({
      isAllChecked,
      cart
    })
    this.calTotalCountPrice()
  },
  //购物车状态
  onClickEdit() {
    let {
      status
    } = this.data
    if (status === 'pay') {
      this.setData({
        status: 'delete'
      })
      return
    }
    this.setData({
      status: 'pay'
    })
  },
  //计算总数和价格
  calTotalCountPrice() {
    let {
      cart,
      totalCount,
      totalPrice
    } = this.data
    //每次执行的时候初始化，防止重复计算
    totalCount = 0
    totalPrice = 0
    for (let i = 0; i < cart.length; i++) {
      //如果都是选中的状态在计算
      if (cart[i].checked) {
        totalCount += 1
        totalPrice += cart[i].dish_price * cart[i].dish_num
      }
    }
    this.setData({
      totalCount,
      totalPrice: totalPrice.toFixed(2)
    })
  },
  //结算和删除
  onPayOrDelete(e) {
    const {
      status
    } = this.data
    console.log("e:", e);
    console.log(status)
    status === 'delete' && this.deleteShopCartList()
    status === 'pay' && this.payShopCartPrice()
    this.onLoad()
  },
  // 删除选中的菜品列表
  deleteShopCartList() {
    try {
      var cartData = wx.getStorageSync('cartData')
      console.log(cartData);
    } catch (e) {
      console.log("没有找到对应缓存");
    }
    for (const i in this.data.checkedArrId) {
      const id = this.data.checkedArrId[i];
      for (let j = 0; j < cartData.length; j++) {
        const item = cartData[j];
        if (item.dish_id == id) {
          cartData.splice(j, 1);
          break;
        }
      }
    }
    try {
      wx.setStorageSync('cartData', cartData)
    } catch (e) {}
    // wx.removeStorageSync('')
    wx.showToast({
      title: 'delete',
    })
  },
  // 跳转到支付页面
  payShopCartPrice() {
    let data = {
      user_id: wx.getStorageSync("user_id"),
      dish_data: []
    }
    for (const i in this.data.cart) {
      const item = this.data.cart[i];
      data.dish_data.push({
        dish_id: item.dish_id,
        dish_num: item.dish_num
      });
    }
    API.submitOrder(data)
      .then(res => {
        let orderId = res.data.order_id;
        wx.navigateTo({
          url: '../../pages/pay/pay?order_id=' + orderId,
        })
      })
      .catch(err => {

      });
  },
  onPullDownRefresh: function () {},
  onReachBottom: function () {},
  touchStart: function () {},
  touchMove: function () {},
  touchEnd: function () {}
})