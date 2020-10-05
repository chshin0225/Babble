//import SERVER from '@/api/api'
//import axios from 'axios'


const profileStore = {
    namespaced: true,
    state: {

    },
    getters: {

    },
    mutations: {

    },
    actions: {
        testAction(root, d){
            console.log(root)
            console.log(d)
            console.log("action!!")
        }
    }
}

export default profileStore