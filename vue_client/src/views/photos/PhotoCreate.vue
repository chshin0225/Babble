<template>
  <div>
    <div class="nav2 d-flex justify-content-between align-items-center">
      <div class="pointer" @click="clickBack">
        <i class="fas fa-chevron-left"></i>
      </div>
      <div class="d-flex align-items-center">
        <input @change="change4" type="file" id="file" name="file" multiple hidden>
        <button v-if="is_OK" class="btn btn-outline-pink" @click="clickUpload()">업로드</button>
        <!-- <button v-else class="btn btn-outline-pink" @click="clickOK()">확인</button> -->
        <v-app v-else> 
          <v-bottom-sheet v-model="sheet" persistent>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="#FEA59C"
                outlined
                v-bind="attrs"
                v-on="on"
              >
                확인
              </v-btn>
            </template>
            <v-sheet class="text-center" :height="height">
              <div class="scallop-down"></div>
              <h3>공개 범위</h3>
              <v-container>
                <v-radio-group v-model="radios" :mandatory="false">
                  <v-radio label="전원 공개" value="All" color="#FEA59C"></v-radio>
                  <v-radio label="부부 한정" value="Couple" color="#FEA59C"></v-radio>
                  <v-radio @click="changeHeight" label="세부 설정" value="Others" color="#FEA59C"></v-radio>
                </v-radio-group>
                <!-- 토글 부분 -->
                  <v-btn-toggle
                  v-model="toggle_exclusive"
                  multiple
                  class="py-2"
                  v-if="radios=='Others'"
                >
                  <v-btn 
                    value="부부" 
                    outlined 
                    color="#FEA59C">
                    부부
                  </v-btn>
                  <v-btn value="친가" outlined color="#FEA59C">
                    친가
                  </v-btn>
                  <v-btn value="외가" outlined color="#FEA59C">
                    외가
                  </v-btn>
                  <v-btn value="친구/지인" outlined color="#FEA59C">
                    친구/지인
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
        </v-app>

      </div>
    </div>
    <!-- 만약 업로드 된이미지가 없을 경우 -->
    <div v-if="no_image" class="text-center mt-5">
      <img class="crying-baby" src="@/assets/baby.png">
      <h5>업로드 된 이미지가 없습니다.</h5>
    </div>
    <div v-else id="frame" class="row no-gutters">
    </div>
  </div>
</template>

<script>
// var camera1 = document.getElementById('camera1');
// var camera2 = document.getElementById('camera2');
// var camera3 = document.getElementById('camera3');
// var camera4 = document.getElementById('camera4');

// var frame1 = document.getElementById('frame1');
// var frame2 = document.getElementById('frame2');
// var frame3 = document.getElementById('frame3');
// var frame4 = document.getElementById('frame4');


export default {
  name: 'PhotoCreate',
   data(){
    return {
      is_OK: true,
      sheet: false,
      radios: '',
      toggle_exclusive: [],
      height: '45vh',
      no_image: true,
    }
  },
  methods: {
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
      this.$router.push({name: 'PhotoList'})
    },
    changeHeight() {
      this.height = '57vh'
    },
    // change1(e) {
    //   var file = e.target.files[0];
    //   var frame1 = document.getElementById('frame1');
    //   frame1.src = URL.createObjectURL(file)
    // },
    // change2(e) {
    //   var file = e.target.files[0];
    //   var frame2 = document.getElementById('frame2');
    //   frame2.src = URL.createObjectURL(file)
    // },
    // change3(e) {
    //   var file = e.target.files[0];
    //   var frame3 = document.getElementById('frame3');
    //   frame3.src = URL.createObjectURL(file)
    // },
    change4(e) {
      var files = e.target.files
      console.log(files)
      var frame = document.getElementById('frame');
      for (var file of files) {
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
        // i.classList.add("img-fluid")
        div.appendChild(i)
        frame.appendChild(div)
        this.is_OK = false
      }
    },
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

// #frame > {
//   .col-4 >{
//     img {
//       object-fit: cover;
//       object-position: 50% 50%;
//       width: 30vw; 
//       height: 30vw;
//       overflow:hidden;
//       margin-right: 2.5vw;
//     }
//   }
// }

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

// .v-btn--outlined {
//   outline: 1px solid#FEA59C;
// }

.v-item-group {
  padding:0;
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

</style>