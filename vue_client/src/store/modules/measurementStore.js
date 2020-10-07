import SERVER from '@/api/api'
import axios from 'axios'
// import router from '@/router'

const measurementStore = {
  namespaced: true,
  state: {
    measurementList: null,
    weightMeasurementList: null,
    heightMeasurementList: null,
    headMeasurementList: null,
  },
  getters: {
  },
  mutations: {
    SET_MEASUREMENT_LIST(state, measurements) {
      state.measurementList = measurements 
    },
    SET_WEIGHT_MEASUREMENT_LIST(state, measurements) {
      state.weightMeasurementList = measurements
    },
    SET_HEIGHT_MEASUREMENT_LIST(state, measurements) {
      state.heightMeasurementList = measurements
    },
    SET_HEAD_MEASUREMENT_LIST(state, measurements) {
      state.headMeasurementList = measurements
    },
  },
  actions: {
    fetchMeasurementList({ rootGetters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.babies + SERVER.ROUTES.measurements, rootGetters.config)
        .then(res => commit('SET_MEASUREMENT_LIST', res.data))
    },
    fetchWeightMeasurementList({ rootGetters, commit }) {
      commit('SET_WEIGHT_MEASUREMENT_LIST', null)
      axios.get(SERVER.URL + SERVER.ROUTES.babies + SERVER.ROUTES.measurements + 'weight/', rootGetters.config)
        .then(res => commit('SET_WEIGHT_MEASUREMENT_LIST', res.data))
    },
    fetchHeightMeasurementList({ rootGetters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.babies + SERVER.ROUTES.measurements + 'height/', rootGetters.config)
        .then(res => commit('SET_HEIGHT_MEASUREMENT_LIST', res.data))
    },
    fetchHeadMeasurementList({ rootGetters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.babies + SERVER.ROUTES.measurements + 'head/', rootGetters.config)
        .then(res => commit('SET_HEAD_MEASUREMENT_LIST', res.data))
    },
  }
}

export default measurementStore