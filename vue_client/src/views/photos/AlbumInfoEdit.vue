<template>
  <div class="container" v-if="albumDataFetched">

    <!-- top toolbar -->
    <div class="d-flex justify-content-between">
      <v-btn icon color="primary" @click="clickBack">
        <v-icon>
          mdi-arrow-left
        </v-icon>
      </v-btn>
      <v-btn text color="primary" @click="clickEdit()">
        <span class="font-weight-bold text-subtitle-1">수정 완료</span>
      </v-btn>
    </div>

    <!-- input field and buttons -->
    <div class="container">
      <v-text-field
        label="앨범 제목"
        v-model="albumInfoData.album_name"
      ></v-text-field>
    </div>

    <!-- 태그 추가 -->
    <div>
      <div class="mx-2">
        <v-combobox
          v-model="albumInfoData.tags"
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
              @click:close="remove(albumInfoData.tags, data.item)"
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
import { mapActions, mapState, mapGetters } from 'vuex'

export default {
  name: 'AlbumInfoEdit',

  data() {
    return {
      tagSearchKeyword: null,
      albumTags: [],
      searchTag: null,
      albumInfoData : {
        id: null,
        album_name: null,
        tags: null
      }
    }
  },

  computed: {
    ...mapState('photoStore', ['album', 'tags']),
    ...mapGetters('photoStore', ['albumDataFetched']),

  },

  methods: {
    ...mapActions('photoStore', ['getAlbum', 'fetchTags', 'editAlbum']),
    remove (data, item) {
      const index = data.indexOf(item)
      if (index >= 0) data.splice(index, 1)
    },
    clickBack() {
      this.$router.go(-1)
    },
    clickEdit() {
      this.editAlbum(this.albumInfoData)
    }
  },
  watch: {
    album() {
      this.albumInfoData.id = this.album.id
      this.albumInfoData.album_name = this.album.album_name
      const tempTags = []
      this.album.album_tags.forEach(tag => {
        tempTags.push(tag.tag_name)
      });
      this.albumInfoData.tags = tempTags
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