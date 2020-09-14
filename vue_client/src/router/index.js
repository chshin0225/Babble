import Vue from 'vue'
import VueRouter from 'vue-router'
import Diary from '@/views/diaries/Diary.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Diary',
    component: Diary
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
