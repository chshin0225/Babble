<template>
  <div class="container">

    <!-- top toolbar -->
    <div class="d-flex justify-content-between">
      <v-btn icon color="primary" @click="clickBack">
        <v-icon>
          mdi-arrow-left
        </v-icon>
      </v-btn>
      <v-btn text color="primary" @click="clickCreate">
        <span class="font-weight-bold text-subtitle-1">생성</span>
      </v-btn>
    </div>

    <!-- input field and buttons -->
    <div class="container">
      <v-text-field
        label="앨범 이름"
        v-model="albumData.album_name"
        :rules="[rules.required]"
      ></v-text-field>
      <div class="d-flex justify-content-around row mt-2">
        <v-btn color="primary" outlined rounded class="col-5" retain-focus-on-click  @click="clickAddPhoto">
          <v-icon class="mr-2">mdi-image</v-icon> 사진 추가
        </v-btn>
        <v-btn color="primary" outlined rounded class="col-5" retain-focus-on-click @click="clickAddTag">
          <v-icon small class="mr-2">mdi-pound</v-icon> 태그 추가
        </v-btn>
      </div>
    </div>

    <!-- 사진 추가 -->
    <div>
      <div class="mx-2" v-if="toggle == 0">
        <!-- <v-text-field
          label="사진 검색"
          v-model="photoSearchKeyword"
          append-icon="mdi-magnify"
          color="secondary"
          @click:append="clickSearch"
        ></v-text-field> -->
        <!-- photo selection toolbar -->
        <div class="pt-2">
          <div class="d-flex justify-content-between" v-if="albumData.photos">
            <p class="mb-2"><span v-text="albumData.photos.length"></span> 장 선택</p>
            <v-btn @click="clear" outlined small color="secondary"><v-icon color="secondary" small class="mr-1">mdi-close</v-icon> 선택 해제</v-btn>
          </div>
        </div>
        <!-- photo grid -->
        <div v-if="photos">
          <div class="my-3" v-for="(dates, idx) in photos" :key="idx">
            <h5 class="dates">{{dates.date | moment("YYYY년 M월 DD일")}}</h5>
            <div class="photos row no-gutters" v-if="photos.length">
              <div v-for="photo in dates.photos" :key="`photo${photo.id}`" class="photo-container pa-1 col-4" :class="activeImage(photo.id)">
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
          </div>
        </div> 
        <div v-else class="text-center no-photos mt-5">
          <!-- 만약 업로드 된이미지가 없을 경우 -->
          <img class="crying-baby" src="@/assets/baby.png">
          <h5>업로드 된 이미지가 없습니다.</h5>
        </div>
      </div>

      <!-- 태그 추가 -->
      <div class="mx-2" v-else-if="toggle == 1">
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

    <div class="footer"></div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'AlbumCreate',

  data() {
    return {
      albumData: {
        album_name: '',
        tags: null,
        photos: [],
      },
      rules: {
        required: value => !!value || '앨범 이름을 입력해주세요.',
      },
      toggle: null,
      photoSearchKeyword: null,
      tagSearchKeyword: null,
      albumTags: [],
      searchTag: null,
    }
  },

  computed: {
    ...mapState('photoStore', ['photos', 'tags',])
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

    isSelected(photoId) {
      return (this.albumData.photos.includes(photoId));
    },

    activeImage(photoId) {
      let classes = ['selectable-box'];
      if (this.isSelected(photoId)) { 
        classes.push('active');
      }
      return classes;
    },

    clear() {
      this.albumData.photos = [];
    },

    onImageSelect(photoId) {
      if (this.isSelected(photoId)) {
        this.albumData.photos = this.albumData.photos.filter((selectedIndex) => {
          return (selectedIndex !== photoId);
        });
      } else {
        this.albumData.photos.push(photoId);
      }
    },

    clickCreate() {
      if (this.albumData.album_name.trim() !== ''){
        this.createAlbum(this.albumData)
      } 
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

  .selectedIcon {
    position: absolute;
    font-size: 1.8rem;
  }

  .footer {
    height: 100px;
  }

  .crying-baby {
    height: 30vh;
    width: auto;
  }
</style>