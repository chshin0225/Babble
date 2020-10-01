<template>
  <div>
    <nav class="nav d-flex justify-content-between p-2">
      <!-- 좌측 형태 정렬 -->
      <div class="nav-container bg-pink">
        <router-link :to="{ name: 'DiaryPhoto' }" class="view right-outline pointer">
          <i class="fas fa-file-image fa-lg"></i>
        </router-link>
        <router-link :to="{ name: 'DiaryTimeline' }" class="view right-outline pointer">
          <i class="fas fa-stream fa-lg"></i>
        </router-link>
        <router-link :to="{ name: 'DiaryCalendar' }" class="view pointer">
          <i class="fas fa-calendar-alt fa-lg"></i>
        </router-link>
      </div>

      <!-- 우측 검색 -->
      <div>
        <i class="fas fa-search pointer"></i>
      </div>
    </nav>

    <!-- router-view -->
    <router-view></router-view>

    <!-- 다이어리 추가 버튼 구현 -->
    <div @click="clickAdd" class="add-button color-pink pointer">
      <i class="fas fa-plus-circle fa-2x"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: "Diary",
  methods: {
    clickAdd() {
      this.$router.push({ name: "DiaryCreate" });
    },
  },
};
</script>

<style scoped>
.nav-container {
  border-radius: 0.5rem;
}

.fas {
  padding: 0.7rem;
}

.right-outline {
  border-right: 1px solid white;
}

.view:link,
.view:active,
.view:visited {
  color: white;
  text-decoration: none;
}

.nav-container .router-link-exact-active {
  color: #aae9f0;
}

/* 추가 버튼 */
.add-button {
  position: fixed;
  bottom: 10vh;
  right: 5vw;
  text-shadow: 5px 5px 20px rgba(0, 0, 0, 0.6);
  z-index: 1000;
}
</style>