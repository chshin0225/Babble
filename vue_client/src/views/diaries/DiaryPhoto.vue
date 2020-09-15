
<template>
<v-app class="h-100">
  <div>
    <p class="main-title text-center color-pink">아롱이의 9월</p>
    <!-- Date Picker -->
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
              class="text-center"
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
    <!-- Swiper -->
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide v-for="n in 10" :key=n> 
        <div class="card" style="background-image:url('https://t1.daumcdn.net/tvpot/thumb/s8b90Dh8u7sDgMlccgchys3/thumb.png?ts=1541536764')">
          <div class="p-3 title col-3 text-center">
            <span class="date">7</span><br>
            <span class="month">July</span>
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
</v-app>


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
      lastday(){ //년과 월에 따라 마지막 일 구하기 
      var Year=document.getElementById('select_year').value; 
      var Month=document.getElementById('select_month').value; 
      var day=new Date(new Date(Year,Month,1)-86400000).getDate(); 
      var dayindex_len=document.getElementById('select_day').length; 
      if(day>dayindex_len){ 
        for(var i=(dayindex_len+1); i<=day; i++){ 
          document.getElementById('select_day').options[i-1] = new Option(i, i); 
        } 
      } else if(day<dayindex_len){ 
          for(var j=dayindex_len; j>=day; j--){ 
            document.getElementById('select_day').options[j]=null; 
          } 
        } 
  }
    }
  }
</script>

<style scoped>
.v-application--wrap {
  min-height: 0px !important;
}

.main-title {
  font-size: 2rem;
  font-weight: 900;
}

.card {
  height: 60vh;
  width: 86vw;
  background-size: cover;
  background-position: 50% 50%;
  border-radius: 10%;
  box-shadow: 10px 10px  5px rgba(0,0,0,0.6);
  -moz-box-shadow: 10px 10px  5px rgba(0,0,0,0.6);
  -webkit-box-shadow: 10px 10px  5px rgba(0,0,0,0.6);
  -o-box-shadow: 10px 10px  5px rgba(0,0,0,0.6);
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

#input-14 {
  padding: 0 !important;
  text-align: center !important;
}

.diary-text {
  color: white;
  text-shadow: 2px 2px black;
}
</style>