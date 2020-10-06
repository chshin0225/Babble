<template>
  <div class="grid">
    <div style="width:100%; text-align:center">
      <!-- <img src="http://bit.do/babbleprofile" style="width:50vw; height:50vw; border-radius:50%; border: 5px solid #fea59c;"> -->
      <img 
        v-if="enrollData.profile_image"
        :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + enrollData.profile_image + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" 
        style="width:50vw; height:50vw; border-radius:50%; border: 5px solid #fea59c;">

      <img v-else style="width:50vw; height:50vw; border-radius:50%; border: 5px solid #fea59c;" src="@/assets/baby.png" />


      <div id="circle" style="
  position: relative;
  left: 48vw;
  bottom: 12vw;
  width: 15vw;
  height: 15vw;
  background-color: #fea59c;
  border-radius: 50%;">
        <!-- <router-link :to="{ name: 'ProfilePhotoEdit' }" class="view pointer"> -->
          <input @change="change4" type="file" id="file" name="file" hidden>
          <img class="photo-edit" style="width: 60%; transform: translate(0%, 30%);" src="@/assets/Camera_r.png" @click="clickUpload()"/>
        <!-- </router-link> -->
      </div>
    </div>
    
      <div class="guide-text">
        아기의 이름을 입력해 주세요.
      </div>
      <div class="input-with-label">
        <input 
          v-model="enrollData.baby_name"
          v-bind:class="{errorText: error.baby_name, complete:!error.baby_name&&enrollData.baby_name.length!==0}"
          class="inputs"
          style="margin-top:0px"
          id="baby_name"
          placeholder="이름, 별명, 태명 등" 
          type="text" 
          autocapitalize="none"
          autocorrect="none"
        />
        <label for="baby_name"></label>
        <div class="error-text ml-2" v-if="error.baby_name">{{error.baby_name}}</div>
      </div>

      <div class="mt-4 guide-text">
        아기의 성별을 선택해 주세요.
      </div>
      <div class="buttons" style="margin-top:10px; birth_height:auto">
        <button class="btn girl-button" style="float:left;" :class="{selected: enrollData.gender=='F'}" @click="clickGirlBtn">여자 아기</button>
        <button class="btn boy-button" style="float:right;" :class="{selected: enrollData.gender=='M'}" @click="clickBoyBtn">남자 아기</button>
        <label for="gender"></label>
        <div class="error-text ml-2" v-if="error.gender">{{error.gender}}</div>
        <div style="float:left; width:100%; margin-bottom:30px"/>
      </div>

      <div class="mt-4 guide-text">
        아기의 출생일자를 선택해 주세요.
      </div>
      <div class="input-with-label">
        <input 
          v-model="enrollData.birth" 
          v-bind:class="{errorText : error.birth, complete:!error.birth&&enrollData.birth.length!==0}"
          class="inputs"
          id="birth" 
          placeholder="년 월 일" 
          type="date" 
          autocapitalize="none"
          autocorrect="none"
          required
          />
        <label for="birth"></label>
        <div class="error-text ml-2" v-if="error.birth">{{error.birth}}</div>
      </div>

        <div class="mt-4" style="font-size:20px; color:#bbbbbb;">
          선택사항
        </div>

      <div class="mt-3 guide-text">
        출생 시 아기의 키를 입력해 주세요.
      </div>
      <div class="input-with-label">
        <input
          v-model="enrollData.birth_height"
          type="number"
          id="birth_height"
          placeholder="키"
          class="inputs"
          required
          @keyup.enter="clickEnroll"
        />
        <label for="birth_height"></label>
      </div>
      
        <div class="mt-4 guide-text">
          출생 시 아기의 몸무게를 입력해 주세요.
        </div>
      <div class="input-with-label">
        <input
          v-model="enrollData.birth_weight"
          type="number"
          id="birth_weight"
          placeholder="몸무게"
          class="inputs"
          required
          @keyup.enter="clickEnroll"
        />
        <label for="birth_weight"></label>
      </div> 
      <!-- -->
  
    <div class="buttons mt-2">
      <button class="btn change-button" @click="modifyBabyInfo">변경하기</button>
    </div>
    
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import firebase from 'firebase'

export default {
  name: 'BabySetting',
  data() {
    return {
      photoObj : null,
      enrollData: {
        baby_name: "",
        gender: "",
        birth: "",
        birth_height: "",
        birth_weight: "",
        profile_image: "",
        id: "",
      },  
      error: {
        baby_name: false,
        gender: false,
        birth: false,
        relationship_name: false,
      },    
     
    }
  },
  computed: {
    ...mapState(['myaccount', 'currentBaby']),
  },
  created(){

  },
  mounted() {
    this.findMyAccount();
  },
  watch: {
    myaccount() {
      if (this.myaccount) {
        this.findBaby(this.myaccount.current_baby)
        // this.enrollData = this.currentBaby;
      }
    },
    currentBaby() {
      if (this.currentBaby) {
        this.enrollData = this.currentBaby
      }
    }
  },
  /*mounted() {
    this.enrollData = this.currentBaby;
  },*/
  methods:{
    ...mapActions('babyStore', ['modifyBaby']),
    ...mapActions(['findBaby', 'findMyAccount']),

    modifyBabyInfo(){
      this.modifyBaby(this.enrollData);
    },
    clickGirlBtn(){
      this.enrollData.gender = 'F';
    },
    clickBoyBtn(){
      this.enrollData.gender = 'M';
    },
    clickUpload() {
      var fileInput = document.getElementById('file')
      fileInput.click()
    },
    change4(e) {
      console.log("e", e);
      console.log("e.target", e.target);
      console.log("e.target.files", e.target.files[0]);
      this.photoObj = e.target.files[0];
      console.log("this.photoObj", this.photoObj);
      
      const promises = []
      var storageRef = firebase.storage().ref()
      
      const uploadTask = storageRef.child('babble_' + this.myaccount.current_baby).child(this.photoObj.name).put(this.photoObj)
      promises.push(uploadTask)
      Promise.all(promises).then(() => {
        console.log("this.enrollData", this.enrollData);
        this.enrollData.profile_image = 'babble_' + this.myaccount.current_baby + '%2F' + this.photoObj.name;
        console.log("this.enrollData.profile_image", this.enrollData.profile_image);
      })
    },
  }
}
</script>

<style scoped>

.grid {
  padding: 15vw 10vw;
}

.input-title-wrap {
  width:100%;
}

.inputs-wrap {
  width:100%;
}

.input-title {
    color: #595959;
    font-size: 1rem;
    font-weight: 800;
}

.inputs {
  border-style: none;
  background-color: #f5f5f5;
  width: 100%;
  padding: 10px;
  padding-left: 10px;
  padding-right: 10px;
  margin-top: 10px;
}

.inputs:focus {
  border-style: none;
  border: 2px solid #FEA59C;
  border-radius:1vw;
  outline-style: none;
}


.change-button{
  background-color: #FEA59C;
  color: #F8F8F8;
  width: 100%;
}

.girl-button {
  /*background-color: #F8F8F8;*/
  border-color: #FEA59C;
  color: #FEA59C;
  width: 49.5%;
}
.girl-button.selected{
  background-color: #FEA59C !important;
  color: #F8F8F8 !important;
  width: 49.5%;
}
.boy-button{
  /*background-color: #F8F8F8;*/
  border-color: #9BC7FF;
  color: #9BC7FF;
  width: 49.5%;
}
.boy-button.selected{
  background-color: #9BC7FF !important;
  color: #F8F8F8 !important;
  width: 49.5%;
}
</style>