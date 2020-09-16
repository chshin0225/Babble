<template>
  <div class="background1">
    <div class="container p-3 mt-5 bg-light-ivory enroll-form">
      <h3 class="color-pink">아기 등록</h3>

      <div class="mt-4 guide-text">
        아기의 이름을 입력해 주세요.
      </div>
      <div class="input-with-label">
        <input 
          v-model="enrollData.babyName"
          v-bind:class="{error: error.babyName, complete:!error.babyName&&enrollData.babyName.length!==0}"
          class="inputs"
          style="margin-top:0px"
          id="babyName"
          placeholder="이름, 별명, 태명 등" 
          type="text" 
          autocapitalize="none"
          autocorrect="none"
        />
        <label for="babyName"></label>
        <div class="error-text ml-2" v-if="error.babyName">{{error.babyName}}</div>
      </div>

      <div class="mt-4 guide-text">
        아기의 성별을 선택해 주세요.
      </div>
      <div class="buttons" style="margin-top:10px; height:auto">
        <button class="btn girl-button" style="float:left;" :class="{selected: enrollData.gender=='girl'}" @click="clickGirlBtn">여자 아기</button>
        <button class="btn boy-button" style="float:right;" :class="{selected: enrollData.gender=='boy'}" @click="clickBoyBtn">남자 아기</button>
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
          v-bind:class="{error : error.birth, complete:!error.birth&&enrollData.birth.length!==0}"
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

      <div class="mt-4 guide-text">
        아기와의 관계를 입력해 주세요.
      </div>
      <div class="input-with-label">
        <input 
          v-model="enrollData.relationship" 
          
          v-bind:class="{error: error.relationship, complete:!error.relationship&&enrollData.relationship.length!==0}"
          class="inputs"
          id="relationship" 
          type="text"
          placeholder="관계" 
          required
        />
        <label for="relationship"></label>
        <div class="error-text ml-2" v-if="error.relationship">{{error.relationship}}</div>
      </div>

        <div class="mt-4" style="font-size:20px; color:#bbbbbb;">
          선택사항
        </div>

      <div class="mt-3 guide-text">
        출생 시 아기의 키를 입력해 주세요.
      </div>
      <div class="input-with-label">
        <input
          v-model="enrollData.height"
          type="number"
          id="height"
          placeholder="키"
          class="inputs"
          required
          @keyup.enter="clickEnroll"
        />
        <label for="height"></label>
      </div>
      
        <div class="mt-4 guide-text">
          출생 시 아기의 몸무게를 입력해 주세요.
        </div>
      <div class="input-with-label">
        <input
          v-model="enrollData.weight"
          type="number"
          id="weight"
          placeholder="몸무게"
          class="inputs"
          required
          @keyup.enter="clickEnroll"
        />
        <label for="weight"></label>
      </div>
      
      <div class="buttons mt-5">
        <button class="btn new-button" :class="{disabled: !isSubmit}" @click="clickEnroll">아기를 새로 등록합니다.</button>
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
      enrollData: {
        babyName: "",
        gender: "",
        birth: "",
        relationship: "",
        height: "",
        weight: "",
      },
      error: {
        babyName: false,
        gender: false,
        birth: false,
        relationship: false,
      },
      isSubmit: false,
    };
  },
  created() {
    this.component = this;
  },
  watch: {
    enrollData: {
      deep: true,
      handler() {
        this.checkbabyNameForm();
        this.checkGenderForm();
        this.checkBirthForm();
        this.checkRelationshipForm();
      }
    }
  },
  methods: {
    clickGirlBtn(){
      this.enrollData.gender = 'girl';
    },
    clickBoyBtn(){
      this.enrollData.gender = 'boy';
    },
    checkbabyNameForm() {
      if ( this.enrollData.babyName.length > 0) {
        this.error.babyName = false;
      }
      else this.error.babyName = "아기의 이름을 입력해 주세요."
    },
    checkGenderForm() {
      if ( this.enrollData.gender.length > 0) {
        this.error.gender = false;
      }
      else this.error.gender = "아기의 성별을 선택해 주세요."
    },
    checkBirthForm() {
      if ( this.enrollData.birth.length > 0) {
        this.error.birth = false;
      }
      else this.error.birth = "아기의 출생일자를 선택해 주세요."
    },
    checkRelationshipForm() {
      if ( this.enrollData.relationship.length > 0) {
        this.error.relationship = false;
      }
      else this.error.relationship = "아기와의 관계를 입력해 주세요."

      // 버튼 활성화
      if (this.enrollData.babyName.length > 0 && this.enrollData.gender.length > 0 && this.enrollData.birth.length > 0 && this.enrollData.relationship.length > 0){
        let isSubmit = true;
        Object.values(this.error).map(v => {
          if (v) isSubmit = false;
        });
        this.isSubmit = isSubmit;
      }
    },
    clickEnroll() {
      if ( this.isSubmit ){
        this.enrollBaby(this.enrollData)
      }
    },
    toLogin() {
      this.$router.push({name: "Login"});
    },
    ...mapActions('accountStore', ['enrollBaby'])
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
  /*margin-top: 20px;*/
}
.new-button{
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
.inputs:focus {
  border-style: none;
  border-bottom: 2px solid #D6CBBD;
  outline-style: none;
}
.error, .error:focus {
  border-bottom: 2px solid rgb(250, 25, 59, 0.7); 
}
.error-text {
  color: rgb(250, 25, 59, 0.7);
  text-align: left;
  padding-left: 0px;
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
.enroll-form {
  margin-top: 10vh !important;
  opacity: 0.9;
}

.guide-text{
  font-size:15px;
  padding-left:10px;
}
</style>