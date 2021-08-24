<template>
  <pro-table
    title="餐品列表"
    ref="table"
    :request="getDishList"
    :columns="columns"
    :pagination="pagination"
    @selectionChange="handleChange"
  >
    <template #toolbar>
      <el-button type="primary" @click="$router.push('/dish/add')">
        添加菜品
      </el-button>
      <el-button
        v-if="selectedDishIds.length > 0"
        type="danger"
        @click="deleteDish(selectedDishIds.join(','))"
      >
        批量删除
      </el-button>
    </template>
    <template #operate="{row}">
      <el-button type="primary" size="mini" @click="$router.push(`/dish/edit/${row.dish_id}`)">
        编辑
      </el-button>
      <el-button type="danger" size="mini" @click="deleteDish(row.dish_id)">
        删除
      </el-button>
    </template>
  </pro-table>
</template>

<script>
import * as API from '@/api/dish.js'
import {
  defineComponent,
  getCurrentInstance,
  reactive,
  toRefs,
  onBeforeMount,
  ref,
} from 'vue'

export default defineComponent({
	name:'dishlist',
  setup() {
    //刷新列表
    const table = ref(null)
    //获取
    const { ctx } = getCurrentInstance()

    //餐品检索框
    const state = reactive({
      // 表格列配置，大部分属性跟el-table-column配置一样
      columns: [
        { label: 'label', type: 'selection' },
        { label: '餐品名称', prop: 'dish_name' },
        { label: '餐品ID', prop: 'dish_id' },
        { label: '餐品分类', prop: 'dish_class' },
        { label: '操作', tdSlot: 'operate', width: 188 },
      ],
      pagination: {
        pageSize: 10,
        pageSizes: [10, 20, 50],
      },
      selectedDishIds: [],
    })
    //获取餐品列表
    const getDishList = async params => {
		const { data, total } = await API.getDishList(params)
		return {
			data,
			total,
		}
    }
    //删除菜品
    const deleteDish = dish_id_temp => {
      ctx
        .$confirm('是否确认删除？')
        .then(async () => {
          const $loading = ctx.$loading()
		  let data = {
			  dish_id:dish_id_temp,
		  }
          const { code } = await API.deleteDish(data)
          $loading.close()
          if (+code === 200) {
            ctx.$message.success('删除成功')
            table.value.refresh()
          }
        })
        .catch(() => {})
    }

    //处理多选
    const handleChange = arr => {
      state.selectedDishIds = arr.map(item => item.dish_id)
    }

    return {
      ...toRefs(state),
      getDishList,
      deleteDish,
      table,
      handleChange,
    }
  },
})
</script>

<style></style>
