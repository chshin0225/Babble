<template>
  <div class="background1">
    <div class="container bg-light-ivory enroll-form">
      <h3 class="color-pink text-center">초대 코드 등록</h3>
      <div class="image-sect mt-5" style="text-align:center">
        <img src="../../assets/images/accounts/envelope.png">
      </div>
        
      <div class="input-with-label">
        <input 
          v-model="inviteLink"
          class="inputs"
          id="inviteLink"
          placeholder="초대 코드를 입력해주세요." 
          type="text" 
          autocapitalize="none"
          autocorrect="none"
          style="text-transform:lowercase"
        />
        <label for="inviteLink"></label>
      </div>
      <div class="buttons mt-5">
        <button class="btn btn-pink" :class="{disabled: !isSubmit}" @click="clickLink">링크 입력 완료</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'RegisterInviteLink',
  data() {
    return {
      inviteLink: "",
      isSubmit: false,
    };
  },
  created() {
    this.component = this;
  },
  watch: {
    inviteLink: {
      deep: true,
      handler() {
        this.checkInviteLink();
      }
    }
  },
  methods: {
    
    checkInviteLink() {
      
      // 버튼 활성화
      if (this.inviteLink.length > 0 ){
        this.isSubmit = true;
      }else{
        this.isSubmit = false;
      }
     
    },
    clickLink() {
      if ( this.isSubmit ){
        this.enrollInviteLink(this.signupData)
      }
    },
    toLogin() {
      this.$router.push({name: "Login"});
    },
    ...mapActions('accountStore', ['enrollInviteLink'])
  }
}
</script>

<style scoped>
.container {
  width: 80%;
  border-radius: 25px;
}
h3 {
  color: #FEA59C;
  font-weight: 800;
}
.inputs {
  border-style: none;
  border-bottom: 1px solid #aea4a3;
  background-color: transparent;
  width: 100%;
  padding: 10px;
  padding-left: 10px;
  padding-right: 10px;
  margin-top: 30px;
}
.btn{
  width:100%;
}
.disabled,
.disabled:hover {
  background-color: rgb(176, 127, 122, 0.25) !important;
  color: #f8f8f8 !important;
  cursor: inherit !important;
}
.background {
  background-image: url("https://user-images.githubusercontent.com/25967949/90751489-27ce4480-e311-11ea-93aa-2ab9d1f41b4e.png");
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  background-repeat: repeat;
}
.enroll-form {
  margin-top: 5vh !important;
  opacity: 0.9;
}

.image-sect img {
  max-width: 40vw;
  height: auto;
}
</style>