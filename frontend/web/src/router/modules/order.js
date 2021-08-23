const Layout = () => import('@/layout/index.vue')
const List = () => import('@/views/order/index.vue')
const Edit = () => import('@/views/order/Edit.vue')

export default [
  {
    path: '/order',
    component: Layout,
    name: 'order-manage',
    meta: {
      title: '订单管理',
    },
    icon: 'order-manage',
    children: [
      {
        path: 'list',
        name: 'orderlist',
        component: List,
        meta: {
          title: '订单列表',
        },
      },
      {
        path: 'edit/:order_id',
        name: 'editOrder',
        component: Edit,
        meta: {
          title: '修改订单',
        },
        hidden: true,
      },
    ],
  },
]
