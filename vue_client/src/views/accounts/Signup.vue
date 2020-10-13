<template>
  <div class="background1">
    <div class="container p-3 bg-light-ivory signup-form">
      <h3 class="color-blue">회원가입</h3>
      <div class="input-with-label">
        <input 
          v-model="signupData.name"
          v-bind:class="{errorText: error.name, complete:!error.name&&signupData.name.length!==0}"
          class="inputs"
          id="name"
          placeholder="닉네임" 
          type="text" 
          autocapitalize="none"
          autocorrect="none"
          style="text-transform:lowercase"
        />
        <label for="name"></label>
        <div class="error-text ml-3" v-if="error.name">{{error.name}}</div>
      </div>

      <div class="input-with-label">
        <input 
          v-model="signupData.email" 
          v-bind:class="{errorText : error.email, complete:!error.email&&signupData.email.length!==0}"
          class="inputs"
          id="email" 
          placeholder="이메일" 
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
          v-model="signupData.password1" 
          
          v-bind:class="{errorText : error.password1, complete:!error.password1&&signupData.password1.length!==0}"
          class="inputs"
          id="password1" 
          type="password"
          placeholder="비밀번호를 입력하세요." 
          required
        />
        <label for="password1"></label>
        <div class="error-text ml-3" v-if="error.password1">{{error.password1}}</div>
      </div>

      <div class="input-with-label">
        <input
          v-model="signupData.password2"
          type="password"
          id="password1-confirm"
          v-bind:class="{errorText : error.password2, complete:!error.password2&&signupData.password2.length!==0}"
          placeholder="비밀번호를 다시 입력해주세요."
          class="inputs"
          required
          @keyup.enter="clickSignup"
        />
        <label for="password1-confirm"></label>
        <div class="error-text ml-3" v-if="error.password2">{{error.password2}}</div>
      </div>
      <div class="buttons mt-3">
        <button class="btn signup-button" :class="{disabled: !isSubmit}" @click="clickSignup">가입하기</button>
      </div>
      <div class="buttons mt-3">
        <button class="btn signup-button" @click="toLogin">로그인 하러 가기</button>
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
        password1: "",
        password2: "",
        name: "",
      },
      error: {
        email: false,
        name: false,
        password1: false,
        password2: false,
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
        this.checknameForm();
        this.checkEmailForm();
        this.checkpassword1Form();
        this.checkpassword2ationForm();
      }
    }
  },
  methods: {
    checknameForm() {
      if ( this.signupData.name.length > 0) {
        this.error.name = false;
      }
      else this.error.name="닉네임을 입력해주세요."
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
    checkpassword1Form() {
      if (this.signupData.password1.length > 0 && this.signupData.password1.length < 8) {
          this.error.password1 = "비밀번호가 너무 짧아요"
        } else if ( this.signupData.password1.length >= 8 && !this.validpassword1(this.signupData.password1) ) {
          this.error.password1 = "영문, 숫자 포함 8 자리 이상이어야 해요.";
        } else this.error.password1 = false;
    },
    validpassword1(password1) {
      var va = /^(?=.*\d)(?=.*)(?=.*[a-zA-Z]).{8,}$/;
      return va.test(password1);
    },
    checkpassword2ationForm() {
      if (this.signupData.password1.length >= 8 && this.validpassword1(this.signupData.password1)) {
         if (this.signupData.password1 !== this.signupData.password2 )
        this.error.password2 = "비밀번호가 일치하지 않아요."
      else this.error.password2 = false;
      }
      
      // 버튼 활성화
      if (this.signupData.name.length > 0 && this.signupData.email.length > 0 && this.signupData.password1.length > 0 && this.signupData.password2.length > 0){
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
.signup-button{
  background-color: #FEA59C;
  color: #F8F8F8;
  width: 100%;
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
.errorText, .errorText:focus {
  border-bottom: 2px solid rgb(250, 25, 59, 0.7); 
}
.error-text {
  color: rgb(250, 25, 59, 0.7);
  text-align: left;
  /*padding-left: 30px;*/
}
.signup-button:hover {
  /*background-color: #3c755a;*/
  background-color: #A05E58;
  color: #F8F8F8;
}
.disabled, .disabled:hover {
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
  margin-top:7.5vh !important;
  opacity: 0.9;
  text-align: center;
  background: #fafafa;
}
.items:hover {
  cursor: pointer;
  color: #d6cbbd;
}
</style>