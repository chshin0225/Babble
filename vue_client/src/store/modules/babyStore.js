import SERVER from '@/api/api'
import axios from 'axios'
//import router from '@/router'
// import Swal from 'sweetalert2'
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
      .then(res => {
          console.log(res)
      })
      .catch(err => {
          console.log(err)
      })
    },
  }
}

export default babyStore