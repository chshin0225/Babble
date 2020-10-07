<template>
  <div>
    <nav class="d-flex justify-content-between w-100 bg-pink">
      <v-icon 
        class="top-left-icons pointer" 
        color="white"
        @click="clickBack"
      >mdi-arrow-left</v-icon>
      <v-spacer></v-spacer>
      <div class="d-flex align-items-center">        
        <v-bottom-sheet v-model="photo_sheet">
          <template v-slot:activator="{ on, attrs }">
            <v-icon
              class="top-right-icons"
              color="white"
              v-bind="attrs"
              v-on="on" 
              >mdi-dots-vertical</v-icon>
          </template>
          <v-list>
            <v-list-item @click="photoDelete()">
              <v-list-item-avatar>
                <v-avatar size="32px" tile>
                <v-icon color="#FEA59C">mdi-trash-can-outline</v-icon>
                </v-avatar>
              </v-list-item-avatar>
              <v-list-item-title>사진 삭제하기</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-bottom-sheet>
      </div>
    </nav>

    <div class="p-3" v-if="photo">
      <div class="photo-content">
        <div class="photo-container">
          <img :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + photo.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'">
        </div>
        <div class="mt-2 photo-date text-muted">
          <p>{{photo.last_modified | convertDate}}</p>
        </div>
      </div>
      <div class="mt-4 comment-content">
        <div class="scallop-down"></div>        
      </div>
    </div>

    <!-- tag update -->
    <div>
      <v-col cols="12">
      <v-combobox
        v-if="tags"
        v-model="photoUpdateData.tags"
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
        cache-items
      >
        <template v-slot:selection="data">
          <v-chip
            v-bind="data.attrs"
            close
            @click:close="remove(photoUpdateData.tags, data.item)"
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
    </v-col>
    </div>
    
    <!-- scope update -->
    <div>
        <v-sheet class="text-center">
          <h5 class="mb-0">공개 범위</h5>
          <v-container class="py-0">
            <v-radio-group v-model="radios" :mandatory="false">
              <v-radio label="전체 공개" value="all" color="#FEA59C"></v-radio>
              <v-radio label="양육자 한정" value="maintainer" color="#FEA59C"></v-radio>
              <v-radio label="세부 설정" value="guests" color="#FEA59C"></v-radio>
            </v-radio-group>
            <!-- 토글 부분 -->
            <v-btn-toggle
              v-model="photoUpdateData.groups"
              multiple
              class="py-2"
              v-if="radios=='guests'"
            >
              <v-btn v-for="group in groups" :key="group.id" :value="group.id" outlined color="#FEA59C">
                {{ group.group_name }}
              </v-btn>
            </v-btn-toggle>
          </v-container>
          <!-- </div> -->
          <v-btn
            class="mt-6 final-button"
            text
            color="#FEA59C"
            raised
            @click="clickUpdate"
          >확인</v-btn>
        </v-sheet>
      <!-- </v-bottom-sheet> -->
    </div>
    
    <div style="height:15vh"></div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
export default {
  name: "PhotoUpdate",
  data() {
    return {
      photo_sheet: false,
      searchTag: null,
      photoUpdateData: {
        "id": null,
        "tags": [],
        "photo_scope": null,
        "groups": []
      },
      sheet: false,
      radios: '',
    }
  },
  computed: {
    ...mapState('photoStore', ['photo', 'tags']),
    ...mapState('settingStore', ['groups'])
  },
  methods: {
    ...mapActions('photoStore', ['findPhoto', 'deletePhoto', 'fetchTags', 'updatePhoto']),
    ...mapActions('settingStore', ['fetchGroups']),
    clickBack() {
      this.$router.go(-1)
    },
    photoDelete(){
      this.photo_sheet = false;
      if(confirm("사진을 삭제하시겠습니까?")){
        this.deletePhoto(this.$route.params.photoId);
      }
    },
    remove (data, item) {
      const index = data.indexOf(item)
      if (index >= 0) data.splice(index, 1)
    },
    clickUpdate() {
      if (this.radios === 'all') {
        this.photoUpdateData.photo_scope = 0;
      } else if (this.radios === 'maintainer') {
        this.photoUpdateData.photo_scope = 1;
      } else {
        this.photoUpdateData.photo_scope = 2;
      }
      this.updatePhoto(this.photoUpdateData);
    }
  },
  created() {
    this.fetchTags();
    this.fetchGroups();
  },
  mounted() {   
    this.photoUpdateData.id = this.photo.id
    
    this.photo.photo_tags.forEach(tag => {
      this.photoUpdateData.tags.push(tag.tag_name)
    });

    if (this.photo.photo_scope === 0) {
      this.radios = 'all'
    } else if (this.photo.photo_scope === 1) {
      this.radios = 'maintainer'
    } else {
      this.radios = 'guests'
    }

    if (this.photo.permitted_groups) {
      this.photo.permitted_groups.forEach(group => {
        this.photoUpdateData.groups.push(group.id)
      });
    }
  },
  filters: {
    convertDate(val){
      //let date = new Date((new Date(val)/1000 + new Date(val).getTimezoneOffset() * 60)*1000);
      let date = new Date(val);
      let year = date.getFullYear();
      let month = date.getMonth()+1;
      let day = date.getDate();
      day = day < 10 ? '0'+day : day;
      let hour = date.getHours();
      hour = hour < 10 ? '0'+hour : hour;
      let min = date.getMinutes();
      min = min < 10 ? '0'+min : min;
      let strDate = year+"년 "+month+"월 "+day+"일 "+hour+":"+min;
      return strDate
    },
    diffDate(val) {
      //let diff = ((new Date() - (new Date(val))) / 1000) - new Date(val).getTimezoneOffset() * 60;
      let diff = (new Date() - (new Date(val))) / 1000;
      
      if(diff < 60)
        return '방금 전'
      diff /= 60;
      if(diff < 60)
        return parseInt(diff) + '분 전'
      diff /= 60;
      if(diff < 24)
        return parseInt(diff) + '시간 전'
      diff /= 24;
      if(diff < 7)
        return parseInt(diff) + '일 전'
      if (diff < 30)
        return parseInt(diff/7) + '주 전'
      if (diff < 365)
        return parseInt(diff/30) + '달 전'
      return parseInt(diff/365) + '년 전'
    }
  },
}
</script>

<style scoped>
  nav {
    background: white;
    position: sticky;  
    height: 7vh;
  }

  .top-left-icons{
    font-size:28px;
  }

  .top-right-icons{
    margin-left:5px;
    font-size:28px;
  }

  .photo-content .photo-container img{
    width: 100%;  
  }

  .photo-container{
    text-align:center;
  }

  .tag-container{
   margin-top:10px;
  }

  .photo-date p{
    font-size:1.2rem;
  }

  .photo-date p, .photo-location p{
    margin:0;
  }

  .comment-content .nickname{
    font-weight:bold;
  }

  .scallop-down{
    height:40px;
    width:100%;
    background: -webkit-gradient(radial, 50% 0, 18, 50% 0, 31, from(#9BC7FF), color-stop(0.49, #9BC7FF), color-stop(0.51, #fff), to(white));
    -webkit-background-size: 49px 100%;
  }

  .v-btn--active {
    background-color: #FEA59C;
    color: white !important;
  }

  .final-button {
    background-color: #9BC7FF;
    color: white !important;
  }
</style>