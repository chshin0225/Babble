import SERVER from '@/api/api'
import axios from 'axios'
import router from '@/router'
// import Swal from 'sweetalert2'


const diaryStore = {
    namespaced: true,
    state: {
        diary: null,
        comments: null,
    },
    getters: {
    },
    mutations: {
        SET_DIARY(state, diary) {
            state.diary = diary
        },
        SET_COMMENTS(state, comments) {
            state.comments = comments
        }
    },
    actions: {
        createDiary({ rootGetters }, diaryData) {
            axios.post(SERVER.URL + SERVER.ROUTES.diaries, diaryData, rootGetters.config)
                .then(res => {
                    router.push({ name: 'DiaryDetail', params: {diaryId: res.data.id}})
                })
                .catch(err => {
                    console.log(err)
                })
       },
       findDiary({ rootGetters, commit }, diaryId) {
           axios.get(SERVER.URL + SERVER.ROUTES.diaries + diaryId +'/' , rootGetters.config)
            .then(res => {
                commit('SET_DIARY', res.data)
                console.log("RES DATA",res.data)
            })
            .catch(err => {
                console.log(err)
            })
       },
       fetchComments({ rootGetters, commit }, diaryId) {
           axios.get(SERVER.URL + SERVER.ROUTES.diaries + diaryId + '/comments/', rootGetters.config)
            .then(res => {
                commit('SET_COMMENTS', res.data)
            })
            .catch(err => {
                console.log(err)
            })
       },
       createComment({ dispatch, rootGetters }, commentData) {
           console.log(commentData)
           axios.post(SERVER.URL + SERVER.ROUTES.diaries + commentData.diaryId + '/comments/', commentData, rootGetters.config)
           .then(res => {
               console.log(res)
               dispatch('fetchComments', commentData.diaryId)
           })
           .catch(err => {
               console.log(err.response)
           })
       }
    }
}

export default diaryStore