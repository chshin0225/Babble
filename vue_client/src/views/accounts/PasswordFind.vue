<template>
  <div class="background1">
    <div class="container p-3 mt-5 bg-light-ivory formatting">
      <h3>비밀번호 찾기</h3>
      <div class="mt-3">
        비밀번호를 잃어버리셨나요?<br>
        Babble에 가입한 이메일을 정확히 입력해 주세요.<br>
        이메일을 통해 비밀번호 변경 메일이 전송됩니다.</div>

      <div class="input-with-label mt-3">
        <input 
          v-model="passwordFindData.email" 
          v-bind:class="{error : error.email, complete:!error.email&&passwordFindData.email.length!==0}"
          class="inputs"
          id="email" 
          placeholder="이메일" 
          type="text" 
          autocapitalize="none"
          autocorrect="none"
          style="text-transform:lowercase"
          required
          @click="isSubmit && findPassword(passwordFindData)"
          />
        <label for="email"></label>
        <div class="error-text ml-3" v-if="error.email">{{error.email}}</div>
      </div>
      <div class="buttons mt-5 ">
        <button class="btn done-button" :class="{disabled: !isSubmit}" @click="isSubmit && findPassword(passwordFindData)" >입력완료</button>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'PasswordFind',
  data() {
    return {
      passwordFindData: {
        email: ""
      },
      error: {
        email: false,
      },
      isSubmit: false
    }
  },
  created() {
    this.component = this;
  },
  watch: {
    passwordFindData: {
      deep: true,
      handler() {
        this.checkEmailForm();
      }
    },
  },
  methods: {
    checkEmailForm() {
      if ( this.passwordFindData.email.length > 0 && !this.validEmail(this.passwordFindData.email) ) {
        this.error.email = "올바른 이메일 형식이 아니에요"   
      }
      else this.error.email = false;
      let isSubmit = true;
      Object.values(this.error).map(v => {
        if (v) isSubmit = false;
      });
      this.isSubmit = isSubmit;
    },
    validEmail(email) {
      // eslint-disable-next-line
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
    clickDone() {
      if ( this.isSubmit ){
        this.$router.push({name: 'PasswordFindEmail'})
      }
    }
  },
}
</script>

<style scoped>
.container {
  width: 80%;
  border-radius: 20px;
}
h3 { 
  color: #FEA59C;
  font-weight: 900;
}
.inputs {
  border-style: none;
  border-bottom: 1px solid #d6cbbd;
  background-color: transparent;
  width: 100%;
  padding: 10px;
  padding-left: 20px;
  margin-top: 20px;
}
.inputs:focus {
  border-style: none;
  border-bottom: 2px solid #d6cbbd;
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
}
.done-button{
  background-color: #FEA59C;
  color: #F8F8F8;
  width: 100%;
}
.done-button:hover {
  background-color: #A05E58;
  color: #F8F8F8;
}
.disabled, .disabled:hover {
  background-color: rgb(176, 127, 122, 0.25);
  color: #F8F8F8;
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
  margin-top: 10vh !important;
  opacity: 0.9;
}
</style>