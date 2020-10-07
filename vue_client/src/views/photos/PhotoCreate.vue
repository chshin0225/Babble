<template>
  <div>
    <div class="my-5 py-5 text-center" v-show="loading">
      <h5>사진을 업로드 중입니다!<br>잠시만 기다려주세요 :)</h5>
      <img class="crying-baby my-5 py-5" src="@/assets/babble_logo.png">
    </div>
    <div v-show="!loading">
      <div class="nav2 d-flex justify-content-between align-items-center">
        <div class="pointer" @click="clickBack">
          <i class="fas fa-chevron-left"></i>
        </div>
        <div>
          <input @change="change4" type="file" accept="image/gif, image/jpeg, image/png" id="file" name="file" multiple hidden>
          <button v-if="is_OK" class="btn btn-outline-pink" @click="clickUpload()">업로드</button>
          <!-- <button v-else class="btn btn-outline-pink" @click="clickOK()">확인</button> -->
          <div v-else class="d-flex flex-column"> 
            <v-bottom-sheet v-model="sheet">
              <template v-slot:activator="{ on, attrs }" >
                <v-btn
                  color="#FEA59C"
                  outlined
                  v-bind="attrs"
                  v-on="on"
                  class="mt-2"
                >
                  확인
                </v-btn>
              </template>
              <v-sheet class="text-center" :height="height">
                <div class="scallop-down"></div>
                <h3>공개 범위</h3>
                <v-container>
                  <v-radio-group v-model="radios" :mandatory="false">
                    <v-radio label="전체 공개" value="all" color="#FEA59C"></v-radio>
                    <v-radio label="양육자 한정" value="maintainer" color="#FEA59C"></v-radio>
                    <v-radio v-if="groups.length" @click="changeHeight" label="세부 설정" value="guests" color="#FEA59C"></v-radio>
                  </v-radio-group>
                  <!-- 토글 부분 -->
                  <v-btn-toggle
                    v-model="toggle_exclusive"
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
                  @click="clickFinal"
                >확인</v-btn>
              </v-sheet>
            </v-bottom-sheet>
          </div>

        </div>
      </div>
      <!-- 만약 업로드 버튼 누르기 전 일 경우 -->
      <div v-if="no_image" class="text-center mt-5">
        <img class="crying-baby" src="@/assets/babble_logo.png" style="width: 100vw">
        <h5>
          우측 상단에 있는 업로드 버튼을 누른 후, <br>
          이미지를 추가해주세요!
        </h5>
      </div>
      <div v-else id="frame" class="row no-gutters">
      </div>
    </div>
    <div style="height: 10vh"></div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import Swal from 'sweetalert2'

export default {
  name: 'PhotoCreate',
   data(){
    return {
      is_OK: true,
      sheet: false,
      radios: 'all',
      toggle_exclusive: [],
      height: '45vh',
      no_image: true,
      photos: [],
      loading: false
    }
  },
  computed: {
    ...mapState('settingStore', ['groups']),
    photoScope() {
      if (this.radios === 'all') {
        return 0
      } else if (this.radios === 'maintainer') {
        return 1
      } else {
        return 2
      }
    }
  },
  methods: {
    ...mapActions('photoStore', ['createPhotos']),
    ...mapActions('settingStore', ['fetchGroups']),
    clickBack() {
      this.$router.go(-1)
    },
    clickUpload() {
      this.no_image = false
      var fileInput = document.getElementById('file')
      fileInput.click()
    },
    clickFinal() {
      this.sheet = !this.sheet
      this.createPhotos({
        "photos": this.photos,
        "photo_scope": this.photoScope,
        "groups": this.toggle_exclusive
      })
      this.loading = true
    },
    changeHeight() {
      this.height = '57vh'
    },
    change4(e) {
      var files = e.target.files
      this.photos = files
      console.log(files)
      var isNotImage = false;
      var frame = document.getElementById('frame');
      for (var file of files) {
        if(file.type == "image/gif" || file.type == "image/jpeg" || file.type == "image/png"){
          var div = document.createElement("div")
          div.classList.add("col-4");
          var i = document.createElement("img")
          i.src = URL.createObjectURL(file)
          i.style.objectFit='cover'
          i.style.objectPosition='50% 50%'
          i.style.width='30vw'
          i.style.height='30vw'
          i.style.overflow='hidden'
          i.style.marginRight='2.5vw'
          i.style.marginBottom='2.5vw'
          i.style.boxShadow='6px 6px 10px rgba(0, 0, 0, 0.5)'
          div.appendChild(i)
          frame.appendChild(div)
          this.is_OK = false
        }else{
          isNotImage = true;
        }
        if(isNotImage){
          Swal.fire({
            icon: 'error',
            text: 'jpg 또는 png 파일만 업로드할 수 있습니다.'
          })
        }
      }
    },
  },
  created() {
    this.fetchGroups()
  }
}


</script>

<style scoped lang="scss">
#app {
  min-height: 0px !important;
  height: 6vh !important;
  overflow: hidden;
}
/* nav */
.nav2 {
  background: white;
  -webkit-box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  height: 6vh;
  position: sticky;
  top: 0;
  z-index: 10000;
  padding: 0.5rem;

  button {
    border-radius:0.5rem;
    padding: 0.3rem 0.5rem; 
    margin: 0 !important;
  }
}

.imgStyle {
  object-fit: cover;
  object-position: 50% 50%;
  width: 30vw; 
  height: 30vw;
  overflow:hidden;
  margin-right: 2.5vw;
}

#app > div.v-dialog__content.v-dialog__content--active > div > div > div > div > div > div.v-input__slot {
  margin: 0;
}

.v-input, .v-input__slot, .v-input__control {
  margin: 0 !important;
  padding: 0 !important;
}

.v-item-group {
  padding:0;
}

.v-btn {
  margin-top: 5px;
}

.v-btn--active {
  background-color: #FEA59C;
  color: white !important;
}

.final-button {
  background-color: #9BC7FF;
  color: white !important;
}

.scallop-down{
  height:40px;
  /* margin-left: auto;
  margin-right: auto; */
  width:100%;
  background: -webkit-gradient(radial, 50% 0, 18, 50% 0, 31, from(#9BC7FF), color-stop(0.49, #9BC7FF), color-stop(0.51, #fff), to(white));
  -webkit-background-size: 49px 100%;
}

.crying-baby {
  height: 50vh;
  width: auto;
}

#frame {
  padding-left: 2.5vw;
}

</style>