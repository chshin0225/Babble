import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import VueCookies from 'vue-cookies'
import secrets from './api/secrets.json'
// firebase
import firebase from 'firebase'

var firebaseConfig = {
  apiKey: secrets['SECRET_KEY'],
  authDomain: "babble-98541.firebaseapp.com",
  databaseURL: "https://babble-98541.firebaseio.com",
  projectId: "babble-98541",
  storageBucket: "babble-98541.appspot.com",
  messagingSenderId: "454487413592",
  appId: "1:454487413592:web:b27b00ffc37289ba064b2d",
  measurementId: "G-GK5WMPJZDT"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();


Vue.use(VueCookies)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
