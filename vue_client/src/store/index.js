import Vue from 'vue'
import Vuex from 'vuex'

import accountStore from '@/store/modules/accountStore'
import diaryStore from '@/store/modules/diaryStore'
import photoStore from '@/store/modules/photoStore'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
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
