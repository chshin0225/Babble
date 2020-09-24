<template>

  <div>
    <!-- <div class="nav">
      <div class="row no-gutters text-center py-3">
        <router-link class="menu col-4" :to="{name: 'BabySetting'}">아기 설정</router-link>
        <router-link class="menu col-4" :to="{name: 'GroupSetting'}">그룹 설정</router-link>
      </div>
    </div>
    <router-view></router-view> -->
    <div class="buttons mt-2">
      <button class="btn setting-button" @click="clickBabySetting">아기 설정</button>
    </div>
    <div class="buttons mt-2">
      <button class="btn setting-button" @click="clickGroupSetting">그룹 설정</button>
    </div>
  </div>
</template>

<script>


export default {
  name: 'Settings',
  methods:{
    clickBabySetting(){
      this.$router.push({ name: 'BabySetting'})
    },
    clickGroupSetting(){
      this.$router.push({ name: 'GroupSetting'})
    }
  }
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

.setting-button{
  background-color: #FEA59C;
  color: #F8F8F8;
  width: 100%;
}


</style>