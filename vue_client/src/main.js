import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import secrets from './api/secrets.json'

import VueCookies from 'vue-cookies'
Vue.use(VueCookies)

import vueMoment from 'vue-moment' 
Vue.use(vueMoment)

// google login
import GAuth from 'vue-google-oauth2'
const gauthOption = {
  clientId: secrets['OAUTH']['GOOGLE']['CLIENT_ID'],
  scope: 'email profile',
  prompt: 'consent',
  fetch_basic_profile: true
}
Vue.use(GAuth, gauthOption)

// kakao login
window.Kakao.init(secrets['OAUTH']['KAKAO']['CLIENT_ID']);

// firebase
import firebase from 'firebase'
var firebaseConfig = {
  apiKey: secrets['FIREBASE']['SECRET_KEY'],
  authDomain: "babble-98541.firebaseapp.com",
  databaseURL: "https://babble-98541.firebaseio.com",
  projectId: "babble-98541",
  storageBucket: "babble-98541.appspot.com",
  messagingSenderId: "454487413592",
  appId: "1:454487413592:web:b27b00ffc37289ba064b2d",
  measurementId: "G-GK5WMPJZDT"
};
firebase.initializeApp(firebaseConfig);
firebase.analytics();

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
