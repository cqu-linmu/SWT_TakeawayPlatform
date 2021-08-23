const Layout = () => import('@/layout/index.vue')
const List = () => import('@/views/dish/index.vue')
const Add = () => import('@/views/dish/Add.vue')

export default [
  {
    path: '/dish',
    component: Layout,
    name: 'dish-manage',
    meta: {
      title: '菜品管理',
    },
    icon: 'dish-manage',
    children: [
      {
        path: 'list',
        name: 'dishlist',
        component: List,
        meta: {
          title: '菜品列表',
        },
      },
      {
        path: 'add',
        name: 'addDish',
        component: Add,
        meta: {
          title: '添加菜品',
        },
        hidden: true,
      },
      {
        path: 'edit/:dish_id',
        name: 'editDish',
        component: Add,
        meta: {
          title: '修改菜品',
        },
        hidden: true,
      },
	  {
	    path: 'view/:dish_id',
	    name: 'viewDish',
	    component: Add,
	    meta: {
	      title: '查看菜品',
	    },
	    hidden: true,
	  },
    ],
  },
]
