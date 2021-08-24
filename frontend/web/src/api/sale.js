import request from '@/utils/request'

// 获取每日流水列表 => 每日流水
export const getDailySale = data => {
	return request({
		url: '/api/sale-daily',
		method: 'get',
		params: data,
	})
}

