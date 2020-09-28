import SERVER from '@/api/api'
import axios from 'axios'
import router from '@/router'
// import Swal from 'sweetalert2'
//import firebase from 'firebase'

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
          commit('SET_USERS', res.data)
        })
        .catch(err => console.log(err.response.data))
    },
    fetchGroups({ rootGetters, commit }) { //현재 babble box 내 존재하는 그룹 및 그룹에 속한 유저 목록 조회
      axios.get(SERVER.URL + SERVER.ROUTES.groups, rootGetters.config)
        .then(res => {
          commit('SET_GROUPS', res.data)
        })
        .catch(err => console.log(err.response.data))
    },
    addUser({ rootGetters }, userData) {
      
      axios.post(SERVER.URL + SERVER.ROUTES.groups + userData.groupId + '/', userData, rootGetters.config)
      .then(res => {
          console.log(res)
          //router.go(0)
      })
      .catch(err => {
          console.log(err)
      })
    },
    deleteGroupUser({ rootGetters }, userData) {
      axios.delete(SERVER.URL + SERVER.ROUTES.groups + userData.groupId + '/', userData, rootGetters.config)
      .then(res => {
          console.log(res)
          router.go(0)
      })
      .catch(err => {
          console.log(err)
      })
    },
    modifyGroup({ rootGetters }, groupData) {
      axios.put(SERVER.URL + SERVER.ROUTES.groups + groupData.groupId + '/info/', groupData, rootGetters.config)
      .then(res => {
          console.log(res)
          router.go(0)
      })
      .catch(err => {
          console.log(err)
      })
    },
    createGroup({ rootGetters }, groupData) {
      axios.post(SERVER.URL + SERVER.ROUTES.groups, groupData, rootGetters.config)
        .then(res => {
          console.log(res)
          router.go(0)
        })
        .catch(err => {
          console.log(err.response)
        })
    },
    modifyUserRank({ rootGetters }, userData) {
      axios.put(SERVER.URL + SERVER.ROUTES.babies + 'relationships/' + userData.userId + '/', userData, rootGetters.config)
      .then(res => {
          console.log(res)
      })
      .catch(err => {
          console.log(err)
      })
    },
    deleteBabbleUser({ rootGetters }, userData){
      axios.delete(SERVER.URL + SERVER.ROUTES.babies + 'relationships/' + userData.userId + '/', rootGetters.config)
      .then(res => {
          console.log(res)
          router.go(0)
      })
      .catch(err => {
          console.log(err)
      })

    },
    deleteBabbleGroup({ rootGetters }, groupData){
      axios.delete(SERVER.URL + SERVER.ROUTES.groups + groupData.groupId + '/info/', rootGetters.config)
      .then(res => {
          console.log(res)
          router.go(0)
      })
      .catch(err => {
          console.log(err)
      })

    }
  }
}

export default settingStore