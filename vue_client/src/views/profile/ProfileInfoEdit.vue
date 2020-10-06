<template>
  <div>
    <div class="text-center mt-5">
      <h5 class="main-title text-center color-pink">Profile 변경</h5>

      <div class="profile-image-outline">
        <img class="profile-image" src="@/assets/test.jpg" />
      </div>
    </div>

      <div class="setting-form">
        <v-text-field 
          label="이름"
          v-model="name"
          :rules="[rules.required]"
        ></v-text-field>

        <v-text-field
          v-model="curpassword"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="show1 ? 'text' : 'password'"
          :rules="[rules.cmatch]"
          label="현재 비밀번호"
          @click:append="show1 = !show1"
        ></v-text-field>
          <!--  hint="At least 8 characters"
                counter -->
        <v-text-field
          v-model="newpassword"
          :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="show2 ? 'text' : 'password'"
          :rules="[rules.minLen]"
          label="새 비밀번호"
          @click:append="show2 = !show2"
        ></v-text-field>

        <v-text-field
          v-model="confirmnewpassword"
          :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="show3 ? 'text' : 'password'"
          :rules="[rules.nmatch]"
          label="새 비밀번호 확인"
          @click:append="show3 = !show3"
        ></v-text-field>
        <div class="text-center mt-5">
          <button
            class="btn new-button"
            :class="{ disabled: !((nickflag && passflag) || (passflag && flagPassword() == 2) )}"
            @click="profileBtn"
          >
            프로필 수정
          </button>
        </div>
        <div style="height: 8vh;"></div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: "Profile",
  computed: {
    ...mapState([ 'myaccount' ]),
  },
  data(){
    return{
      name:"",
      loadedpassword:"asdf1234",
      curpassword:"",
      newpassword:"",
      confirmnewpassword:"",
      show1:false,
      show2:false,
      show3:false,
      nickflag:false,
      passflag:true,
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
        cmatch: value => {
          if ((value.length < 8 && value.length >0) || (value.length !=0 && !this.validPassword(value))){
            this.passflag = false
            return "영문, 숫자 포함 8 자리 이상이어야 해요."
          }
          this.passflag = true && this.flagPassword()
          return true
        },
        minLen: value => {
          if ((value.length < 8 && value.length >0) || (value.length !=0 && !this.validPassword(value))){
            this.passflag = false
            return "영문, 숫자 포함 8 자리 이상이어야 해요."
          }

          this.passflag = true && this.flagPassword()
          return true
        },
        nmatch: value => {
          if (value.length !=0 && value !== this.newpassword){
            this.passflag = false
            return "일치하지 않습니다."
          }

          this.passflag = true && this.flagPassword()
          return true
        },
      }
    }
  },
  methods:{
    ...mapActions('accountStore',['updateProfile']),
    profileBtn(){
      if((this.nickflag && this.passflag) || (this.passflag && this.flagPassword() == 2)){
        const profileData = {
          "currentPassword": this.curpassword,
          "newPassword": this.newpassword,
          "confirmNewPassword": this.confirmnewpassword,
          "name": this.name
        }

        this.updateProfile(profileData)
      }

    },
    validPassword(password) {
      var va = /^(?=.*\d)(?=.*[a-z])(?=.*[a-zA-Z]).{8,}$/;
      return va.test(password);
    },
    flagPassword(){
      if (this.curpassword.length == 0 && this.newpassword.length ==0 && this.confirmnewpassword ==0){
        return 1
      }
      else if(this.curpassword.length != 0 && this.newpassword.length !=0 && this.confirmnewpassword !=0){
        return 2
      }
      return false
    }
  },
  mounted: function(){
    this.name = this.myaccount.name
    //this.loadedpassword = 
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
#circle {
  position: relative;
  left: 70%;
  bottom: 20%;
  width: 20%;
  height: 20%;

  background-color: #fea59c;
  border-radius: 50%;
}

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
</style>
