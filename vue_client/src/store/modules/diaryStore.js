import SERVER from '@/api/api'
import axios from 'axios'
import router from '@/router'
// import Swal from 'sweetalert2'


const diaryStore = {
    namespaced: true,
    state: {
        diary: null,
    },
    getters: {
    },
    mutations: {
        SET_DIARY(state, diary) {
            state.diary = diary
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
           axios.get(SERVER.URL + SERVER.ROUTES.diaries + diaryId, null, rootGetters.config)
            .then(res => {
                commit('SET_DIARY', res.data)
                console.log("RES DATA",res.data)
            })
            .catch(err => {
                console.log(err)
            })
       }
    }
}

export default diaryStore