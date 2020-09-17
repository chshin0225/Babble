import SERVER from '@/api/api'
import axios from 'axios'
import router from '@/router'
// import Swal from 'sweetalert2'


const diaryStore = {
    namespaced: true,
    state: {

    },
    getters: {

    },
    mutations: {

    },
    actions: {
        createDiary({ rootGetters }, diaryData) {
            axios.post(SERVER.URL + SERVER.ROUTES.diaries, diaryData, rootGetters.config)
                .then(res => {
                    console.log(res)
                    router.push({ name: 'DiaryPhoto '})
                })
                .catch(err => {
                    console.log(err)
                })
       }
    }
}

export default diaryStore