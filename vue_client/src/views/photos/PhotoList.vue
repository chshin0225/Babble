<template>
  <div class="grid" data-app>
    <div v-if="photos">
      <div v-if="photos.length">
        <div class="my-3" v-for="(dates, idx) in photos" :key="idx">
          <h5 class="dates">{{dates.date | moment("YYYY년 M월 DD일")}}</h5>
          <div class="photos row no-gutters" v-if="photos.length">
            <div v-for="photo in dates.photos" :key="`photo${photo.id}`" class="photo-container pointer" @click="clickPhoto(photo.id)">
              <div class="photo">             
                <img
                 :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + photo.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" 
                 class="card-img-top" 
                 :alt="photo.id">
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 만약 업로드 된이미지가 없을 경우 -->
      <div v-else class="text-center no-photos mt-5">
        <img class="crying-baby" src="@/assets/baby.png">
        <h5>업로드 된 이미지가 없습니다.<br>아기 사진을 올려주세요!</h5>
      </div>
    </div>


    <!-- 사진 추가 버튼 구현 -->
    <div v-if="relationship">
      <div @click="clickAdd" class="add-button color-pink pointer" v-if="[1, 2].includes(relationship.rank)">
        <i class="fas fa-plus-circle fa-2x"></i>
      </div>
    </div>

    <div style="height:15vh"></div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'PhotoList',
  data() {
    return {
      dates: [],
    }
  },
  computed: {
    ...mapState(['relationship']),
    ...mapState('photoStore', ['photos'])
  },
  methods: {
    ...mapActions('photoStore', ['fetchPhotos', 'findPhoto']),
    clickAdd() {
      this.$router.push({ name: 'PhotoCreate' })
    },
    clickPhoto(photo_id) {
      this.$router.push({ name: 'PhotoDetail' , params : {photoId : photo_id}})
    }
  },
  mounted() {
    this.fetchPhotos()
  },
  beforeRouteUpdate (to, from, next) {
    next()
  },


}
</script>

<style scoped>
.grid {
  padding: 0 0 0 2.5vw;
}

.dates {
  font-weight: 900;
}

.photos img {
  height: 30vw;
  width: auto;
}

.photo-container{
  overflow:hidden;
  margin-right: 2.5vw;
  margin-bottom: 2.5vw;
  box-shadow:5px 6px 10px rgba(0, 0, 0, 0.1);
}

.photo-container img {
  object-fit: cover;
  object-position: 50% 50%;
  width: 30vw;
  overflow: hidden;
}

.date {
  font-weight: 900;
  margin: 5vw 0 0 3vw;
}

/* 추가 버튼 */
.add-button {
  position: fixed;
  bottom: 10vh;
  right: 5vw;
  text-shadow: 5px 5px 20px rgba(0,0,0,0.6);
  z-index: 1000;
}

.crying-baby {
  margin-top: 10vh;
  height: 30vh;
  width: auto;
}

</style>


