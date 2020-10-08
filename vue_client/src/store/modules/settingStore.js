import SERVER from '@/api/api'
import axios from 'axios'
//import router from '@/router'
import Swal from 'sweetalert2'


const settingStore = {
  namespaced: true,
  state: {
    groups: null,
    users: null,
  },
  getters: {
    
  },
  mutations: {
    SET_GROUPS(state, groups) {
      state.groups = groups
    },
    SET_USERS(state, users) {
      state.users = users
    },
  },
  actions: {
    fetchUsers({ rootGetters, commit }) { //현재 babble box 내 존재하는 유저 목록 조회
      axios.get(SERVER.URL + SERVER.ROUTES.babies + 'relationships/', rootGetters.config)
        .then(res => {
          var master = []
          var maintainers = []
          var guests = []
          for(var i=0; i<res.data.length; i++){
            if (res.data[i].rank === 1) {
              master.push(res.data[i])
            } else if (res.data[i].rank === 2) {
              maintainers.push(res.data[i])
            } else {
              res.data[i].isCheck = false;
              guests.push(res.data[i])
            }
          }
          var total  = {
            "master" : master,
            "maintainers" : maintainers,
            "guests": guests
          } 
          commit('SET_USERS', total)
        })
    },
    fetchGroups({ rootGetters, commit }) { //현재 babble box 내 존재하는 그룹 및 그룹에 속한 유저 목록 조회
      axios.get(SERVER.URL + SERVER.ROUTES.groups, rootGetters.config)
        .then(res => commit('SET_GROUPS', res.data))
    },
    addUser({ rootGetters }, userData) {
      axios.put(SERVER.URL + SERVER.ROUTES.groups + userData.groupId + '/', userData, rootGetters.config)
        .then(() => {
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
              title: "그룹에 추가되었습니다."
            })
        })
    },
    deleteGroupUser({ rootGetters, dispatch }, userData) {
      axios.post(SERVER.URL + SERVER.ROUTES.groups + userData.groupId + '/', userData, rootGetters.config)
        .then(() => dispatch('fetchGroups'))
    },
    modifyGroup({ rootGetters }, groupData) {
      axios.put(SERVER.URL + SERVER.ROUTES.groups + groupData.groupId + '/info/', groupData, rootGetters.config)
    },
    createGroup({ rootGetters }, groupData) {
      axios.post(SERVER.URL + SERVER.ROUTES.groups, groupData, rootGetters.config)
    },
    modifyUserRank({ rootGetters, dispatch }, userData) {
      axios.put(SERVER.URL + SERVER.ROUTES.babies + 'relationships/' + userData.userId + '/', userData, rootGetters.config)
      .then(() => {
          dispatch("fetchUsers")
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
            title: "유저 권한을 변경하였습니다."
          })
      })
    },
    deleteBabbleUser({ rootGetters }, userData){
      axios.delete(SERVER.URL + SERVER.ROUTES.babies + 'relationships/' + userData.userId + '/', rootGetters.config)
        .then(() => {
          Swal.fire({
            icon: 'success',
            text: '그룹에서 삭제되었습니다.'
          })
        })
        .catch(() => {
          Swal.fire({
            icon: 'error',
            text: '오류가 발생했습니다.'
          })
        })

    },
    deleteBabbleGroup({ rootGetters }, groupData){
      axios.delete(SERVER.URL + SERVER.ROUTES.groups + groupData.groupId + '/info/', rootGetters.config)
    },
  }
}

export default settingStore