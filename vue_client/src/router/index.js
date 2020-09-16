import Vue from 'vue'
import VueRouter from 'vue-router'

// Photos
import PhotoMain from '@/views/photos/PhotoMain'
import PhotoList from '@/views/photos/PhotoList'
import PhotoLibrary from '@/views/photos/PhotoLibrary'
import PhotoSearch from '@/views/photos/PhotoSearch'

// Diary
import Diary from '@/views/diaries/Diary'
import DiaryPhoto from '@/views/diaries/DiaryPhoto'
import DiaryCalendar from '@/views/diaries/DiaryCalendar'
import DiaryTimeline from '@/views/diaries/DiaryTimeline'
import DiaryCreate from '@/views/diaries/DiaryCreate'
import DiaryDetail from '@/views/diaries/DiaryDetail'


// Babble Box
import Babblebox from '@/views/common/Babblebox'

// Authentication
import Login from '@/views/accounts/Login.vue'
import Signup from '@/views/accounts/Signup.vue'
import PasswordFind from '@/views/accounts/PasswordFind.vue'
import PasswordFindEmail from '@/views/accounts/PasswordFindEmail.vue'
import HowToRegisterBaby from '@/views/accounts/HowToRegisterBaby.vue'
import RegisterBaby from '@/views/accounts/RegisterBaby.vue'
import RegisterBabyRelate from '@/views/accounts/RegisterBabyRelate.vue'
import RegisterInviteLink from '@/views/accounts/RegisterInviteLink.vue'


Vue.use(VueRouter)

  const routes = [
    // photos
  {
    path: '/photo',
    name: 'PhotoMain',
    component: PhotoMain,
    children: [
      {
        path: '',
        component: PhotoList,
        name: 'PhotoList'
      },
      {
        path: 'library',
        component: PhotoLibrary,
        name: 'PhotoLibrary'
      },
      {
        path: 'search',
        component: PhotoSearch,
        name: 'PhotoSearch'
      },
    ]
  },
  // Authentication
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

  // Babble Box
  {
    path: '/babblebox',
    name: 'Babblebox',
    component: Babblebox
  },
  // Diary
  {
    path: '/diary',
    name: 'Diary',
    component: Diary,
    children: [
      {
        path: '',
        component: DiaryPhoto,
        name: 'DiaryPhoto'
      },
      {
        path: 'calendar',
        component: DiaryCalendar,
        name: 'DiaryCalendar'
      },
      {
        path: 'timeline',
        component: DiaryTimeline,
        name: 'DiaryTimeline'
      },
    ]
  },
  {
    path: '/diary/create', 
    name: 'DiaryCreate',
    component: DiaryCreate
  },
  {
    path: '/diary/:diaryId',
    name: 'DiaryDetail',
    component: DiaryDetail
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
