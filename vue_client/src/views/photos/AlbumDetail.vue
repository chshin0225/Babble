<template>
  <div v-if="albumDataFetched">

    <!-- top button bar -->
    <div class="d-flex justify-content-between bg-pink nav" v-if="relationship.rank in [1, 2]">
      <v-btn icon color="white" @click="goToLibrary">
        <v-icon>
          mdi-arrow-left
        </v-icon>
      </v-btn>
      <!-- 더보기 메뉴 -->
      <v-bottom-sheet v-model="sheet">
        <template v-slot:activator="{ on, attrs }">
          <v-icon
            class="top-right-icons"
            color="white"
            v-bind="attrs"
            v-on="on" 
            >mdi-dots-vertical</v-icon>
        </template>
        <v-list>
          <v-list-item @click="clickEditAlbum">
            <v-list-item-avatar>
              <v-avatar size="32px" tile>
              <v-icon color="#FEA59C">mdi-image-area</v-icon>
              </v-avatar>
            </v-list-item-avatar>
            <v-list-item-title>사진 편집</v-list-item-title>
          </v-list-item>
          <v-list-item @click="clickEditAlbumInfo">
            <v-list-item-avatar>
              <v-avatar size="32px" tile>
              <v-icon color="#FEA59C">mdi-share-outline</v-icon>
              </v-avatar>
            </v-list-item-avatar>
            <v-list-item-title>앨범 정보 수정</v-list-item-title>
          </v-list-item>
          <v-list-item @click="clickDelete">
            <v-list-item-avatar>
              <v-avatar size="32px" tile>
              <v-icon color="#FEA59C">mdi-square-edit-outline</v-icon>
              </v-avatar>
            </v-list-item-avatar>
            <v-list-item-title>앨범 삭제</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-bottom-sheet>
    </div>

    <div class="container text-center pb-0">
      <!-- album name -->
      <div class="">
        <h4>{{ album.album_name }}</h4>
      </div>
      <!-- album tags -->
      <v-chip v-for="tag in album.album_tags" :key="tag.id" class="ma-1" outlined color="secondary">#{{ tag.tag_name }}</v-chip>
    </div>
    <hr>

    <!-- photo grid -->
    <div class="grid">
      <div class="photos row no-gutters" v-if="albumPhotos.length">
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
    },

    clickEditAlbum() {
      this.$router.push({ name: 'AlbumEdit', params: {albumId: this.album.id}})
    }
  },

  mounted() {
    this.getAlbum(this.$route.params.albumId)
    this.fetchAlbumPhotos(this.$route.params.albumId)
  },
}
</script>

<style scoped>
  .nav {
    height: 6vh;
  }

  .grid {
    margin-left: 2.5vw;
  }

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
    box-shadow:5px 6px 10px rgba(0, 0, 0, 0.1);
  }

  .crying-baby {
    height: 50vh;
    width: auto;
  }
</style>