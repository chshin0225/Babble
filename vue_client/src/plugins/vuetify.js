import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

import ko from 'vuetify/es5/locale/ko'

Vue.component('my-component', {
    methods: {
      changeLocale () {
        this.$vuetify.lang.current = 'ko'
      },
    },
  })

export default new Vuetify({
    lang: {
        locales: { ko },
        current: 'ko'
    }
});
