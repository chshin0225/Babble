<template>
  <div class="box">
    <div class="nav d-flex justify-content-between">
        <!-- 좌측 형태 정렬 -->
        <div class="nav-container bg-pink">
          <router-link :to="{ name: 'DiaryPhoto'}" class="view right-outline pointer">
            <i class="fas fa-file-image fa"></i>
          </router-link>
          <router-link :to="{ name: 'DiaryTimeline'}" class="view right-outline pointer">
            <i class="fas fa-stream fa"></i>
          </router-link>
          <router-link :to="{ name: 'DiaryCalendar'}" class="view pointer">
            <i class="fas fa-calendar-alt fa"></i>
          </router-link>
        </div>

        <!-- 우측 검색 -->
        <div>
          <i class="fas fa-search pointer"></i>
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
  color: #ff6454;
}


</style>