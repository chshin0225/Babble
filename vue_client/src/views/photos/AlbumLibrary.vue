<template>
  <div class="container" data-app>
    <div class="albums row">
      <div class="new-album col-6 d-flex flex-column justify-content-center align-items-center">
        <div class="album">
          <v-btn icon color="primary" :to="{ name: 'AlbumCreate' }" class="text-decoration-none">
            <v-icon x-large>mdi-plus-circle</v-icon>      
          </v-btn>
        </div>
        <p class="album-title">새 앨범</p>
      </div>
      <div v-for="album in albums" :key="album.id" class="col-6 d-flex flex-column justify-content-center align-items-center">
        <div class="album">
          <img :src="album.cover_photo" :alt="album.album_name">
        </div>
        <p class="album-title">{{ album.album_name }}</p>
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
import { mapActions, mapState } from 'vuex'

export default {
  name: 'AlbumLibrary',
  data() {
    return {
      
    }
  },

  computed: {
    ...mapState('photoStore', ['albums',])
  },

  methods: {
    ...mapActions('photoStore', ['fetchAlbums']),
  },

  created() {
    this.fetchAlbums()
  },
}
</script>

<style scoped>

/* .crying-baby {
  height: 50vh;
  width: auto;
}

.albums img {
  min-width:45vw;
  min-height:45vw;
  height: 45vw;
  width: auto;
} */

.albums .album{
  border : 1px solid #888888;
  border-radius: 10vw;
  min-width:45vw;
  min-height:45vw;
}

/*
.album {
  width: 45vw; 
  height: 45vw;
  display: table-cell; 
  text-align: center; 
  vertical-align: middle;
}

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
} */

</style>