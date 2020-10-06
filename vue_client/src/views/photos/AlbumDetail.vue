<template>
  <div v-if="albumDataFetched" class="container">

    <!-- top button bar -->
    <div class="d-flex justify-content-between" v-if="relationship.rank in [1, 2]">
      <v-btn icon color="primary" @click="goToLibrary">
        <v-icon>
          mdi-arrow-left
        </v-icon>
      </v-btn>
      <v-btn icon color="primary" @click="sheet = !sheet">
        <v-icon>
          mdi-dots-horizontal
        </v-icon>
      </v-btn>
      <!-- 더보기 메뉴 -->
      <v-bottom-sheet v-model="sheet">
        <v-sheet class="text-center" height="27vh">
          <div class="py-3">
            <div class="mb-3" >
              <router-link class="black--text" :to="{ name: 'AlbumEdit', params: {albumId: album.id}}">사진 편집</router-link>
            </div>
            <hr>
            <div class="black--text" @click="clickEditAlbumInfo">앨범 정보 수정</div>
            <hr>
            <div class="black--text" @click="clickDelete">앨범 삭제</div>
          </div>
        </v-sheet>
      </v-bottom-sheet>
    </div>

    <div class="container pb-0">
      <!-- album name -->
      <h2>{{ album.album_name }}</h2>
      <!-- album tags -->
      <v-chip v-for="tag in album.album_tags" :key="tag.id" class="ma-1" outlined color="secondary">#{{ tag.tag_name }}</v-chip>
    </div>
    <hr>

    <!-- photo grid -->
    <div class="mx-2">
      <div class="photos row" v-if="albumPhotos.length">
        <div v-for="photo in albumPhotos" :key="photo.id" class="photo-container pa-1 col-4">
          <div class="photo">             
            <img 
              :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + photo.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" 
              :alt="photo.id"
              @click="clickPhoto(photo.id)"
            >
          </div>
        </div>
      </div>

      <!-- 만약 업로드 된 이미지가 없을 경우 -->
      <div v-else class="text-center no-photos mt-5">
        <img class="crying-baby" src="@/assets/baby.png">
        <h5>앨범에 사진이 없습니다.</h5>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'
import Swal from 'sweetalert2'

export default {
  name: 'AlbumDetail',

  data() {
    return {
      sheet: false,
    }
  },

  computed: {
    ...mapState(['relationship']),
    ...mapState('photoStore', ['album', 'albumPhotos']),
    ...mapGetters('photoStore', ['albumDataFetched',])
  },
  
  methods: {
    ...mapActions('photoStore', ['getAlbum', 'deleteAlbum', 'fetchAlbumPhotos']),
    goToLibrary() {
      this.$router.push({ name: 'AlbumLibrary' })
    },
    clickDelete() {
      Swal.fire({
        text: "정말 앨범을 삭제하시겠습니까?",
        showCancelButton: true,
        confirmButtonText: '네',
        cancelButtonText: '아니요',
        icon: "warning",
      })
      .then(result => {
        if (result.isConfirmed) {
          this.deleteAlbum(this.$route.params.albumId)
        }
      })
    },

    clickEditAlbumInfo() {
      // var albumData = {
      //   id: this.album.id,
      //   album_name: this.album.album_name,
      //   tags: []
      // }
      // this.album.album_tags.forEach(tag => {
      //   albumData.tags.push(tag.tag_name)
      // })
      this.$router.push({ name: "AlbumInfoEdit", params: { albumId: this.album.id}})
    },

    clickPhoto(photo_id) {
      this.$router.push({ name: 'PhotoDetail' , params : {photoId : photo_id}})
    }
  },

  mounted() {
    this.getAlbum(this.$route.params.albumId)
    this.fetchAlbumPhotos(this.$route.params.albumId)
  },
}
</script>

<style scoped>
  .photos img {
    height: 30vw;
    width: auto;
  }

  .photo-container img {
    object-fit: cover;
    object-position: 50% 50%;
    width: 30vw;
    overflow: hidden;
  }

  .photo-container {
    overflow:hidden;
  }

  .crying-baby {
    height: 50vh;
    width: auto;
  }
</style>