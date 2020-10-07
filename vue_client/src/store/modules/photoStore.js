import SERVER from '@/api/api'
import axios from 'axios'
import router from '@/router'
// import Swal from 'sweetalert2'
import firebase from 'firebase'

const photoStore = {
  namespaced: true,
  state: {
    tags: [],
    emotionTagPhotos: [],
    babbleboxTags: [],
    photos: [],
    photo: null,
    comments: null,
    searchedPhotos: [],
    albums: null,
    album: null,
    albumPhotos: null,
    albumPhotoIdList: [],
    measurementList: [],
  },
  getters: {
    albumDataFetched: state => !!state.album,
    albumPhotoIdListFetched: state => !!state.albumPhotoIdList,
  },
  mutations: {
    SET_TAGS(state, tags) {
      state.tags = tags
    },
    SET_EMOTION_PHOTOS(state, emotionTagPhotos) {
      state.emotionTagPhotos = emotionTagPhotos
    },
    SET_BABBLEBOX_TAGS(state, babbleboxTags) {
      state.babbleboxTags = babbleboxTags
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
    SET_ALBUM_PHOTO_ID_LIST(state, albumPhotoIdList) {
      state.albumPhotoIdList = albumPhotoIdList
    },
    SET_ALBUM_PHOTOS(state, photos) {
      state.albumPhotos = photos
    },
    SET_MEASUREMENT_LIST(state, measurements) {
      state.measurementList = measurements 
    },
  },
  actions: {
    fetchTags({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.tags)
        .then(res => commit('SET_TAGS', res.data))
    },
    fetchEmotionTagPhotos({ rootGetters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.emotionTags, rootGetters.config)
        .then(res => commit('SET_EMOTION_PHOTOS', res.data))
    },
    fetchBabbleboxTags({ rootGetters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.babbleboxTags, rootGetters.config)
        .then(res => commit('SET_BABBLEBOX_TAGS', res.data))
    },


    // photo CRUD
    fetchPhotos({ rootGetters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.photos, rootGetters.config)
        .then(res => {
          commit('SET_PHOTOS', res.data)
        })
    },
    findPhoto({ rootGetters, commit }, photoId) {
      axios.get(SERVER.URL + SERVER.ROUTES.photos + photoId + '/',  rootGetters.config)
        .then(res => {
          commit('SET_PHOTO', res.data)
          //router.push({name: 'PhotoDetail', params: { photoId: photoId}})
        })
    },
    createPhotos({ rootState, rootGetters, dispatch }, createInfo) {
      const photoData = []
      const promises = []
      const tagPromises = []
      var storageRef = firebase.storage().ref()

      if (createInfo.photos.length == 1) {
        createInfo.photos.forEach(photo => {
          const uploadTask = storageRef.child('babble_' + rootState.myaccount.current_baby).child(photo.name).put(photo)
          promises.push(uploadTask)
  
          var imageInfo = {
            "image_url": 'babble_' + rootState.myaccount.current_baby + '%2F' + photo.name,
            "temp_url": 'babble_' + rootState.myaccount.current_baby + '/' + photo.name,
            "last_modified": photo.lastModifiedDate,
            "size": photo.size,
            "file_type": photo.type,
            "tags": [],
            "photo_scope": createInfo.photo_scope,
            "groups": createInfo.groups
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
                router.push({ name: "TagSelect", params: { createData: photoData[0], photoType: 'create' }})
              })
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
            "tags": [],
            "photo_scope": createInfo.photo_scope,
            "groups": createInfo.groups
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
            tagPromises.push(tagExtract)
          });

          Promise.all(tagPromises).then(() => {
            axios.post(SERVER.URL + SERVER.ROUTES.photos, photoData, rootGetters.config)
              .then(() => {
                dispatch('fetchPhotos')
                router.push({name: 'PhotoList'})
              })
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
    },
    updatePhoto({ rootGetters, commit }, updateData) {
      axios.put(SERVER.URL + SERVER.ROUTES.photos + updateData.id + '/', updateData, rootGetters.config)
        .then(res => {
          commit('SET_PHOTO', res.data)
          router.replace({name: 'PhotoDetail', params: { photoId: updateData.id}})
        })
    },
    deletePhoto({ rootGetters }, photoId) {
      axios.delete(SERVER.URL + SERVER.ROUTES.photos + photoId + '/', rootGetters.config)
      .then(() => {
          router.push({ name: 'PhotoList' })
      })
    },

    // photo comment CRUD
    fetchComments({ rootGetters, commit }, photoId) {
      axios.get(SERVER.URL + SERVER.ROUTES.photos + photoId + '/' + 'comments/',  rootGetters.config)
        .then(res => {
          commit('SET_PHOTO_COMMENTS', res.data)
        })
    },
    createComment({ rootGetters, dispatch }, commentData) {
      axios.post(SERVER.URL + SERVER.ROUTES.photos + commentData.photo_id + '/comments/', commentData, rootGetters.config)
      .then(() => {
          dispatch('fetchComments', commentData.photo_id)
      })
    },
    updateComment({ rootGetters, dispatch }, commentData) {
      axios.put(SERVER.URL + SERVER.ROUTES.photos + commentData.photo_id + '/comments/' + commentData.comment_id + '/', commentData.comment, rootGetters.config)
      .then(() => {
          dispatch('fetchComments', commentData.photo_id)
      })
    },
    deleteComment({ rootGetters, dispatch }, commentData) {
      axios.delete(SERVER.URL + SERVER.ROUTES.photos + commentData.photoId + '/comments/' + commentData.commentId + '/', rootGetters.config)
        .then(() => {
            dispatch('fetchComments', commentData.photoId)
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
      }
    },

    // album CRUD
    fetchAlbums({ commit, rootGetters }) {
      axios.get(SERVER.URL + SERVER.ROUTES.albums, rootGetters.config) 
        .then(res => commit('SET_ALBUMS', res.data))
    },
    createAlbum({ rootGetters }, albumData) {
      axios.post(SERVER.URL + SERVER.ROUTES.albums, albumData, rootGetters.config)
        .then(res => {
          let albumId = res.data.id
          router.push({ name: 'AlbumDetail', params: {albumId: albumId}})
        })
    },
    getAlbum({ commit, rootGetters }, album_id) {
      commit('SET_ALBUM', null)
      axios.get(SERVER.URL + SERVER.ROUTES.albums + `${album_id}/`, rootGetters.config)
        .then(res => commit('SET_ALBUM', res.data))
    },
    fetchAlbumPhotoIds({ commit, rootGetters }, album_id) {
      axios.get(SERVER.URL + SERVER.ROUTES.albums + `${album_id}/photo/simple/`, rootGetters.config)
        .then(res => commit('SET_ALBUM_PHOTO_ID_LIST', res.data))
    },
    fetchAlbumPhotos({ commit, rootGetters }, album_id) {
      axios.get(SERVER.URL + SERVER.ROUTES.albums + `${album_id}/photo/`, rootGetters.config)
        .then(res => commit('SET_ALBUM_PHOTOS', res.data))
    },
    deleteAlbum({ rootGetters }, album_id) {
      axios.delete(SERVER.URL + SERVER.ROUTES.albums + `${album_id}/`, rootGetters.config)
        .then(() => router.push({ name: 'AlbumLibrary' }))
    },
    addPhotoToAlbum({ rootGetters }, albumData) {
      axios.post(SERVER.URL + SERVER.ROUTES.albums + `${albumData.albumId}/photo/`, albumData.body, rootGetters.config)
        .then(() => router.push({ name: 'AlbumEdit', params: {albumId: albumData.albumId}}))
    },
    deletePhotoFromAlbum({ rootGetters, dispatch }, albumData) {
      axios.put(SERVER.URL + SERVER.ROUTES.albums + `${albumData.albumId}/photo/`, albumData.body, rootGetters.config)
        .then(() => dispatch('fetchAlbumPhotos', albumData.albumId))
    },
    editAlbum({ rootGetters }, albumData) {
      axios.put(SERVER.URL + SERVER.ROUTES.albums + `${albumData.id}/`, albumData, rootGetters.config)
        .then(() => router.push({ name: 'AlbumDetail', params: {albumId: albumData.id}}))
    },

  }
}

export default photoStore