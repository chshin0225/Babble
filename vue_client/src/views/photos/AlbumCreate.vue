<template>
  <div class="container">

    <div class="d-flex justify-content-between">
      <v-btn icon color="primary" @click="clickBack">
        <v-icon>
          mdi-arrow-left
        </v-icon>
      </v-btn>
      <v-btn text color="primary" @click="createAlbum(albumData)">
        <span class="font-weight-bold text-subtitle-1">생성</span>
      </v-btn>
    </div>

    <div class="container">
      <v-text-field
        label="앨범 제목"
        v-model="albumData.album_name"
      ></v-text-field>
      <!-- button toggle -->
      <div class="d-flex justify-content-around row">
        <v-btn color="primary" outlined rounded class="col-5" retain-focus-on-click  @click="clickAddPhoto">
          <v-icon class="mr-2">mdi-image</v-icon> 사진 추가
        </v-btn>
        <v-btn color="primary" outlined rounded class="col-5" retain-focus-on-click @click="clickAddTag">
          <v-icon small class="mr-2">mdi-pound</v-icon> 태그 추가
        </v-btn>
      </div>
    </div>

    <div class="container pt-0">
      <!-- 사진 추가 -->
      <div v-if="toggle == 0">
        <v-text-field
          label="사진 검색"
          v-model="photoSearchKeyword"
          append-icon="mdi-magnify"
          color="secondary"
          @click:append="clickSearch"
        ></v-text-field>
        <div class="photos row" v-if="photos.length">
          <div v-for="photo in photos" :key="photo.id" class="photo-container col-4">
            <div class="photo">             
              <img :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + photo.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" class="card-img-top" :alt="photo.id">
            </div>
          </div>
        </div>
        <div v-else class="text-center no-photos mt-5">
          <!-- 만약 업로드 된이미지가 없을 경우 -->
          <img class="crying-baby" src="@/assets/baby.png">
          <h5>업로드 된 이미지가 없습니다.</h5>
        </div>
      </div>

      <!-- 태그 추가 -->
      <div v-else-if="toggle == 1">
        <v-combobox
          v-model="albumData.tags"
          :items="tags"
          :search-input.sync="searchTag"
          hide-selected
          counter="10"
          :rules="[
            v => (v.length < 11) || '최대 10개의 태그를 고를 수 있습니다.'
          ]"
          color="secondary"
          label="태그 검색"
          multiple
          item-text="tag_name"
          item-value="tag_name"
          :return-object="false"
          persistent-hint
          small-chips
        >
          <template v-slot:selection="data">
            <v-chip
              v-bind="data.attrs"
              close
              @click:close="remove(albumData.tags, data.item)"
            >
              {{ data.item }}
            </v-chip>
          </template>
          <template v-slot:no-data>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>
                  "<strong>{{ searchTag }}</strong>"를 찾을 수 없습니다. <kbd>enter</kbd>를 눌러 새로운 태그를 만들어보세요. 
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-combobox>


      </div>
    </div>


  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'AlbumCreate',

  data() {
    return {
      albumData: {
        album_name: null,
        tags: null
      },
      toggle: null,
      photoSearchKeyword: null,
      tagSearchKeyword: null,
      albumTags: [],
      searchTag: null,
    }
  },

  computed: {
    ...mapState('photoStore', ['photos', 'tags'])
  },

  methods: {
    ...mapActions('photoStore', ['createAlbum', 'fetchPhotos', 'fetchTags']),
    clickBack() {
      this.$router.go(-1)
    },

    clickAddPhoto() {
      this.toggle = 0
    },

    clickAddTag() {
      this.toggle = 1
    },

    clickSearch() {
      console.log(this.photoSearchKeyword)
    },

    remove(data, item) {
      const index = data.indexOf(item)
      if (index >= 0) data.splice(index, 1)
    },
  },



  created() {
    this.fetchPhotos()
    this.fetchTags()
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
</style>