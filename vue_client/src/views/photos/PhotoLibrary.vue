<template>
  <div class="grid" data-app>
    
    <div class="albums row no-gutters">
      <div class="albums-container pointer" 
          @click="clickNewAlbum()">
        <div class="album-container">
          <div class="album" style="width:45vw; height:45vw;display:table-cell; text-align:center; vertical-align:middle;">
            <v-icon class="" style="margin:auto; font-size:15vw;" color="#FEA59C">mdi-plus-circle</v-icon>      
          </div>
        </div>
        <div class="album-title">새 앨범</div>
      </div>
      <div v-for="album in albums" 
          :key="`club_${album.id}`" 
          class="albums-container pointer" 
          @click="clickAlbum(album.id)">
        <div class="album-container">
          <div class="album">             
            <img :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + album.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" class="card-img-top " alt="">
          </div>
        </div>
        <div class="album-title">{{album.title}}</div>
      </div>
    </div>

    <!-- <div class="text-center mt-5">
      <img class="crying-baby" src="@/assets/baby.png">
      <h5>
        페이지를 개발중입니다.<br>
        빠른 시일 내에 찾아뵙도록 하겠습니다.
      </h5>
    </div>-->

  </div>
</template>

<script>
export default {
  name: 'PhotoLibrary',
  data() {
    return {
      albums : [
        //{id : 0, image_url:"", title:"새 앨범"},
        {id : 1, image_url:"babble_1%2FKakaoTalk_20200924_233638829_11.jpg", title:"웃음"},
        {id : 2, image_url:"babble_1%2FKakaoTalk_20200924_233638829_01.jpg", title:"눈물"},
        {id : 3, image_url:"babble_1%2FKakaoTalk_20200924_233638829_04.jpg", title:"음식"},
        {id : 4, image_url:"babble_1%2FKakaoTalk_20200924_233638829_03.jpg", title:"야외"},
      ]
    }
  }
}
</script>

<style scoped>

.grid {
  padding: 0 0 0 3.3vw;
}

.crying-baby {
  height: 50vh;
  width: auto;
}

.albums img {
  /* width: 90%; */
  min-width:45vw;
  min-height:45vw;
  height: 45vw;
  width: auto;
}

.albums .album{
  border : 1px solid #888888;
  border-radius: 10vw;
  min-width:45vw;
  min-height:45vw;
}

/*.albums img {
  min-width:45vw;
  min-height:45vw;
  height: 45vw;
  width: auto;
}

.album-container{
  object-fit: cover;
  object-position: 50% 50%;
  width: 45vw; 
  height: 45vw;
  overflow:hidden;
  margin-right: 3.3vw;
  margin-bottom: 3.3vw;
  border-radius: 10vw;
}*/

.albums-container{
  width:45vw; 
  margin-right:3.3vw; 
  margin-bottom:3.3vw;
}
.album-container {      
  position: relative;
  width: 45vw; 
  height: 45vw;
  margin-right: 3.3vw;
  overflow: hidden;
  border-radius : 10vw;
}
.album-container .album img { 
  position: absolute;
  top: -9999px;
  left: -9999px;
  right: -9999px;
  bottom: -9999px;
  margin: auto;
}

.album-title{
  font-size: 4vw;
  text-align:center; 
  width:45vw; 
  z-index:9999; 
  float:left; 
  height:auto;
}

</style>