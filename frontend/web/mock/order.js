export default [
	{
		url: '/api/order-list',
		method: 'get',
		timeout: 1000,
		response: body => {
			return {
				// 响应内容
				code: 200,
				message: '获取订单列表成功',
				[`data|${body.query.pageSize}`]: [
					{
					  'order_id':'@id()',
					  'order_dish':'@cname()',
					  'order_price':'@integer(10,100)',
					  'order_time':'@datatime()',
					  'order_status':'@pick("未支付","已支付","待收货","待评价","已完成")',
					},
				],
				'total|100-999':1,
			}
		},
	},
	//模拟编辑菜品
	{
		url: '/api/order/edit/:order_id',
		method: 'get',
		timeout: 1000,
		statusCode: 200,
		response: {
			// 响应内容
			code: 200,
			message: '修改订单成功',
		},
	},
	//删除订单
	{
		url: '/api/order/:order_id',
		method: 'get',
		timeout: 1000,
		response: {
			// 响应内容
			code: 200,
			message: '删除成功',
		},
	},
]
