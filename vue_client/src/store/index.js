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
