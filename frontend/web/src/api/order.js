import request from '@/utils/request'

// 获取订单列表 => 订单管理
export const getOrderList = data => {
  return request({
    url: '/api/order-list',
    method: 'get',
    params: data,
  })
}
// // 获取每日订单列表
// export const getOrderDailyList = data => {
//   return request({
//     url: '/api/order-daily-list',
//     method: 'get',
//     params: data,
//   })
// }
// 删除订单
export const deleteOrder = data => {
  return request({
    url: `/api/order`,
    method: 'get',
    params: data
  })
}
// 修改订单 => 订单编辑
export const editOrder = data => {
  return request({
    url: `/api/order/edit`,
    method: 'get',
    params: data,
  })
}
// // 获取订单状态列表	
// export const getOrderClassList = data => {
//   return request({
//     url: '/api/order_class-list',
//     method: 'get',
//     params: data,
//   })
// }