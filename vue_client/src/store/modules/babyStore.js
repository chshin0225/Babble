import SERVER from '@/api/api'
import axios from 'axios'
//import router from '@/router'
import Swal from 'sweetalert2'
//import firebase from 'firebase'

const babyStore = {
  namespaced: true,
  state: {
  },
  getters: {
    
  },
  mutations: {
  },
  actions: {
    
    modifyBaby({ rootGetters }, enrollData) {
      axios.put(SERVER.URL + SERVER.ROUTES.babies + enrollData.id + '/', enrollData, rootGetters.config)
      .then(() => {
          Swal.fire({
            icon: 'success',
            text: '수정되었습니다.'
          })
      })
    },
  }
}

export default babyStore