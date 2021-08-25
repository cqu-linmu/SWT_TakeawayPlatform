import request from '@/utils/request'

// 获取餐品列表 => 餐品管理
export const getDishList = data => {
  return request({
    url: '/api/dish-list',
    method: 'get',
    params: data,
  })
}
// 获取餐品销售列表 => 单品销售量统计
export const getDishSaleList = data => {
  return request({
    url: '/api/dish-Sale-list',
    method: 'get',
    params: data,
  })
}
// // 获取餐品信息 => 
// export const getDishInfo = dish_id => {
//   return request({
//     url: `/api/dish/view/${dish_id}`,
//     method: 'get',
//   })
// }
// 添加餐品 => 菜品编辑
export const addDish = data => {
  return request({
    url: '/api/dish/add',
    method: 'get',
    params: data,
  })
}
// 修改餐品 => 菜品编辑
export const editDish = data => {
  return request({
    url: `/api/dish/edit`,
    method: 'get',
    params: data,
  })
}

// 删除餐品 => 删除菜品
export const deleteDish = data => {
  return request({
    url: `/api/dish`,
    method: 'get',
    params: data,
  })
}
// 获取餐品分类列表 => 获取餐品分类
export const getDishClassList = data => {
  return request({
    url: '/api/dish_class-list',
    method: 'get',
    params: data,
  })
}