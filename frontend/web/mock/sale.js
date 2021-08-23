export default [
	{
		url: '/api/sale-daily',
		method: 'get',
		timeout: 1000,
		response: body => {
			return {
				// 响应内容
				code: 200,
				message: '获取每日流水成功',
				'data|30': [
					{
					  'sale_daily|100-200':1,
					  'order_time':'@datetime()'
					},
				],
			}
		},
	},
]
