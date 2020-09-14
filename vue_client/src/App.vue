<template>
  <div>
    <div id="app">
      <router-view></router-view>
      <!-- footer -->
      <div class="footer row no-gutters">
        <div class="col-4 color-gray" :class="{'color-pink' : isAlbum()}">
          <p><i class="fas fa-images"></i></p>
          <p>Album</p>
        </div>
        <div class="col-4 color-gray" :class="{'color-pink' : isDiary()}">
          <p><i class="fas fa-book"></i></p>
          <p>Diary</p>
        </div>
        <div class="col-4 color-gray" :class="{'color-pink' : isProfile()}">
          <p><i class="fas fa-user"></i></p>
          <p>Profile</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',

  data(){
    return {
      // isAlbum: true,
      // isDiary: false,
      // isProfile: false,
    }
  },
  methods: {
    isAlbum() {
      console.log(this.$route.name)
      if (this.$route.name === 'Album') {
        return true
      } else {
        return false
      }
    },
    isDiary() {
      if (this.$route.name === 'Diary') {
        return true
      } else {
        return false
      }
    },
    isProfile() {
      if (this.$route.name === 'Profile') {
        return true
      } else {
        return false
      }
    }
  }


};
</script>

<style scoped>
.footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: ;
  color: black;
  text-align: center;
  -webkit-box-shadow: 0px -4px 5px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px -4px 5px 0px rgba(0,0,0,0.1);
  box-shadow: 0px -4px 5px 0px rgba(0,0,0,0.1);
}

p {
  margin: 0;
}
</style>
