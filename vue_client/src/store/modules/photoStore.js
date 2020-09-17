import SERVER from '@/api/api'
import axios from 'axios'
import router from '@/router'
// import Swal from 'sweetalert2'


const photoStore = {
  namespaced: true,
  state: {
    photos: null,
    selectedPhoto: null,
  },
  getters: {
    
  },
  mutations: {
    SET_PHOTOS(state, photos) {
      state.photos = photos
    },
    SET_SELECTED_PHOTO(state, photo) {
      state.photo = photo
    }
  },
  actions: {
    fetchPhotos({ rootGetters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.photos, rootGetters.config)
        .then(res => {
          commit('SET_PHOTOS', res.data)
        })
        .catch(err => console.log(err.response.data))
    },
    findPhoto({ rootGetters, commit }, photoId) {
      axios.get(SERVER.URL + SERVER.ROUTES.photos + photoId + '/',  rootGetters.config)
        .then(res => {
          commit('SET_SELECTED_PHOTO', res.data)
          router.push({name: 'PhotoDetail', params: { photoId: photoId}})
        })
        .catch(err => console.log(err.response.data))
    },
    createPhotos({ rootGetters }, photos) {
      axios.post(SERVER.URL + SERVER.ROUTES.photos, photos, rootGetters.config)
        .then(() => {
          router.push({name: 'PhotoList'})
        })
        .catch(err => console.log(err.response.data))
      },
  }
}

export default photoStore