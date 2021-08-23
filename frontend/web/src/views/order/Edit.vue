<template>
	<el-form class="form" ref="form" :model="model" label-width="80px">
		
		<el-form-item label="订单状态">
			<el-select 
				v-model="model.order_status" 
				placeholder="请选择订单状态">
					<el-option
						v-for="item in options"
						:key="item.value"
						:label="item.name"
						:value="item.value">
				    </el-option>
			</el-select>
		</el-form-item>
	
		<el-form-item>
			<el-button type="primary" @click="submitForm">提交</el-button>
			<el-button type="primary" @click="quit">取消</el-button>
		</el-form-item>
	</el-form>
</template>

<script>
	import {
		defineComponent,
		getCurrentInstance,
		reactive,
		ref,
		toRefs,
	} from 'vue'
	
	import * as API from '@/api/order'
	import {useStore} from 'vuex'
	import {useRoute, useRouter} from 'vue-router'
	
	export default defineComponent( {
		name:'orderAdd',
		setup() {
			const { ctx } = getCurrentInstance()
			const store = useStore()
			const router = useRouter()
			const route = useRoute()
			const form = ref(null)
			const state = reactive({
				model: {
					order_id: route.params.dish_id,
					order_status: '',
				},
				options:[
					{
						value: '未支付',
						label: '未支付',
					}, 
					{
						value: '已支付',
						label: '已支付',
					}, 
					{
						value: '待收货',
						label: '待收货',
					}, 
					{
						value: '待评价',
						label: '待评价',
					}, 
					{
						value: '已完成',
						label: '已完成',
					}, 
					{
						value: '已取消',
						label: '已取消',
					}, 
				],
			})
			const submitForm = async params => {
			  const { code, message } = await API.editOrder(state.model)
			  if (+code===200) {
			  	ctx.$message.success(message)
			  	store.dispatch('tags/delTag', route)
			  	router.push('/order/list?t=' + Date.now())
			  } else {
			    ctx.$message.error(message)
			  }
			}
			const quit = () => {
				store.dispatch('tags/delTag', route)
				router.push('/order/list')
			}
			return {
				...toRefs(state),
				form,
				submitForm,
				quit,
			}
		}
	})
</script>