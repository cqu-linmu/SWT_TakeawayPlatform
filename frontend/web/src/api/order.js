import request from '@/utils/request'

// 获取订单餐品列表
export const getOrderList = data => {
  return request({
    url: '/api/order-list',
    method: 'get',
    params: data,
  })
}
// 获取每日订单列表
export const getOrderDailyList = data => {
  return request({
    url: '/api/order-daily-list',
    method: 'get',
    params: data,
  })
}
// 删除订单
export const deleteOrder = order_id => {
  return request({
    url: `/api/order/${order_id}`,
    method: 'delete',
  })
}
// 修改订单
export const editOrder = data => {
  return request({
    url: `/api/order/edit/${data.order_id}`,
    method: 'get',
    params: data,
  })
}
// 获取订单状态列表
export const getOrderClassList = data => {
  return request({
    url: '/api/order_class-list',
    method: 'get',
    params: data,
  })
}
