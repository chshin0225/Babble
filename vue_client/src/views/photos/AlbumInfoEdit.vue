<template>
  <div class="container">

    <!-- top toolbar -->
    <div class="d-flex justify-content-between">
      <v-btn icon color="primary" @click="clickBack">
        <v-icon>
          mdi-arrow-left
        </v-icon>
      </v-btn>
      <v-btn text color="primary" @click="createAlbum(albumData)">
        <span class="font-weight-bold text-subtitle-1">수정 완료</span>
      </v-btn>
    </div>

    <!-- input field and buttons -->
    <div class="container">
      <v-text-field
        label="앨범 제목"
        v-model="album.album_name"
      ></v-text-field>
    </div>

    <!-- 사진 추가 -->
    <div>
      <!-- 태그 추가 -->
      <div class="mx-2">
        <v-combobox
          v-model="album.tags"
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
  name: 'AlbumInfoEdit',

  data() {
    return {
      albumData: {
        album_name: null,
        tags: null,
        photos: [],
      },
      tagSearchKeyword: null,
      albumTags: [],
      searchTag: null,
    }
  },

  computed: {
    ...mapState('photoStore', ['album', 'tags'])
  },

  methods: {
    ...mapActions('photoStore', ['getAlbum', 'fetchPhotos',]),
    clickBack() {
      this.$router.go(-1)
    },

  },

  created() {
    this.getAlbum(this.$route.params.albumId)
    this.fetchTags()
  },
  
}
</script>

<style scoped>
  .footer {
    height: 100px;
  }
</style>