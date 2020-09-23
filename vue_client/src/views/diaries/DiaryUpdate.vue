<template>
  <div>
    <div class="nav d-flex align-items-center">
      <div class="left-align pointer" @click="clickBack">
        <i class="fas fa-chevron-left"></i>
      </div>
      <div class="center-align d-flex align-items-center">
        <img class="float-left mr-2" width="30px" src="https://user-images.githubusercontent.com/25967949/93281500-2f491680-f807-11ea-97bb-3fb3a98bbabc.png">
        <h6>일기 수정</h6>
      </div>
    </div>
    
    <!-- 제목 -->
    <v-text-field 
      class="m-3" 
      label="제목"
      v-model="diaryData.diaryUpdateData.title"
    ></v-text-field>

    <!-- 에디터 -->
    <vue-editor
      id="editor"
      class="p-3"
      v-model="diaryData.diaryUpdateData.content"
      useCustomImageHandler
      @image-added="handleImageAdded"
      :editorToolbar="customToolbar"
    ></vue-editor>

    <!-- 성장 기록 -->
    <div class="mx-3 mt-5 mb-2">
      <h6>우리 아이 성장 기록</h6>
      <v-text-field
        label=" 키"
        suffix="cm"
        v-model="babyHeight"
      ></v-text-field>
      <v-text-field
        label="몸무게"
        suffix="kg"
        v-model="babyWeight"
      ></v-text-field>
      <v-text-field
        label="머리 둘레"
        suffix="cm"
        v-model="babyHead"
      ></v-text-field>
    </div>
    <div class="p-2 d-flex justify-content-end">
      <button @click="clickUpdate()" class="btn btn-pink ">수정</button>
    </div>
    <div style="height:10vh"></div>
        
  </div>

  

</template>

<script>
// Advanced Use - Hook into Quill's API for Custom Functionality
import { VueEditor } from "vue2-editor";
import firebase from 'firebase'

import { mapState, mapGetters, mapActions } from 'vuex';
import axios from "axios";

import SERVER from '@/api/api'
// import router from '@/router'

export default {
  name: 'DiaryUpdate',
  components: {
    VueEditor
  },
  computed: {
    ...mapState([ 'myaccount']),
    ...mapGetters(['config']),
    ...mapState('diaryStore', ['diary'])
  },
  data() {
    return {
      // editorText: 'This is initialValue.',
      customToolbar: [["bold", "italic", "underline"], [{ list: "ordered" }, { list: "bullet" }], ["image", "code-block"]],
      editorSettings: {
        modules: {
          imageDrop: true,
          imageResize: {}
        }
      },
      babyHead: 0,
      babyHeight: 0,
      babyWeight: 0,
      diaryData: {
        diaryUpdateData: {
          title: '',
          content: '',
          content_html: ''
        },
        diaryId: this.$route.params.diaryId,
      },
      htmlForEditor:""
    };
  },
  methods: {
    ...mapActions('diaryStore', ['updateDiary']),
    clickBack() {
      this.$router.go(-1)
    },
    clickUpdate() {
      this.diaryData.diaryUpdateData.content_html = this.diaryData.diaryUpdateData.content;
      this.updateDiary(this.diaryData)
    },
    handleImageAdded: function(file, Editor, cursorLocation, resetUploader) {
      const createData = []
      const promises = []
      var storageRef = firebase.storage().ref()
      
      const uploadTask = storageRef.child('babble_'+ this.myaccount.id).child(file.name).put(file)
      promises.push(uploadTask)

      var imageInfo = {
        "image_url": 'babble_' + this.myaccount.id + '%2F' + file.name,
        "last_modified": file.lastModifiedDate,
        "size": file.size,
        "file_type": file.type
      }
      createData.push(imageInfo)

      Promise.all(promises).then(() => {
        axios.post(SERVER.URL + SERVER.ROUTES.photos, createData, this.config)
          .then(() => {
            let url = "https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/" + imageInfo.image_url + "?alt=media&token=fc508930-5485-426e-8279-932db09009c0"
            Editor.insertEmbed(cursorLocation, "image", url);
            resetUploader();
          })
          .catch(err => {
            console.log(err);
          });
      })
    }
  },
  mounted() {
    this.diaryData.diaryUpdateData.title = this.diary.diary.title
    this.diaryData.diaryUpdateData.content = this.diary.diary.content
    this.diaryData.diaryUpdateData.content_html = this.diary.diary.content_html
    console.log("다이어리 업데이트", this.diary)
  }
}
</script>

<style scoped lang="scss">
// btn
button:focus {
  outline: none;
}

/* nav */
.nav {
  background: white;
  -webkit-box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  height: 6vh;
  position: sticky;
  top: 0;
  z-index: 2;

  .left-align {
    float: left;
    width: 33.3333%;
    text-align: left;
  }

  .center-align {
    float: left;
    width: 33.3333%;
    text-align: center;

    h6 {
      margin: 0;
      font-weight: 900;
    }
  }
}
</style>