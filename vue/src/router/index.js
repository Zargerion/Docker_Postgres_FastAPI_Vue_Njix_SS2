import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Hello, bro!',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/about',
    name: 'Creations',
    component: () => import('../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

router.beforeEach((to, from, next) => {
  document.title = to.name;
  next();
})

