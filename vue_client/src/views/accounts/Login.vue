<template>
  <div class="background1">
    <div class="container p-3 mt-5 bg-light-ivory login-form">
      <div class="input-with-label">
        <input
          v-model="loginData.email"
          v-bind:class="{errorText : error.email, complete:!error.email&&loginData.email.length!==0}"
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
          v-model="loginData.password"
          v-bind:class="{errorText : error.password, complete:!error.password&&loginData.password.length!==0}"
          class="inputs"
          id="password"
          type="password"
          placeholder="비밀번호를 입력하세요."
          required
          @keyup.enter="clickLogin"
        />
        <label for="password"></label>
        <div class="error-text ml-3" v-if="error.password">{{error.password}}</div>
      </div>
      <p class="my-3">
        <span class="items" @click="clickSignup">회원가입하기</span>ㆍ
        <span class="items" @click="clickPasswordFind">비밀번호 찾기</span>
      </p>
      <div class="buttons mt-3">
        <button class="btn login-button" :class="{disabled: !isSubmit}" @click="clickLogin">로그인하기</button>
      </div>

      <hr class="divide" />

      <div class="buttons d-flex justify-content-center">
        <button
          class="btn kakao d-flex align-items-center justify-content-center"
          @click="kakaoLogin"
        >
          <i class="xi-2x xi-kakaotalk text-dark"></i>
          <span class="justify-content-center">카카오 아이디 로그인</span>
        </button>
      </div>
      <div class="buttons mt-2 d-flex justify-content-center mx-auto px-0">
        <button
          class="btn google d-flex align-items-center justify-content-center"
          @click="handleClickSignIn"
        >
          <img
            class="google-logo"
            src="https://user-images.githubusercontent.com/57381062/88908677-291dcb80-d295-11ea-8a24-2a96837dd714.png"
            width="32px"
            height="32px"
          />
          <span class="justify-content-center">구글 아이디 로그인</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import router from '@/router';

export default {
  name: "Login",
  data() {
    return {
      loginData: {
        email: "",
        password: "",
      },
      error: {
        email: false,
        password: false,
      },
      isSubmit: false
    };
  },
  watch: {
    loginData: {
      deep: true,
      handler() {
        this.checkEmailForm();
        this.checkPasswordForm();
      },
    },
  },
  methods: {
    ...mapActions("accountStore", ["login", "socialLogin"]),
    async handleClickSignIn() {
      const googleUser = await this.$gAuth.signIn();
      const profile = googleUser.getBasicProfile();
      const userInfo = {
        name: profile.getName(),
        email: profile.getEmail(),
        user_type: "google",
      };
      this.socialLogin(userInfo)
    },
    kakaoLogin() {
      window.Kakao.Auth.login({
        scope: "profile, account_email",
        success: this.GetMe
      });
    },
    GetMe() {
      window.Kakao.API.request({
        url: "/v2/user/me",
        success: res => {
          const kakao_account = res.kakao_account;
          const userInfo = {
            name: kakao_account.profile.nickname,
            email: kakao_account.email,
            user_type: "kakao",
          };
          if (userInfo.email === undefined) {
            router.push({
              name: "SignupKakao",
              params: {
                name: userInfo.name,
                user_type: userInfo.user_type,
              },
            });
          } else {
            this.socialLogin(userInfo)
          }
        },
      });
    },
    clickLogin() {
      if (this.isSubmit) {
        this.login(this.loginData);
      }
    },
    checkEmailForm() {
      if (
        this.loginData.email.length > 0 &&
        !this.validEmail(this.loginData.email)
      ) {
        this.error.email = "올바른 이메일 형식이 아니에요";
      } else this.error.email = false;
    },
    validEmail(email) {
      // eslint-disable-next-line
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
    checkPasswordForm() {
      if (
        this.loginData.password.length > 0 &&
        this.loginData.password.length < 8
      ) {
        this.error.password = "비밀번호가 너무 짧아요";
      } else if (
        this.loginData.password.length >= 8 &&
        !this.validPassword(this.loginData.password)
      ) {
        this.error.password = "영문, 숫자 포함 8 자리 이상이어야 해요.";
      } else this.error.password = false;
      // 버튼 활성화
      if (
        this.loginData.password.length > 0 &&
        this.loginData.email.length > 0
      ) {
        let isSubmit = true;
        Object.values(this.error).map((v) => {
          if (v) isSubmit = false;
        });
        this.isSubmit = isSubmit;
      }
    },
    validPassword(password) {
      var va = /^(?=.*\d)(?=.*[a-z])(?=.*[a-zA-Z]).{8,}$/;
      return va.test(password);
    },
    clickSignup() {
      router.push({ name: "Signup" });
    },
    clickPasswordFind() {
      router.push({ name: "PasswordFind" });
    },
  }
};
</script>

<style scoped>
.login-form {
  margin-top: 2.5vh !important;
  text-align: center;
  opacity: 0.9;
  /* border: 1px solid #FEA59C; */
}
.container {
  width: 80%;
  border-radius: 25px;
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
.login-button {
  background-color: #FEA59C;
  box-shadow: 3px 3px 3px 0px rgb(0, 0, 0, 0.2);
  color: #f8f8f8;
  width: 100%;
}
.divide {
  width: 100%;
  border-top: 1px solid #aea4a3;
  margin-left: auto;
  margin-right: auto;
}
.kakao {
  background-color: #ffe812;
  box-shadow: 3px 3px 3px 0px rgb(0, 0, 0, 0.2);
  border-radius: 5px;
  width: 100%;
}
.google {
  background-color: #ffffff;
  box-shadow: 3px 3px 3px 0px rgb(0, 0, 0, 0.2);
  border-radius: 5px;
  width: 100% !important;
}
.inputs:focus {
  border-style: none;
  border-bottom: 2px solid #d6cbbd;
  outline-style: none;
}
input[type="password"] {
  font-family: sans-serif;
}
.errorText,
.errorText:focus {
  border-bottom: 2px solid rgb(250, 25, 59, 0.7);
}
.error-text {
  color: rgb(250, 25, 59, 0.7);
  text-align: left;
  /*padding-left: 30px;*/
}
.login-button:hover {
  /*background-color: #3c755a;*/
  background-color: #A05E58;
  color: #f8f8f8;
}
.disabled,
.disabled:hover {
  /*background-color: rgb(136, 154, 152, 0.25);*/
  background-color: rgb(176, 127, 122, 0.25);
  color: #f8f8f8;
  cursor: inherit;
}
.items:hover {
  cursor: pointer;
  color: #d6cbbd;
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
.formatting {
  opacity: 0.9;
}

.v-application >>> .error {
  background-color: none !important;
}
</style>