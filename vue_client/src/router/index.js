import Vue from 'vue'
import VueRouter from 'vue-router'

// Photos
import PhotoMain from '@/views/photos/PhotoMain'
import PhotoList from '@/views/photos/PhotoList'
import PhotoLibrary from '@/views/photos/PhotoLibrary'
import PhotoSearch from '@/views/photos/PhotoSearch'

// Diary
// import Diary from '@/views/diaries/Diary'

// Babble Box
import Babblebox from '@/views/common/Babblebox'

// Authentication
import Login from '@/views/accounts/Login.vue'
import Signup from '@/views/accounts/Signup.vue'

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
  // Babble Box
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
