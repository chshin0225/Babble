<template>
  <div class="container" v-if="albumPhotoIdListFetched">
    <!-- top toolbar -->
    <div class="d-flex justify-content-between">
      <v-btn icon color="primary" @click="clickBack">
        <v-icon>
          mdi-arrow-left
        </v-icon>
      </v-btn>
      <v-btn text color="primary" @click="clickAdd">
        <span class="font-weight-bold text-subtitle-1">추가</span>
      </v-btn>
    </div>

    <!-- photo grid -->
    <div class="mx-2">
      <div class="pt-2">
        <div class="d-flex justify-content-between">
          <p class="mb-2"><span v-text="albumData.body.photos.length"></span> 장 선택</p>
          <v-btn @click="clear" outlined small color="secondary"><v-icon color="secondary" small class="mr-1">mdi-close</v-icon> 선택 해제</v-btn>
        </div>
      </div>
      <div v-if="photos">
        <div class="my-3" v-for="(dates, idx) in photos" :key="idx">
          <h5 class="dates">{{dates.date | moment("YYYY년 M월 DD일")}}</h5>
          <div class="photos row no-gutters" v-if="photos.length">
            <div v-for="photo in dates.photos" :key="`photo${photo.id}`" class="photo-container pa-1 col-4" :class="activeImage(photo.id)">
              <div class="photo">
                <v-icon v-if="isSelected(photo.id)" color="primary" class="selectedIcon">mdi-check-circle</v-icon>
                <v-icon v-if="existingPhoto(photo.id)" color="gray" class="selectedIcon">mdi-check-circle</v-icon>
                <img
                  v-if="albumPhotoIdList.photos.includes(photo.id)"
                  :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + photo.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" 
                  :alt="photo.id" 
                >
                <img
                  v-else
                  :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + photo.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" 
                  :alt="photo.id" 
                  @click="onImageSelect(photo.id)"
                >
              </div>
            </div>
          </div>
        </div>
      </div> 

      <!-- 만약 업로드 된이미지가 없을 경우 -->
      <div v-else class="text-center no-photos mt-5">
        <img class="crying-baby" src="@/assets/baby.png">
        <h5>업로드 된 이미지가 없습니다.</h5>
      </div>
    </div>

    <div class="footer"></div>

  </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'

export default {
  name: 'AlbumAddPhoto',

  data() {
    return {
      albumData: {
        albumId: this.$route.params.albumId,
        body: {
          photos: []
        }
      }
    }
  },

  computed: {
    ...mapState('photoStore', ['photos', 'albumPhotoIdList']),
    ...mapGetters('photoStore', ['albumPhotoIdListFetched'])
  },

  methods: {
     ...mapActions('photoStore', ['fetchPhotos', 'fetchAlbumPhotoIds', 'addPhotoToAlbum']),

     clickBack() {
       this.$router.go(-1)
     },

     clickAdd() {
        this.addPhotoToAlbum(this.albumData)
     },

    clear() {
      this.albumData.body.photos = [];
    },

    existingPhoto(photoId) {
      return (this.albumPhotoIdList.photos.includes(photoId))
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
    this.fetchPhotos()
    this.fetchAlbumPhotoIds(this.$route.params.albumId)
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

  .footer {
    height: 10vh;
  }
</style>