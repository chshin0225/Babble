<template>
  <div>
    <div class="text-center mt-5">
      <!-- <h5 class="main-title text-center color-pink">Profile 변경</h5>

      <div class="profile-image-outline">
        <img class="profile-image" src="@/assets/test.jpg" />
      </div> -->
      <div style="width:100%; text-align:center; padding: 0 10vw;">
      <!-- <img src="http://bit.do/babbleprofile" style="width:50vw; height:50vw; border-radius:50%; border: 5px solid #fea59c;"> -->
      <img 
        v-if="this.profile_image"
        :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + this.profile_image + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" 
        style="width:50vw; height:50vw; border-radius:50%; border: 5px solid #fea59c;">
      <img v-else style="width:50vw; height:50vw; border-radius:50%; border: 5px solid #fea59c;" src="@/assets/babble_logo.png" />


      <div id="circle" 
          style="position: relative;
                left: 48vw;
                bottom: 12vw;
                width: 15vw;
                height: 15vw;
                background-color: #fea59c;
                border-radius: 50%;
                cursor:pointer" 
          @click="clickUpload()">
        <!-- <router-link :to="{ name: 'ProfilePhotoEdit' }" class="view pointer"> -->
          <input @change="change4" type="file" id="file" name="file" hidden>
          <img class="photo-edit" style="width: 60%; transform: translate(0%, 30%);" src="@/assets/Camera_r.png"/>
        <!-- </router-link> -->
      </div>
    </div>
    </div>

      <div class="setting-form">
        <v-text-field 
          label="이름"
          v-model="name"
          :rules="[rules.required]"
        ></v-text-field>

        <div class="text-center">
          <button
            class="btn new-button"
            :class="{ disabled: !(nickflag)}"
            @click="profileBtn"
          >
            프로필 수정
          </button>
        </div>
      </div>
      <div class="setting-form mt-10">
        <v-text-field
          v-model="old_password"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="show1 ? 'text' : 'password'"
          label="현재 비밀번호"
          @click:append="show1 = !show1"
        ></v-text-field>
          <!--  hint="At least 8 characters"
                counter -->
        <v-text-field
          v-model="new_password1"
          :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="show2 ? 'text' : 'password'"
          :rules="[rules.minLen]"
          label="새 비밀번호"
          @click:append="show2 = !show2"
        ></v-text-field>

        <v-text-field
          v-model="new_password2"
          :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="show3 ? 'text' : 'password'"
          :rules="[rules.nmatch]"
          label="새 비밀번호 확인"
          @click:append="show3 = !show3"
        ></v-text-field>
        <div class="text-center mt-5">
          <button
            class="btn new-button"
            :class="{ disabled: !(passflag)}"
            @click="changePW"
          >
            비밀번호 변경
          </button>
        </div>
        <div style="height: 8vh;"></div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import firebase from 'firebase'

export default {
  name: "Profile",
  computed: {
    ...mapState([ 'myaccount' ]),
  },
  data(){
    return{
      name:"",
      profile_image:"", 
      old_password:"",
      new_password1:"",
      new_password2:"",
      photoObj : null,
      show1:false,
      show2:false,
      show3:false,
      nickflag:false,
      passflag:false,
      rules:{
        required: value => {
          if (value.length == 0){
            this.nickflag = false
            return 'This field is required.'
          }
          else if(value === this.myaccount.name){
            this.nickflag = false
            return true
          }
          this.nickflag = true
          return !!value || 'This field is required.'
        },
        minLen: value => {
          if ((value.length < 8 && value.length >0) || (value.length !=0 && !this.validPassword(value))){
            this.passflag = false
            return "영문, 숫자 포함 8 자리 이상이어야 해요."
          }
          if (value.length == 0){
            this.passflag = false
            return true
          }
          this.passflag = true && this.flagPassword()
          return true
        },
        nmatch: value => {
          if (value.length !=0 && value !== this.new_password1){
            this.passflag = false
            return "일치하지 않습니다."
          }
          else if(value.length == 0){
            this.passflag = false
            return true
          }

          this.passflag = true && this.flagPassword()
          return true
        },
      }
    }
  },
  methods:{
    ...mapActions('accountStore', ['changePassword', 'changeProfile']),
    clickUpload() {
      var fileInput = document.getElementById('file')
      fileInput.click()
    },
    change4(e) {
      this.photoObj = e.target.files[0];
      
      const promises = []
      var storageRef = firebase.storage().ref()
      
      const uploadTask = storageRef.child('user_' + this.myaccount.id).child(this.photoObj.name).put(this.photoObj)
      promises.push(uploadTask)
      Promise.all(promises).then(() => {
        this.profile_image = 'user_' + this.myaccount.id + '%2F' + this.photoObj.name;
      })
    },
    profileBtn(){
      if(this.nickflag){
        var profileData = {
                            name : this.name,
                            profile_image : this.profile_image,
                            };
        this.changeProfile(profileData);
      }

    },
    changePW(){
      if(this.passflag){
        var passwordData = {
                            old_password : this.old_password,
                            new_password1 : this.new_password1,
                            new_password2 : this.new_password2 
                            };
        this.changePassword(passwordData);
      }


    },
    validPassword(password) {
      var va = /^(?=.*\d)(?=.*[a-z])(?=.*[a-zA-Z]).{8,}$/;
      return va.test(password);
    },
    flagPassword(){
      if (this.old_password.length == 0 && this.new_password1.length ==0 && this.new_password2 ==0){
        return true
      }
      else if(this.old_password.length != 0 && this.new_password1.length !=0 && this.new_password2 !=0){
        return true
      }
      return false
    }
  },
  mounted: function(){
    this.name = this.myaccount.name
    this.profile_image = this.myaccount.profile_image
  },
  watch: {
    myaccount() {
      if (this.myaccount) {
        this.name = this.myaccount.name;
        this.profile_image = this.myaccount.profile_image;
      }
    },
  }
};
</script>

<style scoped>
.profile-image-outline {
  border: 5px solid #fea59c;
  border-radius: 50%;
  margin: 5vh auto;
  height: 70vw;
  width: 70vw;
}
.profile-image {
  margin-top: -1px;
  margin-left: -1px;
  width: 70vw;
  border-radius: 50%;
}
/*#circle {
  position: relative;
  left: 70%;
  bottom: 20%;
  width: 20%;
  height: 20%;

  background-color: #fea59c;
  border-radius: 50%;
}*/

.main-title {
  font-size: 1.3rem;
  font-weight: 900;
  margin-top: 10%;
}

.setting-form{
    width:70%;
    margin: 0px auto
}

.new-button {
  background-color: #fea59c;
  color: #f8f8f8;
  /* width: 100%; */
}

div >>> .v-text-field__slot  {
  font-family: sans-serif !important;
}

</style>

