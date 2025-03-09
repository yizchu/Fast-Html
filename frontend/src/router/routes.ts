import type { RouteRecordRaw } from 'vue-router'


const routes: RouteRecordRaw[] = [
    {
        path: '/home',
        component: () => import('@/components/start_menu.vue'),
    },

    {
        path: '/',
        component: () => import('@/components/dev_page.vue'),
    },

]

export default routes