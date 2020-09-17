import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';

// firebase
import firebase from 'firebase'

var firebaseConfig = {
  apiKey: "AIzaSyBdMcBm_CrI9gGx0F-kjU6Q-Rxah0Q99z0",
  authDomain: "babble-20baf.firebaseapp.com",
  databaseURL: "https://babble-20baf.firebaseio.com",
  projectId: "babble-20baf",
  storageBucket: "babble-20baf.appspot.com",
  messagingSenderId: "29022455607",
  appId: "1:29022455607:web:5fffe19e5c4cff42af7cb2",
  measurementId: "G-FQ6ZNW45P8"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
