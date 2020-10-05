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
        ></v-text-field>

        <v-text-field
          v-model="curpassword"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="show1 ? 'text' : 'password'"
          label="현재 비밀번호"
          @click:append="show1 = !show1"
        ></v-text-field>
          <!--  hint="At least 8 characters"
                counter -->
        <v-text-field
          v-model="newpassword"
          :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="show2 ? 'text' : 'password'"
          label="새 비밀번호"
          @click:append="show2 = !show2"
        ></v-text-field>

        <v-text-field
          v-model="confirmnewpassword"
          :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="show3 ? 'text' : 'password'"
          label="새 비밀번호 확인"
          @click:append="show3 = !show3"
        ></v-text-field>
        <div class="text-center mt-5">
          <button
            class="btn new-button"
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
import { mapState } from 'vuex'

export default {
  name: "Profile",
  computed: {
    ...mapState([ 'myaccount' ]),
  },
  data(){
    return{
      name:"",
      curpassword:"",
      newpassword:"",
      confirmnewpassword:"",
      show1:false,
      show2:false,
      show3:false,
    }
  },
  methods:{
    profileBtn(){
      console.log(this.myaccount.name)
    }
  },
  mounted: function(){
    this.name = this.myaccount.name
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
