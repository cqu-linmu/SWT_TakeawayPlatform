
//调用接口
const API = require("../../utils/api.js").API;
var that = '';
var query;
Page({
    /**
     * 页面的初始数据
     */
    data: {
        dataList: [],
        recommends:[],
        idx: 0,
        scrollTop: 0,
        toView:'position0'
      },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function () {
        API.getRecommend()
            .then(res =>{
                let tmpdata  = []
                console.log("请求推荐列表的返回:",res);
                for (const i in res.data) {
                    const item = res.data[i];
                    tmpdata[i] = {
                        url:'../../pages/dish/dish?dish_id=' + item.dish_id,
                        dish_img:item.dish_img
                    }
                }
                console.log("data:",tmpdata);
                this.setData({
                    recommends:tmpdata
                })
            })
            .catch(err =>{
                //请求失败
                console.log("请求失败");
                console.log(err);
            })
        // 调用接口获取餐品列表
        API.getDishList()
            .then(res => {
                // console.log(res.data);
                // console.log(typeof( res.data));
                //获取到数据后，对列表进行处理
                console.log("请求菜品列表的返回",res);
                let data_handled = this.handleData(res);
                //将处理后的数据赋值
                this.setData({ dataList:data_handled });
            })
            .catch(err => {
                //请求失败
                console.log("请求失败");
                console.log(err);
            })
        query = wx.createSelectorQuery();
        that = this;
        wx.createSelectorQuery().selectAll('.position').boundingClientRect(function (rects) {
            that.setData({ positions:rects })
        }).exec();
        wx.setStorage({
            key: 'cartData',
            data:[]
        })
    },
    onShow:function() {
        this.onLoad()
    },
    //标签跳转
    switchClassfun(e){
        var e = e.currentTarget.dataset.index;
        this.setData({ idx: e, toView: 'position' + e })
    },
    // 餐品页面跳转
    bindDishTap(e) {
        let dish_id = e.currentTarget.dataset.index;
        dish_id = JSON.stringify(dish_id);
        // let dataList = JSON.stringify()
        wx.navigateTo({
            url: '../../pages/dish/dish?dish_id=' + dish_id,
        })
    },
    //滑动
    bindscrollfunc(e){
        var arr = [];
        for(var item of this.data.positions){
            if (item.top <= e.detail.scrollTop + 2){
                arr.push(item)
            }
        }
        try {
            this.setData({ idx:arr[arr.length-1].dataset.index })
        } catch (error) {}//处理arr数字空的报错 
    },
    handleData(res){
        let data_handled = [];
        for (const i in res.data) {
            let item = res.data[i];
            // console.log(item);
            let index = -1;
            for (const j in data_handled) {
                const it = data_handled[j];
                if (it.dish_type==item.dish_type) {
                    index = j;
                    break;
                }
            }
            if(index!=-1) {
                data_handled[index].dishes.push(item);
            }
            else {
                data_handled.push({
                    "dish_type":item.dish_type,
                    "dishes":[item]
                });
            }
            // console.log(data_handled);
        }
        return data_handled;
    },
    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {
    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {

    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    }
})