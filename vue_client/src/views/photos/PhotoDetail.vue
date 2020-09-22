<template>
  <div class="">
    <v-app-bar color="#FFFFFF" flat dense>
      <v-icon 
        class="top-left-icons pointer" 
        color="#FEA59C"
        @click="clickBack"
      >mdi-arrow-left</v-icon>
      <v-spacer></v-spacer>
      <v-icon class="top-right-icons" color="#FEA59C">mdi-folder-outline</v-icon>
      <v-icon class="top-right-icons" color="#FEA59C">mdi-heart-outline</v-icon>
      <v-icon class="top-right-icons" color="#FEA59C">mdi-dots-horizontal</v-icon>
    </v-app-bar>

      <div class="p-3">
      <div class="photo-content">
        <div class="photo-container">
          <!-- <img src="https://t1.daumcdn.net/tvpot/thumb/s8b90Dh8u7sDgMlccgchys3/thumb.png?ts=1541536764"> -->
          <img :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + photo.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'">
        </div>
        <div class="mt-3 tag-container">
          <v-chip class="ma-2" outlined color="#FEA59C" style="font-size:16px; margin-right:10px; color: #FEA59C;"> #놀이터 </v-chip>
          <v-chip class="ma-2" outlined color="#FEA59C" style="font-size:16px; color: #FEA59C;"> #할머니 집 </v-chip>
        </div>

        <div class="mt-2 photo-date text-muted">
          <p>2020년 7월 8일 14:28</p>
          <!-- <p>{{photo.create_date}}</p> -->
        </div>
        <div class="mt-2 photo-location text-muted">
          <p><v-icon>mdi-map-marker</v-icon>서울특별시 강남구 역삼동</p>
        </div>
      </div>
      <div class="mt-4 comment-content">
        
        <div class="scallop-down"></div>
        <div v-for="comment in comments" :key="`comment_${comment.id}`">
          <div>
            <div class="d-flex justify-content-between">
              <p class="nickname">{{comment.user.name}}</p>
              <p>{{comment.modify_date | diffDate}}</p>
            </div>
            <div>{{comment.content}}</div>
          </div>
          <hr>
        </div>
        <!-- <div>
          <div class="d-flex justify-content-between">
            <p class="nickname">아빠</p>
            <p>3시간 전</p>
          </div>
          <div>우리 애기 이쁘당</div>
        </div>
        <hr>
        <div>
          <div class="d-flex justify-content-between">
            <p class="nickname">엄마</p>
            <p>어제</p>
          </div>
          <div>이쁜 울애기</div>
        </div>
        <hr>
        <div>
          <div class="d-flex justify-content-between">
            <p class="nickname">할머니</p>
            <p>2020.09.10</p>
          </div>
          <div>할미가 맛난 거 해줄게</div>
        </div> -->
      </div>
    </div>
    <div style="height:15vh"></div>
  </div>
</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.19.1/moment.min.js"></script>
<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'PhotoDetail',
  /*mounted() {
    console.log("mounted", this.$route.params.photoId );
  },*/
  computed: {
    ...mapState('photoStore', ['photo', 'comments'])
  },
  methods: {
    ...mapActions('photoStore', ['findPhoto', 'fetchPhotoComments']),
    clickBack() {
      this.$router.go(-1)
    }
  },
  filters: {
      diffDate(val) {
        let diff = ((new Date() - (new Date(val))) / 1000) - new Date(val).getTimezoneOffset() * 60;
        
        if(diff < 60)
          return '방금 전'
        diff /= 60;
        if(diff < 60)
          return parseInt(diff) + '분 전'
        diff /= 60;
        if(diff < 24)
          return parseInt(diff) + '시간 전'
        diff /= 24;
        if(diff < 7)
          return parseInt(diff) + '일 전'
        if (diff < 30)
          return parseInt(diff/7) + '주 전'
        if (diff < 365)
          return parseInt(diff/30) + '달 전'
        return parseInt(diff/365) + '년 전'
        return val
      }
  },
  mounted() {
    this.findPhoto(this.$route.params.photoId);
    this.fetchPhotoComments(this.$route.params.photoId);
    //alert(this.$route.params.photoId);
  }
}
</script>
<style scoped>
.top-left-icons{
  font-size:28px;
}
.top-right-icons{
  margin-left:5px;
  font-size:28px;
}
.photo-container{
    text-align:center;
}
.photo-content .photo-container img{
    width: 100%;  
}

.tag-container{
   margin-top:10px;
}
.photo-date p{
  font-size:1.2rem;
}
.photo-date p, .photo-location p{
  margin:0;
}
.comment-content .nickname{
  font-weight:bold;
}

.scallop-down{
  height:40px;
  /* margin-left: auto;
  margin-right: auto; */
  width:100%;
  background: -webkit-gradient(radial, 50% 0, 18, 50% 0, 31, from(#9BC7FF), color-stop(0.49, #9BC7FF), color-stop(0.51, #fff), to(white));
  -webkit-background-size: 49px 100%;
}

</style>