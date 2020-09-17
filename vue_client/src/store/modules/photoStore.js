import SERVER from '@/api/api'
import axios from 'axios'
import router from '@/router'
// import Swal from 'sweetalert2'
import firebase from 'firebase'

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
    createPhotos({ rootState, rootGetters }, photos) {
      const createData = []
      var storageRef = firebase.storage().ref();
      for (var photo of photos) {
        storageRef.child('babble_' + rootState.myaccount.id).child(photo.name).put(photo)
        
        var imageInfo = {
          "image_url": 'babble_' + rootState.myaccount.id + '%2F' + photo.name,
          "last_modified": photo.lastModifiedDate,
          "size": photo.size,
          "file_type": photo.type
        }
        createData.push(imageInfo)
      }
      axios.post(SERVER.URL + SERVER.ROUTES.photos, createData, rootGetters.config)
        .then(() => {
          router.push({name: 'PhotoList'})
        })
        .catch(err => console.log(err.response.data))
      },
  }
}

export default photoStore