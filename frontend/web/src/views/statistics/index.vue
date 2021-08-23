<template>
  <pro-table
    title="餐品列表"
    ref="table"
    :request="getDishSaleList"
    :columns="columns"
    :pagination="pagination"
  >
  </pro-table>
</template>

<script>
import * as API from '@/api/dish.js'
import {
  defineComponent,
  reactive,
  toRefs,
} from 'vue'

export default defineComponent({
	name:'dishlist',
  setup() {

    //餐品检索框
    const state = reactive({
      // 表格列配置，大部分属性跟el-table-column配置一样
      columns: [
		{ label: '餐品ID', prop: 'dish_id' },
        { label: '餐品名称', prop: 'dish_name' },
		{ label: '餐品销量', prop: 'dish_number' },
        { label: '餐品评分', prop: 'dish_score' },
      ],
      pagination: {
        pageSize: 10,
        pageSizes: [10, 20, 50],
      },
    })
    //获取餐品列表
    const getDishSaleList = async params => {
      const { data, total } = await API.getDishSaleList(params)

      return {
        data,
        total,
      }
    }

    return {
      ...toRefs(state),
      getDishSaleList,
    }
  },
})
</script>

<style></style>
