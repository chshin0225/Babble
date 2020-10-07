<template>
  <div>
    <div class="photo-content">
      <div class="photo-container">
        <img :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + createData.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'">
      </div>
    </div>
    <h5 class="text-center mt-5">사진의 태그를 자유롭게 수정해주세요 :)</h5>
    <v-col cols="12">
      <v-combobox
        v-if="tags"
        v-model="createData.tags"
        :items="tags"
        :search-input.sync="searchTag"
        hide-selected
        counter="10"
        :rules="[
          v => (v.length < 11) || '최대 10개의 태그를 고를 수 있습니다.'
        ]"
        color="blue-grey lighten-2"
        label="태그"
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
            @click:close="remove(createData.tags, data.item)"
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
      <v-btn
        class="mt-6 final-button"
        text
        color="#FEA59C"
        raised
        absolute
        right
        @click="clickConfirm"
      >확인</v-btn>
    </v-col>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'


export default {
  name: 'TagSelect',
  data() {
    return {
      createData: this.$route.params.createData,
      photoType: this.$route.params.photoType,
      searchTag: null
    }
  },
  computed: {
    ...mapState('photoStore', ['tags'])
  },
  methods: {
    ...mapActions('photoStore', ['completeCreatePhoto', 'fetchTags', 'updatePhoto']),
    remove (data, item) {
      const index = data.indexOf(item)
      if (index >= 0) data.splice(index, 1)
    },
    clickConfirm() {
      if (this.photoType === "update") {
        this.updatePhoto(this.createData)
      } else if (this.photoType === "create") {
        this.completeCreatePhoto(Array(this.createData))
      }
    }
  },
  created() {
    this.fetchTags()
  }
}
</script>

<style scoped>
.photo-container{
    text-align:center;
}

.photo-content .photo-container img{
    width: 100%;
    max-height: 50vh;
}

.final-button {
  background-color: #9BC7FF;
  color: white !important;
}
</style>