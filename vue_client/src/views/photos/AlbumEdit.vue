<template>
  <div v-if="albumDataFetched" class="container">

    <!-- top button bar -->
    <div class="d-flex justify-content-between">
      <!-- 사진 추가 버튼 -->
      <v-btn icon color="primary" :to="{ name: 'AlbumAddPhoto', params: { albumId: album.id } }">
        <v-icon>
          mdi-plus
        </v-icon>
      </v-btn>
      <v-btn text color="primary" @click="clickDone" class="px-2">
        <span class="font-weight-bold text-subtitle-1">편집 완료</span>
      </v-btn>
    </div>

    <div class="container pb-0">
      <!-- album name -->
      <h2>{{ album.album_name }}</h2>
      <!-- album tags -->
      <v-chip v-for="tag in album.album_tags" :key="tag.id" class="ma-1" outlined color="secondary">#{{ tag.tag_name }}</v-chip>
    </div>
    <hr>

    <div class="mx-2">
      <!-- photo selection toolbar -->
      <div class="mb-1">
        <div class="d-flex justify-content-between">
          <p class="mb-2"><span v-text="albumData.body.photos.length"></span> 장 선택</p>
          <div>
            <v-btn @click="clear" outlined small color="secondary" class="mr-2"><v-icon color="secondary" small class="mr-1">mdi-close</v-icon> 선택 해제</v-btn>
            <v-btn @click="deletePhotos" outlined small color="primary"><v-icon color="primary" small class="mr-1">mdi-trash-can-outline</v-icon> 삭제</v-btn>
          </div>
        </div>
      </div>

      <!-- photo grid -->
      <div class="photos row" v-if="albumPhotos.length">
        <div :class="activeImage(photo.id)" v-for="photo in albumPhotos" :key="photo.id" class="photo-container pa-1 col-4">
          <div class="photo">
            <v-icon v-if="isSelected(photo.id)" color="primary" class="selectedIcon">mdi-check-circle</v-icon>
            <img 
            :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + photo.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" 
            :alt="photo.id" 
            @click="onImageSelect(photo.id)"
          >
          </div>
        </div>
      </div>

      <!-- 만약 업로드 된이미지가 없을 경우 -->
      <div v-else class="text-center no-photos mt-5">
        <img class="crying-baby" src="@/assets/baby.png">
        <h5>업로드 된 이미지가 없습니다.</h5>
      </div>
    </div>

  </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'
import Swal from 'sweetalert2'

export default {
  name: 'AlbumEdit',

  data() {
    return {
      sheet: false,
      albumData: {
        albumId: this.$route.params.albumId,
        body: {
          photos: [],
        }
      }
    }
  },

  computed: {
    ...mapState('photoStore', ['album', 'albumPhotos']),
    ...mapGetters('photoStore', ['albumDataFetched',])
  },
  
  methods: {
    ...mapActions('photoStore', ['getAlbum', 'deletePhotoFromAlbum', 'fetchAlbumPhotos']),
    clickDone() {
      this.$router.push({ name: 'AlbumDetail', params: {photoId: this.album.id}})
    },

    deletePhotos() {
      Swal.fire({
        text: "선택한 사진(들)을 앨범에서 삭제하시겠습니까?",
        showCancelButton: true,
        confirmButtonText: '네',
        cancelButtonText: '아니요',
        icon: "warning",
      })
      .then(result => {
        if (result.isConfirmed) {
          this.deletePhotoFromAlbum(this.albumData)
        }
      })
    },

    clear() {
      this.albumData.body.photos = [];
    },

    isSelected(photoId) {
      return (this.albumData.body.photos.includes(photoId));
    },

    activeImage(photoId) {
      let classes = ['selectable-box'];
      if (this.isSelected(photoId)) { 
        classes.push('active');
      }
      return classes;
    },

    onImageSelect(photoId) {
      if (this.isSelected(photoId)) {
        this.albumData.body.photos = this.albumData.body.photos.filter((selectedIndex) => {
          return (selectedIndex !== photoId);
        });
      } else {
        this.albumData.body.photos.push(photoId);
      }
    },


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

  .selectedIcon {
    position: absolute;
    font-size: 1.8rem;
  }

  .crying-baby {
    height: 50vh;
    width: auto;
  }
</style>