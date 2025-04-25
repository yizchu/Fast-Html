import type { RouteRecordRaw } from 'vue-router'


const routes: RouteRecordRaw[] = [
    {
        path: '/',
        component: () => import('@/components/test.vue'),
    },
    {
        path: '/test',
        component: () => import('@/components/test.vue'),
        meta: {
            title: 'Fast HTML',
        }
    },
    {
        path: '/style',
        component: () => import('@/components/dialog/style.vue'),
        meta: {
            title: '样式',
        }
    }

]

export default routes