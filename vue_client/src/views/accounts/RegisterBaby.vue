<template>
  <div class="background1">
    <div class="container p-3 mt-5 bg-light-ivory signup-form">
      <h3 class="color-pink">아기 등록</h3>

      <div class="input-with-label">
        <input 
          v-model="signupData.nickName"
          v-bind:class="{error: error.nickName, complete:!error.nickName&&signupData.nickName.length!==0}"
          class="inputs"
          id="nickName"
          placeholder="이름, 별명, 태명 등" 
          type="text" 
          autocapitalize="none"
          autocorrect="none"
          style="text-transform:lowercase"
        />
        <label for="nickName"></label>
        <div class="error-text ml-3" v-if="error.nickName">{{error.nickName}}</div>
      </div>
      <div class="buttons mt-3">
        <button class="btn girl-button" style="float:left;" :class="{disabled: !isSubmit}" @click="clickSignup">여자 아기</button>
        <button class="btn boy-button" style="float:right;" :class="{disabled: !isSubmit}" @click="clickSignup">남자 아기</button>
      </div>

      <div class="input-with-label">
        <input 
          v-model="signupData.email" 
          v-bind:class="{error : error.email, complete:!error.email&&signupData.email.length!==0}"
          class="inputs"
          id="email" 
          placeholder="년 월 일" 
          type="text" 
          autocapitalize="none"
          autocorrect="none"
          style="text-transform:lowercase"
          required
          />
        <label for="email"></label>
        <div class="error-text ml-3" v-if="error.email">{{error.email}}</div>
      </div>

      <div class="input-with-label">
        <input 
          v-model="signupData.password" 
          
          v-bind:class="{error : error.password, complete:!error.password&&signupData.password.length!==0}"
          class="inputs"
          id="password" 
          type="password"
          placeholder="관계" 
          required
        />
        <label for="password"></label>
        <div class="error-text ml-3" v-if="error.password">{{error.password}}</div>
      </div>

      <div class="input-with-label">
        <input
          v-model="signupData.passwordConfirm"
          type="password"
          id="password-confirm"
          v-bind:class="{error : error.passwordConfirm, complete:!error.passwordConfirm&&signupData.passwordConfirm.length!==0}"
          placeholder="키"
          class="inputs"
          required
          @keyup.enter="clickSignup"
        />
        <label for="password-confirm"></label>
        <div class="error-text ml-3" v-if="error.passwordConfirm">{{error.passwordConfirm}}</div>
      </div>
      <div class="input-with-label">
        <input
          v-model="signupData.passwordConfirm"
          type="password"
          id="password-confirm"
          v-bind:class="{error : error.passwordConfirm, complete:!error.passwordConfirm&&signupData.passwordConfirm.length!==0}"
          placeholder="몸무게"
          class="inputs"
          required
          @keyup.enter="clickSignup"
        />
        <label for="password-confirm"></label>
        <div class="error-text ml-3" v-if="error.passwordConfirm">{{error.passwordConfirm}}</div>
      </div>
      
      <div class="buttons mt-5">
        <button class="btn new-button" :class="{disabled: !isSubmit}" @click="clickSignup">아기를 새로 등록합니다.</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'Signup',
  data() {
    return {
      signupData: {
        email: "",
        password: "",
        passwordConfirm: "",
        nickName: "",
      },
      error: {
        email: false,
        nickName: false,
        password: false,
        passwordConfirm: false,
      },
      isSubmit: false,
    };
  },
  created() {
    this.component = this;
  },
  watch: {
    signupData: {
      deep: true,
      handler() {
        this.checknickNameForm();
        this.checkEmailForm();
        this.checkPasswordForm();
        this.checkPasswordConfirmationForm();
      }
    }
  },
  methods: {
    checknickNameForm() {
      if ( this.signupData.nickName.length > 0) {
        this.error.nickName = false;
      }
      else this.error.nickName="닉네임을 입력해주세요."
    },
    checkEmailForm() {
      if ( this.signupData.email.length > 0 && !this.validEmail(this.signupData.email) ) {
        this.error.email = "올바른 이메일 형식이 아니에요"   
      }
      else this.error.email = false;
    },
    validEmail(email) {
      // eslint-disable-next-line
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
    checkPasswordForm() {
      if (this.signupData.password.length > 0 && this.signupData.password.length < 8) {
          this.error.password = "비밀번호가 너무 짧아요"
        } else if ( this.signupData.password.length >= 8 && !this.validPassword(this.signupData.password) ) {
          this.error.password = "영문, 숫자 포함 8 자리 이상이어야 해요.";
        } else this.error.password = false;
    },
    validPassword(password) {
      var va = /^(?=.*\d)(?=.*[a-z])(?=.*[a-zA-Z]).{8,}$/;
      return va.test(password);
    },
    checkPasswordConfirmationForm() {
      if (this.signupData.password.length >= 8 && this.validPassword(this.signupData.password)) {
         if (this.signupData.password !== this.signupData.passwordConfirm )
        this.error.passwordConfirm = "비밀번호가 일치하지 않아요."
      else this.error.passwordConfirm = false;
      }
      
      // 버튼 활성화
      if (this.signupData.nickName.length > 0 && this.signupData.email.length > 0 && this.signupData.password.length > 0 && this.signupData.passwordConfirm.length > 0){
        let isSubmit = true;
        Object.values(this.error).map(v => {
          if (v) isSubmit = false;
        });
        this.isSubmit = isSubmit;
      }
     
    },
    clickSignup() {
      if ( this.isSubmit ){
        this.signup(this.signupData)
      }
    },
    toLogin() {
      this.$router.push({name: "Login"});
    },
    ...mapActions('accountStore', ['signup'])
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
  margin-top: 20px;
}
.new-button{
  background-color: #FEA59C;
  color: #F8F8F8;
  width: 100%;
}
.girl-button{
  background-color: #F8F8F8;
  border-color: #FEA59C;
  color: #FEA59C;
  width: 49.5%;
}
.boy-button .selected{
  background-color: #FEA59C;
  color: #F8F8F8;
  width: 49.5%;
}
.boy-button{
  background-color: #F8F8F8;
  border-color: #9BC7FF;
  color: #9BC7FF;
  width: 49.5%;
}
.boy-button .selected{
  background-color: #9BC7FF;
  color: #F8F8F8;
  width: 49.5%;
}
.divide {
  width: 10%;
  border-top: 1px solid #FEA59C;
  margin-left: auto;
  margin-right: auto;
}
.kakao {
  background-color: #ffe812;
  border-radius: 5px;
  width: 70%;
}
.google {
  background-color:  #FFFFFF;
  border-radius: 5px;
  width: 70%;
}
.inputs:focus {
  border-style: none;
  border-bottom: 2px solid #D6CBBD;
  outline-style: none;
}
input[type="password"] {
  font-family:sans-serif;
}
.error, .error:focus {
  border-bottom: 2px solid rgb(250, 25, 59, 0.7); 
}
.error-text {
  color: rgb(250, 25, 59, 0.7);
  text-align: left;
  padding-left: 30px;
}
.new-button:hover {
  /*background-color: #3c755a;*/
  background-color: #A05E58;
  color: #F8F8F8;
}
.new-button .disabled, .new-button .disabled:hover {
  /*background-color: rgb(136, 154, 152, 0.25);*/
  background-color: rgb(176, 127, 122, 0.25);
  color: #F8F8F8;
  cursor: inherit;
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
.signup-form {
  margin-top: 15vh !important;
  opacity: 0.9;
}
.items:hover {
  cursor: pointer;
  color: #d6cbbd;
}
</style>