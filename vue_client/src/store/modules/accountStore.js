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
        postAuthData1({ rootState, commit } , info) {
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
                if (rootState.invitationToken) {
                  router.push({ name: "InvitationConfirm", params: { token: rootState.invitationToken }})
                } else {
                  router.push({name: 'RegisterBaby'})
                }
              })

              .catch(() => {
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
                  title: "아이디와 비밀번호를 확인해주세요"
                })
              })
          },
        postAuthData2({ rootState, commit, dispatch }, info) {
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
                dispatch('findMyAccount', null, { root: true })
                // dispatch('findBaby', rootState.myaccount.current_baby, { root: true })
                if (rootState.invitationToken) {
                  router.push({ name: "InvitationConfirm", params: { token: rootState.invitationToken }})
                } else {
                router.push({name: 'PhotoList'})
                }
              })
              .catch(() => {
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
                  title: "아이디와 비밀번호를 확인해주세요"
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
        enrollBaby({ rootGetters, dispatch }, enrollData) {
          axios.post(SERVER.URL + SERVER.ROUTES.babies, enrollData, rootGetters.config)
            .then(() => {
              dispatch('findMyAccount', null, { root: true })
              // dispatch('findBaby', rootState.myaccount.current_baby, { root: true })
              router.push({ name: 'PhotoList'})
            })

        },
        socialLogin({ commit, dispatch, rootState }, userInfo) {
          axios.post(SERVER.URL + SERVER.ROUTES.social, userInfo)
            .then(res => {
              commit('SET_TOKEN', res.data.key, { root: true });
              dispatch('findMyAccount', null, { root: true })
              const Toast = Swal.mixin({
                toast: true,
                position: "top-end",
                showConfirmButton: false,
                timer: 2000,
                timerProgressBar: true,
                onOpen: (toast) => {
                  toast.addEventListener("mouseenter", Swal.stopTimer);
                  toast.addEventListener("mouseleave", Swal.resumeTimer);
                },
              });
              Toast.fire({
                icon: "success",
                title: "로그인에 성공하였습니다.",
              });
              if (res.data.state === 'login') {
                if (rootState.invitationToken) {
                  router.push({ name: "InvitationConfirm", params: { token: rootState.invitationToken }})
                } else {
                  router.push({name: 'PhotoList'});
                }
              } else if (res.data.state === 'signup') {
                if (rootState.invitationToken) {
                  router.push({ name: "InvitationConfirm", params: { token: rootState.invitationToken }})
                } else {
                  router.push({name: 'RegisterBaby'})
                } 
              }
            })
            .catch((err) => {
              const Toast = Swal.mixin({
                toast: true,
                position: "top-end",
                showConfirmButton: false,
                timer: 2000,
                timerProgressBar: true,
                onOpen: (toast) => {
                  toast.addEventListener("mouseenter", Swal.stopTimer);
                  toast.addEventListener("mouseleave", Swal.resumeTimer);
                },
              });
              Toast.fire({
                icon: "error",
                title: err.response.data.message,
              });
            });
        },
        changePassword({ rootGetters }, passwordData) {
          axios.post(SERVER.URL + SERVER.ROUTES.password + 'change/', passwordData, rootGetters.config)
            .then(() => {
              Swal.fire({
                icon: 'success',
                text: '비밀번호가 변경되었습니다.'
              })
              router.go(0)
            })
            .catch(() => {
              Swal.fire({
                icon: 'error',
                text: '비밀번호를 확인해주세요.'
              })
          })
        },
        changeProfile({ rootGetters, commit }, profileData) {
          axios.put(SERVER.URL + '/accounts/profilechange/', profileData, rootGetters.config)
            .then(res => {
              commit('SET_MYACCOUNT', res.data, { root : true })
              Swal.fire({
                icon: 'success',
                text: '프로필 정보가 변경되었습니다.'
              })
            })
        },
        updateProfile({rootGetters, rootState, commit}, profileUpdateData){
          if(profileUpdateData.newPassWord){
            const passwordData = {
              "old_password": profileUpdateData.currentPassword,
              "new_password1": profileUpdateData.newPassword,
              "new_password2": profileUpdateData.confirmNewPassword
            }
            axios.post(SERVER.URL + SERVER.ROUTES.passwordChange,  passwordData, rootGetters.config)
          }

          if(profileUpdateData.name != rootState.myaccount.name){
            const nameData = {
              "name": profileUpdateData.name
            }
            axios.put(SERVER.URL + SERVER.ROUTES.profileChange, nameData, rootGetters.config)
              .then(res=>{
                commit("SET_MYACCOUNT", res.data, {root:true})
              })
          }
        }
    }
}

export default accountStore