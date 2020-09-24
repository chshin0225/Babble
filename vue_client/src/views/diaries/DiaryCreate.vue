<template>
  <div>
    <div class="my-5 py-5 text-center" v-show="loading">
      <h5>사진을 업로드 중입니다!<br>잠시만 기다려주세요 :)</h5>
      <img class="crying-baby my-5 py-5" src="@/assets/babble_logo.png">
    </div>
    <div data-app v-show="!loading">
      <div class="nav d-flex align-items-center">
        <div class="left-align pointer" @click="clickBack">
          <i class="fas fa-chevron-left"></i>
        </div>
        <div class="center-align d-flex align-items-center">
          <img class="float-left mr-2" width="30px" src="https://user-images.githubusercontent.com/25967949/93281500-2f491680-f807-11ea-97bb-3fb3a98bbabc.png">
          <h6>새 일기 작성</h6>
        </div>
      </div>

      <!-- 날짜 입력 -->
      <v-col cols="12" sm="6" md="4">
        <v-dialog
          ref="dialog"
          v-model="modal"
          :return-value.sync="diaryData.diary_date"
          width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="diaryData.diary_date"
              label="날짜"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker 
            color="#FEA59C" 
            :close-on-content-click="false" 
            v-model="diaryData.diary_date" 
            :max="today"
            scrollable>
            <v-col class="d-flex justify-end">
              <v-btn text color="#9BC7FF" @click="modal = false">취소</v-btn>
              <v-btn text color="#9BC7FF" @click="$refs.dialog.save(diaryData.diary_date)">선택</v-btn>
            </v-col>
            
          </v-date-picker>
        </v-dialog>
      </v-col>
      
      <!-- 제목 -->
      <v-text-field 
        class="m-3" 
        label="제목"
        v-model="diaryData.title"
      ></v-text-field>

      <!-- 에디터 -->
      <vue-editor
        id="editor"
        class="p-3"
        v-model="diaryData.content"
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
          v-model="tempRecord.babyHeight"
        ></v-text-field>
        <v-text-field
          label="몸무게"
          suffix="kg"
          v-model="tempRecord.babyWeight"
        ></v-text-field>
        <v-text-field
          label="머리 둘레"
          suffix="cm"
          v-model="tempRecord.babyHead"
        ></v-text-field>
      </div>
      <div class="p-2 d-flex justify-content-end">
        <button @click="clickCreate()" class="btn btn-pink ">작성</button>
      </div>
      <div style="height:15vh"></div>
    </div>
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
  name: 'DiaryCreate',
  components: {
    VueEditor
  },
  computed: {
    ...mapState([ 'myaccount']),
    ...mapGetters(['config'])
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
      // babyRecord: {
      // },
      tempRecord: {
        babyHead: 0,
        babyHeight: 0,
        babyWeight: 0,
      },
      diaryData: {
        diary_date: new Date().toISOString().substr(0, 10),
        title: '',
        content: '',
        content_html: '',
      },
      htmlForEditor:"",
      // Date
      menu2: false,
      modal: false,
      today: new Date().toISOString().substr(0, 10),
      // files
      files: null,
      loading: false
    };
  },
  methods: {
    ...mapActions('diaryStore', ['createDiary', 'createRecord']),
    clickBack() {
      this.$router.go(-1)
    },
    clickCreate() {
      var flag = 0

      if (this.tempRecord.babyHead !== 0 || this.tempRecord.babyWeight !== 0 || this.tempRecord.babyHeight !== 0) {
        var babyRecord = new Object()
        if (this.tempRecord.babyHead !== 0) {
          babyRecord.head_size = parseFloat(this.tempRecord.babyHead)
        } 
        if (this.tempRecord.babyWeight !== 0) {
          babyRecord.weight = parseFloat(this.tempRecord.babyWeight)
        }
        if (this.tempRecord.babyHeight !== 0) {
          babyRecord.height = parseFloat(this.tempRecord.babyHeight)
        }
        babyRecord.measure_date = this.diaryData.diary_date
        console.log(babyRecord)
        this.createRecord(babyRecord)
          .then(() => {
            flag = 1
            this.$router.push({ name: 'DiaryPhoto'})
          })
      }

      if (this.diaryData.content.length >= 1 && this.diaryData.title.length >= 1) {
        this.diaryData.content_html = this.diaryData.content;
        if (flag === 1) {
          flag = 2
        }
        else {
          flag = 3
        }

        if (flag === 1) {
          this.$router.push({ name: 'DiaryPhoto' })
        } else if (flag === 2 || flag === 3) {
          this.createDiary(this.diaryData)
        }
      }
      

      



    },
    handleImageAdded: function(file, Editor, cursorLocation, resetUploader) {
      this.loading = true
      console.log("HANDLE IMAGE ADDED")
      const createData = []
      const promises = []
      const tagPromises = []
      var storageRef = firebase.storage().ref()
      
      const uploadTask = storageRef.child('babble_'+ this.myaccount.current_baby).child(file.name).put(file)
      promises.push(uploadTask)
      Promise.all(promises).then(() => {
        var imageInfo = {
          "image_url": 'babble_' + this.myaccount.current_baby + '%2F' + file.name,
          "temp_url": 'babble_' + this.myaccount.current_baby + '/' + file.name,
          "last_modified": file.lastModifiedDate,
          "size": file.size,
          "file_type": file.type,
          "tags": []
        };
        var imagePath = {
          "path": imageInfo.temp_url
        }
        const tagExtract = axios.post(SERVER.AIURL, imagePath)
                            .then(res => {
                              imageInfo.tags = res.data.tags
                            })
                            .catch(err => console.log(err.response.data))
        tagPromises.push(tagExtract)
        Promise.all(tagPromises).then(() => {
          createData.push(imageInfo)
          axios.post(SERVER.URL + SERVER.ROUTES.photos, createData, this.config)
            .then(() => {
              let url = "https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/" + imageInfo.image_url + "?alt=media&token=fc508930-5485-426e-8279-932db09009c0"
              Editor.insertEmbed(cursorLocation, "image", url);
              resetUploader();
              this.loading = false
            })
            .catch(err => {
              console.log(err);
              this.loading = false
            });
            if ( this.files === null ) {
              let url = "https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/" + imageInfo.image_url + "?alt=media&token=fc508930-5485-426e-8279-932db09009c0"
              this.diaryData.cover_photo = url
              this.files = true
              console.log(this.diaryData)
            }
        })
      })
    }
  },
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
  z-index: 1;

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

<style scoped>
.v-picker__title__btn >>> div {
  color: black !important;
}

.v-date-picker-title >>> p {
  color: black !important;
}

.v-picker__actions >>> button {
  text-align: right !important;
}

.crying-baby {
  height: 50vh;
  width: auto;
}

</style>