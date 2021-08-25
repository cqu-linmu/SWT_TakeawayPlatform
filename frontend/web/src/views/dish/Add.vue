<template>
	<el-form class="form" ref="form" :model="model" :rules="rules" label-width="80px">
		
		<el-form-item label="菜品名称" >
			<el-input 
				type="text" 
				v-model.trim="model.dish_name" 
				placeholder="请输入菜品名称" 
				clearable>
			</el-input>
		</el-form-item>
		
		<el-form-item label="菜品分类">
			<el-select 
				v-model="model.dish_class" 
				placeholder="请选择菜品分类">
					<el-option
						v-for="item in dish_classes"
						:key="item.class_name"
						:label="item.class_value"
						:value="item.class_name">
				    </el-option>
			</el-select>
		</el-form-item>
	
		<el-form-item label="菜品价格" >
			<el-input-number
				v-model="model.dish_price" 
				:precision="2" 
				:step="1" 
				:min="0" 
				:max="9999" >
			</el-input-number>
		</el-form-item>
	
	
		<el-form-item label="菜品描述">
			<el-input 
				type="textarea" 
				:autosize="{ minRows: 2, maxRows: 20}" 
				placeholder="请输入内容" 
				v-model.trim="model.dish_description">
			</el-input>
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
		onBeforeMount,
		reactive,
		ref,
		toRefs,
	} from 'vue'
	
	import * as API from '@/api/dish'
	import {useStore} from 'vuex'
	import {useRoute, useRouter} from 'vue-router'
	
	export default defineComponent( {
		name:'dishAdd',
		setup() {
			const { ctx } = getCurrentInstance()
			const store = useStore()
			const router = useRouter()
			const route = useRoute()
			const form = ref(null)
			const state = reactive({
				model: {
					dish_name: '',
					dish_class: '',
					dish_price: 1,
					dish_description: '',
				},
				rules:{
					dish_name:[
						{
							required:true,
							message:'请输入菜品名称',
							trigger:'blur',
						},
						{
							min:2,
							max:20,
							message:'菜品名长度为2-20位',
							trigger:'blur',
						},
					],
					dish_class:[
						{
							required:true,
							message:'请选择菜品分类',
							trigger:'blur',
						},
					],
					dish_price:[
						{
							required:true,
							message:'请输入菜品价格',
							trigger:'blur',
						},
					],
					dish_description:[
						{
							required:true,
							message:'请输入菜品描述',
							trigger:'blur',
						},
					],
				},
				dish_classes:[],
			})
			onBeforeMount(async ()=>{
				//获取菜品分类
				const {code, data} = await API.getDishClassList()
				if (+code ===200) {
					state.dish_classes = data
					console.log('===============成功读取菜品分类================')
				}
				
				// if(route.params.dish_id) {
				// 	const {code,data} = await API.GetDishInfo(route.params.dish_id)
				// 	if(+code===200) {
				// 		state.model = data
				// 		console.log('===============成功读取菜品ID================')
				// 	}
				// }
			})
			const submitForm = () => {
				form.value.validate(async valid => {
					if(valid) {
						const { code, message } = await API[
							route.params.dish_id? 'editDish' : 'addDish'
						](state.model)
						if (+code===200) {
							ctx.$message.success(message)
							store.dispatch('tags/delTag', route)
							router.push('/dish/list?t=' + Date.now())
						} else {
						  ctx.$message.error(message)
						}
					}
					else {
						console.log('===============表单无效================')
					}
				})
			}
			const quit = () => {
				store.dispatch('tags/delTag', route)
				router.push('/dish/list')
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