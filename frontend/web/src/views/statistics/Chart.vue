<template>
    <div>
        <div id="main" style="width:800px; height:500px">
		</div>
    </div>
</template>
        
<script>
	import { onMounted } from "vue";
	import * as API from '@/api/sale.js'
	import * as echarts from 'echarts'
	export default {
		name: "chart",
		setup() {
			
			onMounted(async (params) => {//需要获取到element,所以是onMounted的Hook
				const { data } = await API.getDailySale(params={
					order_time_st : '2021-08-23',
				})
				console.log('data:',data)
				var data_sale = {
					order_time : [],
					sale_daily : [],
				}
				for (var i = 0; i < data.length; i++) {
					data_sale.order_time.push(data[i].order_time)
					data_sale.sale_daily.push(data[i].sale_daily)
				}
				console.log('data_sale:',data_sale)
				let myChart = echarts.init(document.getElementById("main"));
				// 绘制图表
				myChart.setOption({
					title: { text: "每日流水" },
					tooltip: {},
					xAxis: {
						data: data_sale.order_time,
					},
					yAxis: {},
					series: [
					{
						name: "用户量",
						type: "line",
						data: data_sale.sale_daily,
					},],
				});
				window.onresize = function () {//自适应大小
					myChart.resize();
				};
			});
		},
		components: {},
		mounted() {},
	};
</script> 
<style>
	
</style>   
