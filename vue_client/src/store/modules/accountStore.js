import SERVER from '@/api/api'
import axios from 'axios'
import router from '@/router'
import Swal from 'sweetalert2'


const accountStore = {
    namespaced: true,
    state: {

    },
    getters: {

    },
    mutations: {

    },
    actions: {
        postAuthData1({ commit } , info) {
            axios.post(SERVER.URL + SERVER.ROUTES.signup, info.data)
              .then(res => {
                commit('SET_TOKEN', res.data.key, { root: true })
                const Toast = Swal.mixin({
                  toast: true,
                  position: 'top-end',
                  showConfirmButton: false,
                  timer: 2000,
                  timerProgressBar: true,
                  onOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                    }
                 })
                 Toast.fire({
                  icon: 'success',
                  title: "회원가입에 성공하였습니다."
                })
      
                router.push({name: 'PhotoList'})
              })

              .catch(err => {
                console.log(err.response)
                const Toast = Swal.mixin({
                  toast: true,
                  position: 'top-end',
                  showConfirmButton: false,
                  timer: 3000,
                  timerProgressBar: false,
                  onOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                    }
                 })
                 Toast.fire({
                  icon: 'error',
                  title: err.response.data.message
                })
              })
          },
        postAuthData2({ commit }, info) {
            axios.post(SERVER.URL + SERVER.ROUTES.login, info.data)
              .then(res => {
                commit('SET_TOKEN', res.data.key, { root: true })
                const Toast = Swal.mixin({
                  toast: true,
                  position: 'top-end',
                  showConfirmButton: false,
                  timer: 2000,
                  timerProgressBar: true,
                  onOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                    }
                 })
                 Toast.fire({
                  icon: 'success',
                  title: "로그인에 성공하였습니다."
                })
      
                router.push({name: 'PhotoList'})
              })
              .catch(err => {
                console.log(err.response)
                const Toast = Swal.mixin({
                  toast: true,
                  position: 'top-end',
                  showConfirmButton: false,
                  timer: 3000,
                  timerProgressBar: false,
                  onOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                    }
                 })
                 Toast.fire({
                  icon: 'error',
                  title: err.response
                })
              })
          },
        // login
        login({ dispatch }, loginData) {
            const info = {
              data: loginData,
              location: SERVER.ROUTES.login,
            }
            dispatch('postAuthData2', info)
        },
        signup({ dispatch }, signupData) {
          const info = {
            data: signupData,
            location: SERVER.ROUTES.signup,
          }
          dispatch('postAuthData1', info)
        },
        enrollBaby({ rootGetters }, enrollData) {
          console.log(enrollData)
          axios.post(SERVER.URL + SERVER.ROUTES.babies, enrollData, rootGetters.config)
            .then(res => {
              console.log(res)
              router.push({ name: 'PhotoList'})
            })
            .catch(err => {
              console.error(err)
            })
        }
    }
}

export default accountStore