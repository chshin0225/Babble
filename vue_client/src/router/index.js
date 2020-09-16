import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/views/accounts/Login.vue'
import Signup from '@/views/accounts/Signup.vue'
import PasswordFind from '@/views/accounts/PasswordFind.vue'
import PasswordFindEmail from '@/views/accounts/PasswordFindEmail.vue'
import HowToRegisterBaby from '@/views/accounts/HowToRegisterBaby.vue'
import RegisterBaby from '@/views/accounts/RegisterBaby.vue'
import RegisterBabyRelate from '@/views/accounts/RegisterBabyRelate.vue'
import RegisterInviteLink from '@/views/accounts/RegisterInviteLink.vue'
import Diary from '@/views/diaries/Diary.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Diary',
    component: Diary
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/pwfind',
    name: 'PasswordFind',
    component: PasswordFind
  },
  {
    path: '/pwfindemail',
    name: 'PasswordFindEmail',
    component: PasswordFindEmail
  },
  {
    path: '/howtoregisterbaby',
    name: 'HowToRegisterBaby',
    component: HowToRegisterBaby
  },
  {
    path: '/registerbaby',
    name: 'RegisterBaby',
    component: RegisterBaby
  },
  {
    path: '/registerbabyrelate',
    name: 'RegisterBabyRelate',
    component: RegisterBabyRelate
  },
  {
    path: '/registerinvitelink',
    name: 'RegisterInviteLink',
    component: RegisterInviteLink
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
