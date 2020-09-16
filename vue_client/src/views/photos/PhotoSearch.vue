<template>
  <div class="grid" data-app>
    <div>
      <h5 class="tag-name">인물</h5>
      <div class="photos d-flex">
        <div class="photo-container">
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
      <h5 class="tag-name">감정</h5>
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
      <h5 class="tag-name">태그</h5>
      <v-chip class="ma-2" color="#FEA59C" style="font-size:16px; margin-right:10px; color: #FFFFFF;"> #놀이터 </v-chip>
      <v-chip class="ma-2" color="#FEA59C" style="font-size:16px; color: #FFFFFF;"> #할머니 집 </v-chip>
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'PhotoSearch',
  data() {
    return {
      // picker: new Date().toISOString().substr(0, 7),
      // dialog: false,
    }
  },
  methods: {
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
.photo-container {      
  position: relative;
  /*width: 300px;
  height: 300px;*/
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

.tag-name {
  
  font-weight: 900;
  margin: 10vw 0 2vw 3vw;
}
</style>