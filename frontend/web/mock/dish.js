export default [
	//模拟菜品列表
	{
		url: '/api/dish-list',
		method: 'get',
		timeout: 1000,
		response: body => {
			return {
			// 响应内容
			code: 200,
			message: '获取餐品列表成功',
			[`data|${body.query.pageSize}`]: [
				{
				  'dish_id':'@id()',
				  'dish_name':'@cname()',
				  'dish_class':'@pick("主食","饮品","小吃")',
				},
			],
			'total|100-999':1,
			}
		},
	},
	//获取菜品销售信息
	{
		url: '/api/dish-sale-list',
		method: 'get',
		timeout: 1000,
		response: body => {
			return {
			// 响应内容
			code: 200,
			message: '获取餐品销售列表成功',
			[`data|${body.query.pageSize}`]: [
				{
				  'dish_id':'@id()',
				  'dish_name':'@cname()',
				  'dish_price|10-50':1,
				  'dish_number|50-100':1,
				  'dish_score|2-10.1':1,
				},
			],
			'total|50':1,
			}
		},
	},
	//获取菜品信息
	{
		url: '/api/dish/view/:dish_id',
		method: 'get',
		timeout: 1000,
		response:{
			// 响应内容
			code: 200,
			message: '获取餐品信息成功',
			data: [
				{
				  'dish_id':'@id()',
				  'dish_name':'@cname()',
				  'dish_price':'@number(10,100)',
				  'dish_class':'@pick("主食","饮品","小吃")',
				  'dish_description':'@pick("主食","饮品","小吃")',
				},
			],
		},
	},
	//模拟菜品分类列表
	{
		url: '/api/dish_class-list',
		method: 'get',
		timeout: 1000,
		response: {
			// 响应内容
			code: 200,
			message: '获取餐品分类列表成功',
			'data': [
				{
					class_name:'主食',
					class_value:'主食',
				},
				{
					class_name:'小吃',
					class_value:'小吃',
				},
				{
					class_name:'饮品',
					class_value:'饮品',
				},
			],
		},
	},
	//删除菜品
	{
		url: '/api/dish/:dish_id',
		method: 'get',
		timeout: 1000,
		statusCode: 200,
		response: {
			// 响应内容
			code: 200,
			message: '删除成功',
		},
	},
	//模拟添加菜品
	{
		url: '/api/dish/add',
		method: 'get',
		timeout: 1000,
		statusCode: 200,
		response:{
			// 响应内容
			code: 200,
			message: '添加菜品成功',
		},
	},
	//模拟编辑菜品
	{
		url: '/api/dish/edit/:dish_id',
		method: 'get',
		timeout: 1000,
		statusCode: 200,
		response: {
			// 响应内容
			code: 200,
			message: '修改菜品成功',
		},
	},
]
