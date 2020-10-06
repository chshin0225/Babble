import SERVER from '@/api/api'
import axios from 'axios'
import router from '@/router'
// import Swal from 'sweetalert2'
import firebase from 'firebase'

const photoStore = {
  namespaced: true,
  state: {
    tags: null,
    photos: null,
    photo: null,
    comments: null,
    searchedPhotos: null,
    albums: null,
    album: null,
  },
  getters: {
    albumDataFetched: state => !!state.album,
  },
  mutations: {
    SET_TAGS(state, tags) {
      state.tags = tags
    },
    SET_PHOTOS(state, photos) {
      state.photos = photos
    },
    SET_PHOTO(state, photo) {
      state.photo = photo
    },
    SET_SEARCHED_PHOTOS(state, photo) {
      state.searchedPhotos = photo
    },
    SET_PHOTO_COMMENTS(state, comments) {
      state.comments = comments
    },
    SET_ALBUMS(state, albums) {
      state.albums = albums
    },
    SET_ALBUM(state, album) {
      state.album = album
    },
  },
  actions: {
    fetchTags({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.tags)
        .then(res => {
          commit('SET_TAGS', res.data)
        })
        .catch(err => console.log(err.response.data))
    },

    // photo CRUD
    fetchPhotos({ rootGetters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.photos, rootGetters.config)
        .then(res => {
          commit('SET_PHOTOS', res.data)
        })
        .catch(err => console.error(err))
    },
    findPhoto({ rootGetters, commit }, photoId) {
      axios.get(SERVER.URL + SERVER.ROUTES.photos + photoId + '/',  rootGetters.config)
        .then(res => {
          commit('SET_PHOTO', res.data)
          //router.push({name: 'PhotoDetail', params: { photoId: photoId}})
        })
        .catch(err => console.log(err.response.data))
    },
    createPhotos({ rootState, rootGetters, dispatch }, createInfo) {
      const photoData = []
      const promises = []
      const tagPromises = []
      var storageRef = firebase.storage().ref()

      if (createInfo.photos.length == 1) {
        createInfo.photos.forEach( photo => {
          const uploadTask = storageRef.child('babble_' + rootState.myaccount.current_baby).child(photo.name).put(photo)
          promises.push(uploadTask)
  
          var imageInfo = {
            "image_url": 'babble_' + rootState.myaccount.current_baby + '%2F' + photo.name,
            "temp_url": 'babble_' + rootState.myaccount.current_baby + '/' + photo.name,
            "last_modified": photo.lastModifiedDate,
            "size": photo.size,
            "file_type": photo.type,
            "tags": []
          }
          photoData.push(imageInfo)
        })
        Promise.all(promises).then(() => {
          var imagePath = {
            "path": photoData[0].temp_url
          }
          axios.post(SERVER.AIURL, imagePath)
              .then(res => {
                photoData[0].tags = res.data.tags
                const createData = {
                  "photoData": photoData[0],
                  "photoScope": createInfo.photoScope
                }
                router.push({ name: "TagSelect", params: { createData: createData, photoType: 'create' }})
              })
              .catch(err => console.log(err.response.data))
        })
      } else {
        createInfo.photos.forEach( photo => {
          const uploadTask = storageRef.child('babble_' + rootState.myaccount.current_baby).child(photo.name).put(photo)
          promises.push(uploadTask)
  
          var imageInfo = {
            "image_url": 'babble_' + rootState.myaccount.current_baby + '%2F' + photo.name,
            "temp_url": 'babble_' + rootState.myaccount.current_baby + '/' + photo.name,
            "last_modified": photo.lastModifiedDate,
            "size": photo.size,
            "file_type": photo.type,
            "tags": []
          }
          photoData.push(imageInfo)
        })
  
        // 모든 업로드가 끝난 후 사진들을 fetch 해온다 
        Promise.all(promises).then(() => {
          photoData.forEach(photoInfo => {
            var imagePath = {
              "path": photoInfo.temp_url
            }
            const tagExtract = axios.post(SERVER.AIURL, imagePath)
              .then(res => {
                photoInfo.tags = res.data.tags
              })
              .catch(err => console.log(err.response.data))
            tagPromises.push(tagExtract)
          });

          Promise.all(tagPromises).then(() => {
            const createData = {
              "photoData": photoData,
              "photoScope": createInfo.photoScope
            }
            axios.post(SERVER.URL + SERVER.ROUTES.photos, createData, rootGetters.config)
              .then(() => {
                dispatch('fetchPhotos')
                router.push({name: 'PhotoList'})
              })
              .catch(err => console.log(err.response.data))
          })
        })
      }
    },
    completeCreatePhoto({rootGetters, dispatch}, createData) {
      axios.post(SERVER.URL + SERVER.ROUTES.photos, createData, rootGetters.config)
        .then(() => {
          dispatch('fetchPhotos')
          router.push({name: 'PhotoList'})
        })
        .catch(err => console.log(err.response.data))
    },
    updatePhoto({ rootGetters, commit }, updateData) {
      axios.put(SERVER.URL + SERVER.ROUTES.photos + updateData.id + '/', updateData, rootGetters.config)
        .then(res => {
          commit('SET_PHOTO', res.data)
          router.push({name: 'PhotoDetail', params: { photoId: updateData.id}})
        })
        .catch(err => {
          console.log(err)
      })
    },
    deletePhoto({ rootGetters }, photoId) {
      axios.delete(SERVER.URL + SERVER.ROUTES.photos + photoId + '/', rootGetters.config)
      .then(res => {
          console.log(res)
          router.push({ name: 'PhotoList' })
      })
      .catch(err => {
          console.log(err.response.data)
      })
    },

    // photo comment CRUD
    fetchComments({ rootGetters, commit }, photoId) {
      axios.get(SERVER.URL + SERVER.ROUTES.photos + photoId + '/' + 'comments/',  rootGetters.config)
        .then(res => {
          commit('SET_PHOTO_COMMENTS', res.data)
          //router.push({name: 'PhotoDetail', params: { photoId: photoId}})
        })
        .catch(err => console.log(err.response.data))
    },
    createComment({ rootGetters, dispatch }, commentData) {
      axios.post(SERVER.URL + SERVER.ROUTES.photos + commentData.photo_id + '/comments/', commentData, rootGetters.config)
      .then(res => {
          console.log(res)
          dispatch('fetchComments', commentData.photo_id)
      })
      .catch(err => {
          console.log(err)
      })
    },
    updateComment({ rootGetters, dispatch }, commentData) {
      axios.put(SERVER.URL + SERVER.ROUTES.photos + commentData.photo_id + '/comments/' + commentData.comment_id + '/', commentData.comment, rootGetters.config)
      .then(res => {
          console.log(res)
          dispatch('fetchComments', commentData.photo_id)
      })
      .catch(err => {
          console.log(err.response)
      })
    },
    deleteComment({ rootGetters, dispatch }, commentData) {
      console.log(commentData)
      axios.delete(SERVER.URL + SERVER.ROUTES.photos + commentData.photoId + '/comments/' + commentData.commentId + '/', rootGetters.config)
        .then(res => {
            console.log(res)
            dispatch('fetchComments', commentData.photoId)
        })
        .catch(err => {
            console.log(err)
        })
    },

    // photo search
    searchPhotos({ commit, rootGetters }, keyword) {
      if (keyword == "") {
        commit('SET_SEARCHED_PHOTOS', null)
      } else {
        var info = {
          "keyword": keyword
        }
        axios.post(SERVER.URL + SERVER.ROUTES.searchPhoto, info, rootGetters.config)
        .then(res => {
          commit('SET_SEARCHED_PHOTOS', res.data)
        })
        .catch(err => {
          console.log(err)
        })
      }
    },

    // album CRUD
    fetchAlbums({ commit, rootGetters }) {
      axios.get(SERVER.URL + SERVER.ROUTES.albums, rootGetters.config) 
        .then(res => commit('SET_ALBUMS', res.data))
        .catch(err => console.error(err))
    },
    createAlbum({ rootGetters }, albumData) {
      axios.post(SERVER.URL + SERVER.ROUTES.albums, albumData, rootGetters.config)
        .then(res => {
          let albumId = res.data.id
          router.push({ name: 'AlbumDetail', params: {albumId: albumId}})
        })
        .catch(err => console.error(err))
    },
    getAlbum({ commit, rootGetters }, album_id) {
      commit('SET_ALBUM', null)
      axios.get(SERVER.URL + SERVER.ROUTES.albums + `${album_id}/`, rootGetters.config)
        .then(res => commit('SET_ALBUM', res.data))
        .catch(err => console.error(err))
    },
    deleteAlbum({ rootGetters }, album_id) {
      axios.delete(SERVER.URL + SERVER.ROUTES.albums + `${album_id}/`, rootGetters.config)
        .then(() => router.push({ name: 'AlbumLibrary' }))
        .catch(err => console.error(err))
    },
    deletePhotoFromAlbum({ rootGetters, dispatch }, albumData) {
      axios.put(SERVER.URL + SERVER.ROUTES.albums + `${albumData.albumId}/photo/`, albumData.body, rootGetters.config)
        .then(() => dispatch('getAlbum', albumData.albumId))
        .catch(err => console.error(err))
    },
    editAlbum({ rootGetters }, albumData) {
      console.log(albumData)
      axios.put(SERVER.URL + SERVER.ROUTES.albums + `${albumData.id}/`, albumData, rootGetters.config)
        .then(() => router.push({ name: 'AlbumDetail', params: {albumId: albumData.id}}))
        .catch(err => console.error(err))
    },

  }
}

export default photoStore