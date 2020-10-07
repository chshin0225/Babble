import SERVER from '@/api/api'
import axios from 'axios'
import router from '@/router'
// import Swal from 'sweetalert2'


const diaryStore = {
    namespaced: true,
    state: {
        diary: null,
        diaries: null,
        photoDiaries: null,
        diaryId: null,
        comments: null,
        measurments: null,
    },
    getters: {
    },
    mutations: {
        SET_DIARY(state, diary) {
            state.diary = diary
        },
        SET_DIARIES(state, diaries) {
            state.diaries = diaries
        },
        SET_PHOTO_DIARIES(state, photoDiaries) {
            state.photoDiaries = photoDiaries
        },
        SET_COMMENTS(state, comments) {
            state.comments = comments
        },
        SET_MEASUREMENTS(state, measurements) {
            state.measurements = measurements
        }
    },
    actions: {
        createDiary({ rootGetters }, diaryData) {
            axios.post(SERVER.URL + SERVER.ROUTES.diaries, diaryData, rootGetters.config)
                .then(res => {
                    router.push({ name: 'DiaryDetail', params: { diaryId: res.data.id } })
                })
                .catch(err => {
                    console.log(err)
                })
        },
        fetchPhotoDiaries({ rootGetters, commit }) {
            axios.get(SERVER.URL + SERVER.ROUTES.diaries + SERVER.ROUTES.photo , rootGetters.config)
                .then(res => {
                    commit('SET_PHOTO_DIARIES', res.data)
                })
                .catch(err => {
                    console.log(err.response)
                })
        },
        fetchDiaries({ rootGetters, commit }) {
            axios.get(SERVER.URL + SERVER.ROUTES.diaries, rootGetters.config)
                .then(res => {
                    commit('SET_DIARIES', res.data)
                })
                .catch(err => {
                    console.log(err.response)
                })
        },
        findDiary({ rootGetters, commit }, diaryId) {
            axios.get(SERVER.URL + SERVER.ROUTES.diaries + diaryId + '/', rootGetters.config)
                .then(res => {
                    commit('SET_DIARY', res.data)
                })
                .catch(err => {
                    console.log(err)
                })
        },
        deleteDiary({ rootGetters }, diaryId) {
            axios.delete(SERVER.URL + SERVER.ROUTES.diaries + diaryId, rootGetters.config)
                .then(() => {
                    router.push({ name: 'DiaryPhoto' })
                })
                .catch(err => {
                    console.log(err.response.data)
                })
        },
        updateDiary({ rootGetters }, diaryData) {
            axios.put(SERVER.URL + SERVER.ROUTES.diaries + diaryData.diaryId + '/', diaryData.diaryUpdateData, rootGetters.config)
                .then(() => {
                    router.push({ name: 'DiaryDetail', params: { diaryId: diaryData.diaryId } })
                })
                .catch(err => {
                    console.log(err.response)
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
            axios.post(SERVER.URL + SERVER.ROUTES.diaries + commentData.diaryId + '/comments/', commentData, rootGetters.config)
                .then(() => {
                    dispatch('fetchComments', commentData.diaryId)
                })
                .catch(err => {
                    console.log(err.response)
                })
        },
        deleteComment({ dispatch, rootGetters }, commentData) {
            axios.delete(SERVER.URL + SERVER.ROUTES.diaries + commentData.diaryId + SERVER.ROUTES.comments + commentData.commentId + '/', rootGetters.config)
                .then(() => {
                    dispatch('fetchComments', commentData.diaryId)
                })
                .catch(err => {
                    console.log(err.response.data)
                })
        },
        updateComment({ dispatch, rootGetters }, commentUpdateData) {
            axios.put(SERVER.URL + SERVER.ROUTES.diaries + commentUpdateData.diaryId + SERVER.ROUTES.comments + commentUpdateData.commentId + '/', commentUpdateData, rootGetters.config)
                .then(() => {
                    dispatch('fetchComments', commentUpdateData.diaryId)
                })
                .catch(err => {
                    console.log(err.response)
                })
        },
        createRecord({ rootGetters }, babyRecord) {
            axios.post(SERVER.URL + SERVER.ROUTES.babies + SERVER.ROUTES.measurements, babyRecord, rootGetters.config)
                .then((res) => {
                    console.log(res.data)
                })
                .catch(err => {
                    console.log(err.response)
                })
        },
        updateMeasurement({ rootGetters }, recordData) {
            axios.put(SERVER.URL + SERVER.ROUTES.babies + SERVER.ROUTES.measurements + recordData.measurement_id + '/', recordData.babyRecord, rootGetters.config)
                .then((res) => {
                    console.log(res.data)
                })
                .catch(err => {
                    console.log(err.response)
                })
        },
        fetchMeasurements({ rootGetters, commit }) {
            console.log(SERVER.URL + SERVER.ROUTES.babies + SERVER.ROUTES.measurements)
            axios.get(SERVER.URL + SERVER.ROUTES.babies + SERVER.ROUTES.measurements, rootGetters.config)
            .then((res) => {
                commit('SET_MEASUREMENTS', res.data)
            })
            .catch(err => {
                console.log(err.response)
            })
        },        
    }
}

export default diaryStore