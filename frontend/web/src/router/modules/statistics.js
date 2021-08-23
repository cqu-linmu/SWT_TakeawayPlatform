const Layout = () => import('@/layout/index.vue')
const Index = () => import('@/views/statistics/index.vue')
const Chart = () => import('@/views/statistics/Chart.vue')

export default [
  {
    path: '/statistics',
    component: Layout,
    name: 'statistics-manage',
    meta: {
      title: '统计管理',
    },
    icon: 'statistics-manage',
    children: [
		{
		  path: 'list',
		  name: 'statisticsList',
		  component: Index,
		  meta: {
		    title: '餐品销售情况',
		  },
		},
		{
			path: 'chart',
			name: 'statisticsChart',
			component:Chart,
			meta: {
			  title: '每日流水',
			},
		}
    ],
  },
]
