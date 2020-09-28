<template>
  <div class="container">

    <div class="d-flex justify-content-between">
      <v-btn icon color="primary" @click="clickBack">
        <v-icon>
          mdi-arrow-left
        </v-icon>
      </v-btn>
      <v-btn text color="primary" @click="createAlbum(albumData)">
        <span class="font-weight-bold text-subtitle-1">완성</span>
      </v-btn>
    </div>

    <div class="container">
      <v-text-field
        label="앨범 제목"
        v-model="albumData.album_name"
      ></v-text-field>
      <div class="d-flex justify-content-around row">
        <v-btn color="primary" outlined rounded class="col-5">
          <v-icon class="mr-2">mdi-image</v-icon> 사진 추가
        </v-btn>
        <v-btn color="primary" outlined rounded class="col-5">
          <v-icon small class="mr-2">mdi-pound</v-icon> 태그 추가
        </v-btn>
      </div>
    </div>


  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'AlbumCreate',

  data() {
    return {
      albumData: {
        album_name: null,
        tags: null
      }
    }
  },

  methods: {
    ...mapActions('photoStore', ['createAlbum']),
    clickBack() {
      this.$router.go(-1)
    },
  },
}
</script>

<style>

</style>