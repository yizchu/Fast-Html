import { createRouter, createWebHistory } from 'vue-router'
import routes from './routes'

const router = createRouter({
    routes,
    history: createWebHistory(),
    scrollBehavior() {
        return { top: 0 }
    }
})
router.beforeEach((to, from, next) => {
    if (to.meta && to.meta.title) {
        document.title = to.meta.title as string; // 设置页面标题
    }
    next();
});
export default router;