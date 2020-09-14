import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Diary from '@/views/diaries/Diary'
// Babble Box
import Babblebox from '@/views/common/Babblebox'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Diary',
    component: Diary
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  // Child List
  {
    path: '/babblebox',
    name: 'Babblebox',
    component: Babblebox
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
