<template>

  <div>
    <div class="nav">
      <div class="row no-gutters text-center py-3">
        <router-link class="menu col-6" :to="{name: 'UserEdit'}">회원 편집</router-link>
        <router-link class="menu col-6" :to="{name: 'GroupEdit'}">그룹 편집</router-link>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>


export default {
  name: 'GroupSetting',
}
</script>

<style scoped>
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