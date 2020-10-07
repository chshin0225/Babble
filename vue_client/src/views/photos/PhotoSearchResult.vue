<template>
  <div class="container">
    <!-- top button bar -->
    <div class="d-flex justify-content-between">
      <v-btn icon color="primary" @click="goBack">
        <v-icon>
          mdi-arrow-left
        </v-icon>
      </v-btn>
    </div>

    <div class="container pb-0 px-1">
      <!-- album name -->
      <h5>검색 결과: {{ keyword }}</h5>
    </div>
    <hr>

    <!-- photo grid -->
    <div class="mx-2">
      <div class="photos row" v-if="searchedPhotos.length">
        <div v-for="photo in searchedPhotos" :key="photo.id" class="photo-container pa-1 col-4">
          <div class="photo">             
            <img 
              :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + photo.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" 
              :alt="photo.id"
              @click="clickPhoto(photo.id)"
            >
          </div>
        </div>
      </div>

      <!-- 만약 업로드 된 이미지가 없을 경우 -->
      <div v-else class="text-center no-photos mt-5">
        <img class="crying-baby" src="@/assets/baby.png">
        <h5>검색결과가 없습니다.</h5>
      </div>
    </div>




  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'PhotoSearchResult',
  
  data() {
    return {
      keyword: this.$route.params.keyword,
    }
  },

  computed: {
    ...mapState('photoStore', ['searchedPhotos'])
  },

  methods: {
    ...mapActions('photoStore', ['searchPhotos',]),
    goBack() {
      this.$router.push({ name: 'PhotoSearch' })
    },

    clickPhoto(photo_id) {
      this.$router.push({ name: 'PhotoDetail' , params : {photoId : photo_id}})
    }
  },

  mounted() {
    this.searchPhotos(this.$route.params.keyword)
  },
}
</script>

<style scoped>
  .photos img {
    height: 30vw;
    width: auto;
  }

  .photo-container img {
    object-fit: cover;
    object-position: 50% 50%;
    width: 30vw;
    overflow: hidden;
  }

  .photo-container {
    overflow:hidden;
  }

  .crying-baby {
    height: 50vh;
    width: auto;
  }
</style>