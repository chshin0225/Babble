<template>
  <div class="grid" data-app>
    <div style="text-align:center">
      <div class="search-bar">
          <input 
            type="text" 
            placeholder="Search" 
            name="search" 
            @keyup.enter="searchPhotos(searchKeyword)"
            v-model="searchKeyword"
            class="input-search"
          >
          <button @click="searchPhotos(searchKeyword)"><i class="fa fa-search" style="color:#9BC7FF;"></i></button>
      </div>
    </div>
    <div v-if="searchedPhotos">
      <div class="photos row no-gutters mt-5" v-if="searchedPhotos.length">
        <div v-for="photo in searchedPhotos" :key="`club_${photo.id}`" class="photo-container2 pointer" @click="clickPhoto(photo.id)">
          <div class="photo">             
            <img :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + photo.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" class="card-img-top " alt="">
          </div>
        </div>
      </div>
      <div class="d-flex flex-column justify-content-center align-items-center mt-5" v-else>
        <h5>검색 결과가 없습니다.</h5>
        <img class="crying-baby" src="@/assets/baby.png">
      </div>
    </div>
    <div v-else>
      <div>
        <h5 class="tag-name">인물</h5>
        <div class="photos d-flex">
          <div class="photo-container">
            <div class="photo">
              <img src="https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/babble_1%2FKakaoTalk_20200924_233638829.jpg?alt=media&token=fc508930-5485-426e-8279-932db09009c0" class="card-img-top " alt="...">
            </div>
          </div>
          <div class="photo-container">
            <div class="photo">
              <img src="https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/babble_1%2FKakaoTalk_20200924_233638829_03.jpg?alt=media&token=fc508930-5485-426e-8279-932db09009c0" class="card-img-top" alt="...">
            </div>
          </div>
          <div class="photo-container">
            <div class="photo">
              <img src="https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/babble_1%2FKakaoTalk_20200924_233638829_06.jpg?alt=media&token=fc508930-5485-426e-8279-932db09009c0" class="card-img-top" alt="...">
            </div>
          </div>
        </div>
      </div>
      <div>
        <h5 class="tag-name">감정</h5>
        <div class="photos d-flex">
          <div class="emotion-container">
            <div class="photo-container">
              <div class="photo">
                <img src="https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/babble_1%2FKakaoTalk_20200924_233638829_11.jpg?alt=media&token=fc508930-5485-426e-8279-932db09009c0" class="card-img-top " alt="...">
              </div>
            </div>
            <div style="text-align:center; width:30vw; float:left; height:auto;">웃음</div>
          </div>
          <div class="emotion-container">
            <div class="photo-container">
              <div class="photo">
                <img src="https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/babble_1%2FKakaoTalk_20200924_233638829_01.jpg?alt=media&token=fc508930-5485-426e-8279-932db09009c0" class="card-img-top" alt="...">
              </div>
            </div>
          <div style="text-align:center; width:30vw; float:left; height:auto;">울음</div>
          </div>
        </div>
      </div>
      <div>
        <h5 class="tag-name">태그</h5>
        <v-chip class="ma-2" color="#FEA59C" style="font-size:16px; margin-right:10px; color: #FFFFFF;"> #놀이터 </v-chip>
        <v-chip class="ma-2" color="#FEA59C" style="font-size:16px; color: #FFFFFF;"> #할머니 집 </v-chip>
      </div>
      <div style="height:15vh"></div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState, mapMutations } from 'vuex'
export default {
  name: 'PhotoSearch',
  data() {
    return {
      // picker: new Date().toISOString().substr(0, 7),
      // dialog: false,
      searchKeyword : "",
    }
  },
  computed: {
    ...mapState('photoStore', ['searchedPhotos'])
  },
  methods: {
    ...mapActions('photoStore', ['searchPhotos']),
    ...mapMutations('photoStore', ['SET_SEARCHED_PHOTOS']),
    clickPhoto(photo_id) {
      this.$router.push({ name: 'PhotoDetail' , params : {photoId : photo_id}})
    }
  },
  beforeRouteLeave(from, to, next) {
    this.SET_SEARCHED_PHOTOS(null)
    next()
  }
}
</script>

<style scoped>
.grid {
  padding: 0 0 0 2.5vw;
}

img {
  /* width: 90%; */
  height: 30vw;
  width: auto;
}

/*.photo-container{
  object-fit: cover;
  object-position: 50% 50%;
  width: 30vw; 
  height: 30vw;
  overflow:hidden;
  margin-right: 2.5vw;
}

.photo-container .photo img{
  max-width:initial;
  margin-left:50%;
}*/
.emotion-container{
  width:30vw;
  margin-right: 2.5vw;
}

/*
.photo-container {      
  position: relative;
  width: 30vw; 
  height: 30vw;
  margin-right: 2.5vw;
  overflow: hidden;
  border-radius : 50%;
}
.photo-container .photo img { 
  position: absolute;
  top: -9999px;
  left: -9999px;
  right: -9999px;
  bottom: -9999px;
  margin: auto;
}

.photos img {
  height: 30vw;
  width: auto;
}*/
.albums-container{
  width:30vw; 
  margin-right:2.5vw; 
  margin-bottom:2.5vw;
  border-radius : 50%;
}
.photo-container {      
  position: relative;
  width: 30vw; 
  height: 30vw;
  margin-right: 2.5vw;
  overflow: hidden;
  border-radius : 50%;
}
.photo-container .photo img { 
  position: absolute;
  top: -9999px;
  left: -9999px;
  right: -9999px;
  bottom: -9999px;
  margin: auto;
}

.photos img {
  /* width: 90%; */
  min-width:30vw;
  min-height:30vw;
  height: 30vw;
  width: auto;
}

.photos .photo{
  border : 1px solid #888888;
  border-radius: 50%;
  min-width:30vw;
  min-height:30vw;
}

.tag-name {
  
  font-weight: 900;
  margin: 5vw 0 2vw 3vw;
}

.search-bar {
  border : 2px solid #9BC7FF;
  display:inline-block;
  border-radius: 10px;
  margin : 0 auto 0 auto;
  padding : 5px 10px;
}

.search-bar .input-search {
  width:60vw;
}


.crying-baby {
  height: 50vh;
  width: auto;
}

</style>