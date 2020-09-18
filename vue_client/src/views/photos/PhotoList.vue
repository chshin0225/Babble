<template>
  <div class="grid" data-app>
    <div>
      <div class="photos row no-gutters">
        <div v-for="photo in photos" :key="`club_${photo.id}`" class="photo-container pointer" @click="clickPhoto">
          <div class="photo">             
            <img :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + photo.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" class="card-img-top " alt="">
          </div>
        </div>
      </div>
    </div>
    <!-- 여기부터 가짜 -->
    <!-- <div>
      <h5 class="date">2020-09-15 화</h5>
      <div class="photos d-flex">
        <div class="photo-container pointer" @click="clickPhoto">
          <div class="photo">
            <img src="https://t1.daumcdn.net/tvpot/thumb/s8b90Dh8u7sDgMlccgchys3/thumb.png?ts=1541536764" class="card-img-top " alt="...">
          </div>
        </div>
        <div class="photo-container">
          <div class="photo">
            <img src="https://pds.joins.com/news/component/htmlphoto_mmdata/201501/07/htm_20150107104932c010c011.jpg" class="card-img-top" alt="...">
          </div>
        </div>
        <div class="photo-container">
          <div class="photo">
            <img src="https://image.ajunews.com/content/image/2015/02/25/20150225134705285589.jpg" class="card-img-top" alt="...">
          </div>
        </div>
      </div>
    </div>
    <div>
      <h5 class="date">2020-09-13 일</h5>
      <div class="photos d-flex">
        <div class="photo-container">
          <div class="photo">
            <img src="https://mimg.segye.com/content/image/2015/01/30/20150130002870_0.jpg" class="card-img-top " alt="...">
          </div>
        </div>
        <div class="photo-container">
          <div class="photo">
            <img src="https://news.imaeil.com/inc/photos/2015/03/27/2015032710112575472_m.jpg" class="card-img-top" alt="...">
          </div>
        </div>
      </div>
    </div>
    <div>
      <h5 class="date">2020-09-08 화</h5>
      <div class="photos d-flex">
        <div class="photo-container">
          <div class="photo">
            <img src="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F22250C45595DFF2808" class="card-img-top " alt="...">
          </div>
        </div>
        <div class="photo-container">
          <div class="photo">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSrNPbIgSPkRCQMuXvofe6jLsUWaP6eALIiFQ&usqp=CAU" class="card-img-top" alt="...">
          </div>
        </div>
        <div class="photo-container">
          <div class="photo">
            <img src="https://image.chosun.com/sitedata/image/201503/19/2015031902832_0.jpg" class="card-img-top" alt="...">
          </div>
        </div>
      </div>
    </div>
    <div>
      <h5 class="date">2020-09-06 일</h5>
      <div class="photos d-flex">
        <div class="photo-container">
          <div class="photo">
            <img src="https://pds.joins.com/news/component/htmlphoto_mmdata/201501/08/htm_2015010810155c010c011.jpeg" class="card-img-top " alt="...">
          </div>
        </div>
      </div>
    </div> -->

    <!-- 날짜 선택 -->
    <!-- <h4>날짜 선택</h4>
    <div class="date-picking">
      <span @click.stop="dialog = true">YYYY</span>
      <v-dialog
        v-model="dialog"
        max-width="290"
      >
        <v-row align="center">
          <v-date-picker 
            v-model="picker" 
            color="green lighten-1"
            type="month"
            year-icon="mdi-calendar-blank"
            prev-icon="mdi-skip-previous"
            next-icon="mdi-skip-next"
          ></v-date-picker>
        </v-row>
      </v-dialog>
    </div> -->
    <!-- 사진 추가 버튼 구현 -->
    <div @click="clickAdd" class="add-button color-pink pointer">
      <i class="fas fa-plus-circle fa-2x"></i>
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
      // picker: new Date().toISOString().substr(0, 7),
      // dialog: false,
    }
  },
  computed: {
    ...mapState('photoStore', ['photos'])
  },
  methods: {
    ...mapActions('photoStore', ['fetchPhotos']),
    clickAdd() {
      this.$router.push({ name: 'PhotoCreate' })
    },
    clickPhoto() {
      this.$router.push({ name: 'PhotoDetail' })
    }
  },
  created() {
    this.fetchPhotos()
  }
}
</script>

<style scoped>
.grid {
  padding: 0 0 0 2.5vw;
}

img {
  /* width: 30vw; */
  height: 30vw;
  width: auto;
}

.photo-container{
  object-fit: cover;
  object-position: 50% 50%;
  width: 30vw; 
  height: 30vw;
  overflow:hidden;
  margin-right: 2.5vw;
  margin-bottom: 2.5vw;
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
</style>