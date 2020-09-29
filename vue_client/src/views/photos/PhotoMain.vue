<template>
  <div>
    <nav class="nav">
      <div class="row no-gutters text-center py-3">
        <router-link class="menu col-4" :to="{name: 'PhotoList'}">전체 사진</router-link>
        <router-link class="menu col-4" :to="{name: 'AlbumLibrary'}">라이브러리</router-link>
        <router-link class="menu col-4" :to="{name: 'PhotoSearch'}"><i class="fas fa-search"></i></router-link>
      </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>


export default {
  name: 'PhotoMain',
  /*mounted() {
    this.$router.push({name: 'PhotoList'})
  }*/
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