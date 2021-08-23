<template>
  <pro-table
    title="订单列表"
    ref="table"
    :request="getOrderList"
    :columns="columns"
    :pagination="pagination"
    @selectionChange="handleChange"
  >
    <template #toolbar>
      <el-button
        v-if="selectedOrderIds.length > 0"
        type="danger"
        @click="deleteOrder(selectedOrderIds.join(','))"
      >
        批量删除
      </el-button>
    </template>
    <template #operate="{row}">
      <el-button type="primary" size="mini" @click="$router.push(`/order/edit/${row.order_id}`)">
        编辑
      </el-button>
      <el-button type="danger" size="mini" @click="deleteOrder(row.order_id)">
        删除
      </el-button>
    </template>
  </pro-table>
</template>

<script>
import * as API from '@/api/order.js'
import {
  defineComponent,
  getCurrentInstance,
  reactive,
  toRefs,
  onBeforeMount,
  ref,
} from 'vue'

export default defineComponent({
	name:'dishList',
	setup() {
    //刷新列表
    const table = ref(null)
    //获取
    const { ctx } = getCurrentInstance()

    //订单检索框
    const state = reactive({
      // 表格列配置，大部分属性跟el-table-column配置一样
      columns: [
        { label: 'label', type: 'selection' },
        { label: '订单ID', prop: 'order_id' },
		{ label: '菜品名称', prop: 'order_dish' },
        { label: '订单金额', prop: 'order_price' },
		{ label: '订单状态', prop: 'order_status' },
        { label: '操作', tdSlot: 'operate', width: 188 },
      ],
      pagination: {
        pageSize: 10,
        pageSizes: [10, 20, 50],
      },
      selectedOrderIds: [],
    })
    //获取订单列表
    const getOrderList = async params => {
      const { data, total } = await API.getOrderList(params)

      return {
        data,
        total,
      }
    }
    //删除订单
    const deleteOrder = order_id => {
      ctx
        .$confirm('是否确认删除？')
        .then(async () => {
          const $loading = ctx.$loading()
          const { code } = await API.deleteOrder(order_id)
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
      state.selectedOrderIds = arr.map(item => item.order_id)
    }

    return {
      ...toRefs(state),
      getOrderList,
      deleteOrder,
      table,
      handleChange,
    }
  },
})
</script>

<style></style>
