
<template>
<div>
  <div>
    <p class="main-title text-center color-pink">아롱이의 9월</p>
    <!-- Date Picker -->
    <v-app>
      <v-row class="d-flex justify-content-center">
        <v-col cols="3" sm="3" class="erase-padding">
          <v-dialog
            ref="dialog"
            v-model="modal"
            :return-value.sync="date"
            persistent
            width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="date"
                readonly
                v-bind="attrs"
                v-on="on"
                class="centered-date"
              ></v-text-field>
            </template>
            <v-date-picker v-model="date" type="month" scrollable>
              <v-spacer></v-spacer>
              <v-btn text color="primary" @click="modal = false">Cancel</v-btn>
              <v-btn text color="primary" @click="$refs.dialog.save(date)">OK</v-btn>
            </v-date-picker>
          </v-dialog>
        </v-col>
      </v-row>
    </v-app>

    <!-- Swiper -->
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide v-for="n in 10" :key=n> 
        <div class="card" @click="clickCard" style="background-image:url('https://t1.daumcdn.net/tvpot/thumb/s8b90Dh8u7sDgMlccgchys3/thumb.png?ts=1541536764')">
          <div class="p-3 title col-3 text-center">
            <span class="date">{{n}}</span><br>
            <span class="month">Sept</span>
          </div>
          <div class="p-3 mt-auto">
            <h4 class="diary-text">세상에서 가장 귀여운 우리 아롱이... 오늘은 밥 많이 먹었다!</h4>
          </div>
          <!-- <img src="https://lh3.googleusercontent.com/proxy/I8VHuGeCKm3Mr0766qrIhVU1CRQCtWKWNhdI-qjWprYYF5Ov20qyr8NmuJR-k6avovYBkit3UERqwGpOLyDJtrYX5GKN3EcFZMkVurpYgz81rzR_tXULTeU72fAoP6Z_tW24KCOrxgWIbb14HITOhg" class="card-img-top " alt="..."> -->
        </div>
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
    </swiper>
  </div>
  <!-- 다이어리 추가 버튼 구현 -->
  <div @click="clickAdd" class="add-button color-pink pointer">
    <i class="fas fa-plus-circle fa-2x"></i>
  </div>
</div>


</template>

<script>

import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'

export default {
  name: 'DiaryPhoto',
  title: 'Centered slides',
  components: {
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      swiperOption: {
        slidesPerView: 1,
        spaceBetween: 30,
        centeredSlides: true,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        }
      },
      selectedDate: '',
      date: new Date().toISOString().substr(0, 7),
      menu: false,
      modal: false,
    }
  },
  methods: {
    clickAdd() {
      this.$router.push({name: 'DiaryCreate'})
    },
    clickCard( ){
      this.$router.push({name: 'DiaryDetail', params: { 'diaryId': 1 } })
    }
  }
}
</script>

<style scoped>
#app {
  min-height: 0px !important;
  height: 6vh !important;
  overflow: hidden;
}

p {
  margin: 0;
}

.main-title {
  font-size: 2rem;
  font-weight: 900;
}

.card {
  height: 60vh;
  width: 82vw;
  background-size: cover;
  background-position: 50% 50%;
  border-radius: 10%;
  box-shadow: 10px 10px  5px rgba(0,0,0,0.6);
  -moz-box-shadow: 10px 10px  5px rgba(0,0,0,0.6);
  -webkit-box-shadow: 10px 10px  5px rgba(0,0,0,0.6);
  -o-box-shadow: 10px 10px  5px rgba(0,0,0,0.6);
   margin-bottom: 2vh;
}


.title {
  font-weight: 900;
  font-size: 1.6rem;
  color: white;
}

.title .date {
  font-size: 2.5rem;
}

/* date picker */
.erase-padding {
  padding: 0;
}

.v-text-field > .v-input__control > .v-input__slot {
  margin: 0 !important;
}

.v-input {
  padding: 0 !important;
}

.centered-date >>> input {
  text-align: center !important;
}

#input-14 {
  padding: 0 !important;
  text-align: center !important;
}

.diary-text {
  color: white;
  text-shadow: 2px 2px black;
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