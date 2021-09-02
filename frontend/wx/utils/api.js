// 预定义请求方式
const GET = 'GET';
const POST = 'POST';
const PUT = 'PUT';
const FORM = 'FORM';
const DELETE = 'DELETE';

//URL基地址
const baseURL = 'http://10.237.54.38:5111/';

//封装request
function request(method, url, data=[]) {
    return new Promise(function(resolve, reject) {
        let header = {
            'content-type': 'application/json',
        };
        wx.request({
            url: baseURL + url,
            method: method,
            data:{
                data:JSON.stringify(data),    //将data转为JSON (data需为对象)
            },
            header: header,
            success(res) {
                //请求成功
                console.log("请求成功");
                //判断状态码---errCode状态根据后端定义来判断
                if (res.statusCode == 200) {
                    resolve(res.data);
                } else {
                    //其他异常
                    console.log("状态码错误");
                    console.log(res);
                    reject('运行时错误,请稍后再试');
                }
            },
            fail(err) {
                //请求失败
                console.log("请求失败");
                console.log(err)
                reject(err)
            }
        })
    })
};
//接口定义
const API = {
    // 登录 data:(code) res:(user_id,token)
    login:(data) => request(GET,"api/WXLogin",data),
    // 获取餐品列表
    getDishList:(data) => request(GET,"api/WXDishList",data),
    // 获取餐品详情
    getDishDetail:(data) => request(GET,"api/WXDishInfo",data),
    // 获取推荐菜品
    getRecommend:(data) => request(GET,"api/WXRecommend",data),
    // 提交订单
    submitOrder:(data) => request(GET,"api/WXSubmitOrder",data),
    // 获取订单列表
    getOrderList:(data) => request(GET,"api/WXCheckOrder",data),
    // 支付
    pay:(data) => request(GET,"api/WXPay",data),
    // 取消订单
    cancelOrder:(data) => request(GET,"api/WXCancelOrder",data),
    // 用户确认收货
    receiveOrder:(data) => request(GET,"api/WXConfirmOrder",data),
    // 用户评价
    evaluate:(data) => request(GET,"api/WXEvaluateOrder",data),
    // 获取地址
    getAddresses:(data) => request(GET,"api/WXSearchAddress",data),
    // 上传地址
    submitAddress:(data) => request(GET,"api/WXRefreshAddress",data),
};

module.exports = {
    API:API
}