<template>
  <div class="box">
    <div class="nav">
      <div class="nav-container d-flex bg-pink">
        <router-link :to="{ name: 'DiaryPhoto'}" class="view right-outline pointer">
          <i class="fas fa-file-image fa-2x"></i>
        </router-link>
        <router-link :to="{ name: 'DiaryTimeline'}" class="view right-outline pointer">
          <i class="fas fa-stream fa-2x"></i>
        </router-link>
        <router-link :to="{ name: 'DiaryCalendar'}" class="view pointer">
          <i class="fas fa-calendar-alt fa-2x"></i>
        </router-link>
      </div>
    </div>
    
    <!-- router-view -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'Diary'
}
</script>

<style scoped>
.box {
  padding: 20px;
}

.nav-container {
  border-radius: 0.5rem;
}

.fas {
  padding: 0.5rem;
}


.right-outline {
  border-right: 1px solid white; 
}

.view:link, .view:active, .view:visited {
  color:white;
  text-decoration: none;
}


.nav-container .router-link-exact-active {
  color: #9BC7FF
}


</style>