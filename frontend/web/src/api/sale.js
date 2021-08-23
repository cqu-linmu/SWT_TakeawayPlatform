import request from '@/utils/request'

// 获取订单餐品列表
export const getDailySale = data => {
	return request({
		url: '/api/sale-daily',
		method: 'get',
		params: data,
	})
}

