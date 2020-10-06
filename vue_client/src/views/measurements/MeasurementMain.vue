<template>
  <div>
    <nav class="nav">
      <div class="row no-gutters text-center py-3">
        <router-link class="menu col-4" :to="{name: 'WeightMeasurement'}">몸무게</router-link>
        <router-link class="menu col-4" :to="{name: 'HeightMeasurement'}">키</router-link>
        <router-link class="menu col-4" :to="{name: 'HeadMeasurement'}">머리둘레</router-link>
      </div>
    </nav>

    <router-view></router-view>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MeasurementMain',

  computed: {
    ...mapState(['myaccount', 'currentBaby']),
  },  
}
</script>

<style scoped>

  nav {
  height: 7vh;
  }

  .menu:link, .menu:active, .menu:visited {
    color: black;
    text-decoration: none;
  }

  .menu:hover {
    text-decoration:none;
  }

  .row .router-link-exact-active {
    color: #FEA59C;
    border-bottom: 3px solid #FEA59C;
  }
</style>