<!--
 * @Descripttion: 
 * @version: 
 * @Date: 2021-04-20 11:06:21
 * @LastEditors: huzhushan@126.com
 * @LastEditTime: 2021-04-23 15:16:12
 * @Author: huzhushan@126.com
 * @HomePage: https://huzhushan.gitee.io/vue3-element-admin
 * @Github: https://github.com/huzhushan/vue3-element-admin
 * @Donate: https://huzhushan.gitee.io/vue3-element-admin/donate/
-->
<template>
  <div id='home' class="home" style="width:600px; height:600px"></div>
</template>

<script>
	import * as API from '@/api/dish.js'
	import { onMounted } from "vue";
	import * as echarts from 'echarts'
	export default {
		name: "chart",
		setup() {
			onMounted(async (params) => {
				
				//绘图
				//=========================================================
				var chartDom = document.getElementById('home');
				var myChart = echarts.init(chartDom);
				var option;
				const { data } = await API.getDishSaleList(params={
					page:-1,
					pageSize:10
				})
				console.log('data:',data)
				console.log('成功读取列表')

				var data_sale=[]
				console.log('data_sale:',data_sale)
				for (var i = 0; i < data.length; i++) {
					let sale = data[i].dish_number * data[i].dish_price
					data_sale.push({
						name:data[i].dish_name+ ':' + sale,
						value:sale,
					})
				}
				console.log('data_sale:',data_sale)

				option = {
				    legend: {
				        top: 'bottom'
				    },
				    toolbox: {
				        show: true,
				        feature: {
				            mark: {show: true},
				            dataView: {show: true, readOnly: true},
				            restore: {show: true},
				            saveAsImage: {show: true}
				        }
				    },
				    series: [
				        {
				            name: '面积模式',
				            type: 'pie',
				            radius: [25, 200],
				            center: ['50%', '50%'],
				            roseType: 'area',
				            itemStyle: {
				                borderRadius: 8
				            },
				            data: data_sale,
				        }
				    ]
				};
				option && myChart.setOption(option);
				window.onresize = function () {//自适应大小
					myChart.resize();
				};
				//=========================================================
			});
			return {

			}
		},
		// components: {},
		// mounted() {},

		
	};
</script>

<style lang="scss" scoped>
.home {
  color: $mainColor;
}
</style>
