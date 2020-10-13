<template>
  <div class="grid" data-app>
    <!-- search bar -->
    <div class="text-center mt-3">
      <div class="search-bar">
          <input 
            type="text" 
            placeholder="태그 검색" 
            @keypress.enter="clickSearch"
            v-model="searchKeyword"
            class="input-search"
          >
          <button class="btn" @click="clickSearch"><i class="fa fa-search secondary--text"></i></button>
      </div>
    </div>

    <!-- suggestions -->
    <div v-if="relationship.rank !== 3">
      <div>
        <h5 class="tag-name">감정</h5>
        <div class="d-flex emotion-photo-scroll">
          <div v-for="emotion in emotionTagPhotos" :key="emotion.id" class="d-flex flex-column align-items-center mx-2" @click="clickEmotionPhoto(emotion.emotion)">
            <div class="emotion-photo-container">         
              <v-img 
                :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + emotion.photos[0].image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" 
                class="photo" 
                :alt="emotion.photos[0].image_url"
              ></v-img>
            </div>
            <p class="mt-2">{{ emotion.emotion }}</p>
          </div>
        </div>
      </div>

      <!-- tags -->
      <div>
        <h5 class="tag-name">자주 사용되는 태그</h5>
        <div class="mx-3">
          <v-chip 
            v-for="tag in babbleboxTags" 
            :key="tag.id" 
            :to="{name: 'PhotoSearchResult', params: {'keyword': tag.tag_name}}"
            class="ma-1" 
            color="secondary" 
            outlined> 
              # {{ tag.tag_name }} 
          </v-chip>
        </div>
      </div>
    </div>

    <div class="footer"></div>
  </div>
</template>

<script>
import { mapActions, mapState, mapMutations } from 'vuex'
export default {
  name: 'PhotoSearch',
  data() {
    return {
      searchKeyword : "",
    }
  },
  computed: {
    ...mapState('photoStore', ['searchedPhotos', 'tags', 'emotionTagPhotos', 'babbleboxTags']),
    ...mapState(['relationship'])
  },
  methods: {
    ...mapActions('photoStore', ['searchPhotos', 'fetchTags', 'fetchEmotionTagPhotos', 'fetchBabbleboxTags']),
    ...mapActions(['findRelationship']),
    ...mapMutations('photoStore', ['SET_SEARCHED_PHOTOS']),
    clickPhoto(photo_id) {
      this.$router.push({ name: 'PhotoDetail' , params : {photoId : photo_id}})
    },
    clickSearch() {
      if (this.searchKeyword.trim() !== '') {
        this.$router.push({ name: 'PhotoSearchResult', params: {'keyword': this.searchKeyword}})
      }
    },
    clickEmotionPhoto(emotion) {
      this.$router.push({ name: 'PhotoSearchResult', params: {'keyword': emotion}})
    },
  },

  beforeRouteLeave(from, to, next) {
    this.SET_SEARCHED_PHOTOS(null)
    next()
  },

  mounted() {
    this.fetchTags()
    this.fetchEmotionTagPhotos()
    this.fetchBabbleboxTags()
  },
}
</script>

<style scoped>
  .grid {
    padding: 0 0 0 2.5vw;
  }

  .search-bar {
    border : 2px solid #9BC7FF;
    display:inline-block;
    border-radius: 10px;
    margin : 0 auto 0 auto;
    padding : 5px 10px;
  }

  .search-bar .input-search {
    width:60vw;
    outline: none;
  }

  .search-results img {
    height: 30vw;
    width: auto;
  }

  .search-results .photo-container img {
    object-fit: cover;
    object-position: 50% 50%;
    width: 30vw; 
    overflow: hidden;
    margin-right: 2.5vw;
    margin-top: 2.5vw;
  }

  .emotion-photo-scroll {
    overflow-x: scroll;
    overflow-y: hidden;
    white-space: nowrap;
  }

  .emotion-photo-scroll::-webkit-scrollbar {
    height: 3px;
  }

  .emotion-photo-scroll::-webkit-scrollbar-thumb {
    background: #FFFFFF;
  }

  .emotion-photo-scroll:hover::-webkit-scrollbar-thumb {
    background: #FFFFFF;
  }

  .emotion-photo-container .photo {
    object-fit: cover;
    object-position: 50% 50%;
    border-radius : 50%;
    width: 30vw;
    height: 30vw;
  }

  .albums-container {
    width:30vw; 
    margin-right:2.5vw; 
    margin-bottom:2.5vw;
    border-radius : 50%;
  }

  img { 
    position: absolute;
    top: -9999px;
    left: -9999px;
    right: -9999px;
    bottom: -9999px;
    margin: auto;
  }

  .tag-name {
    font-weight: 900;
    margin: 5vw 0 2vw 3vw;
  }

  .crying-baby {
    height: 50vh;
    width: auto;
  }

  .footer {
    height: 15vh;
  }

</style>