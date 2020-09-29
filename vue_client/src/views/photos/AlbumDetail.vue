<template>
  <div v-if="albumDataFetched" class="container">
    <!-- top button bar -->
    <div class="d-flex justify-content-between">
      <v-btn icon color="primary" @click="clickBack">
        <v-icon>
          mdi-arrow-left
        </v-icon>
      </v-btn>
      <v-btn icon color="primary" @click="sheet = !sheet">
        <v-icon>
          mdi-dots-horizontal
        </v-icon>
      </v-btn>
      <v-bottom-sheet v-model="sheet">
        <v-sheet class="text-center" height="27vh">
          <div class="py-3">
            <div class="mb-3" >앨범 표지 변경</div>
            <hr>
            <div class="mb-3" >앨범 수정</div>
            <hr>
            <div @click="clickDelete">앨범 삭제</div>
          </div>
        </v-sheet>
      </v-bottom-sheet>
    </div>

    <div class="container">
      <!-- album name -->
      <h3>{{ album.album_name }}</h3>
      <!-- album tags -->
      <v-chip v-for="tag in album.album_tags" :key="tag.id" class="ma-2" outlined color="secondary">#{{ tag.tag_name }}</v-chip>
      <div class="d-flex justify-content-around row">
        <v-btn color="primary" outlined rounded class="col-5">
          <v-icon class="mr-2">mdi-image</v-icon> 사진 추가
        </v-btn>
        <v-btn color="primary" outlined rounded class="col-5">
          <v-icon small class="mr-2">mdi-pound</v-icon> 태그 추가
        </v-btn>
      </div>
    </div>

    {{ album }}
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
    ...mapState('photoStore', ['album',]),
    ...mapGetters('photoStore', ['albumDataFetched',])
  },
  
  methods: {
    ...mapActions('photoStore', ['getAlbum', 'deleteAlbum',]),
    clickBack() {
      this.$router.go(-1)
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
  },

  mounted() {
    this.getAlbum(this.$route.params.albumId)
  },
}
</script>

<style>

</style>