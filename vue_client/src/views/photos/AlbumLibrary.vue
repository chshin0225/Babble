<template>
  <div class="container" data-app>

    <div class="albums row">
      <div class="new-album col-6 d-flex flex-column justify-content-center align-items-center" v-if="relationship.rank === 1 || relationship.rank === 2">
        <div class="album add-album d-flex justify-content-center align-items-center">
          <v-btn icon color="primary" :to="{ name: 'AlbumCreate' }" class="text-decoration-none">
            <v-icon x-large>mdi-plus-circle</v-icon>      
          </v-btn>
        </div>
        <p class="album-title">새 앨범</p>
      </div>
      <!-- 내 앨범들 -->
      <router-link v-for="album in albums" :key="album.id" :to="{ name: 'AlbumDetail', params: {albumId: album.id}}" class="col-6 d-flex flex-column justify-content-center align-items-center text-dark">
        <div class="album add-album">
          <v-img class="cover-photo" v-if="album.cover_photo" :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + album.cover_photo + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" :alt="album.album_name"></v-img>
          <v-img class="no-photo" v-else src="@/assets/baby_face.png"></v-img>
        </div>
        <p class="album-title" mt-2>{{ album.album_name }}</p>
      </router-link>
    </div>

    <div class="footer"></div>

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
    ...mapState(['relationship']),
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

  .albums .add-album {
    border : 1px solid #e9c6c2;
    border-radius: 10vw;
    width:45vw;
    height:45vw;
  }

  .no-photo {
    border : 1px solid #e9c6c2;
    border-radius: 10vw;
    width:45vw;
    height:45vw;
    object-fit: cover;
    object-position: 50% 50%;
  }

  .albums .album {
    border-radius: 10vw;
    min-width:45vw;
    min-height:45vw;
  }

  .cover-photo {
    border-radius: 10vw;
    width:45vw;
    height:45vw;
    object-fit: cover;
    object-position: 50% 50%;
  }

  .footer {
    height: 100px;
  }
</style>