import Vue from 'vue'
import Vuex from 'vuex'

import accountStore from '@/store/modules/accountStore'
import diaryStore from '@/store/modules/diaryStore'
import photoStore from '@/store/modules/photoStore'

import cookies from 'vue-cookies'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authToken: cookies.get('auth-token'),
  },
  getters: {
    config: state => ({ headers: { Authorization: `Token ${state.authToken}`}}),
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.authToken = token
      cookies.set('auth-token', token)
    },
  },
  actions: {
  },
  modules: {
    accountStore: accountStore,
    diaryStore: diaryStore,
    photoStore: photoStore,
  }
})

// save our state (isPanel open or not) 
export const store = Vue.observable({
  isNavOpen: false
});

// We call toggleNav anywhere we need it in our app
export const mutations = {
  setIsNavOpen(yesno) {
    store.isNavOpen = yesno;
  },
  toggleNav() {
      store.isNavOpen = !store.isNavOpen
  }
};
