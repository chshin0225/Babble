<template>
  <div class="background1">
    <div class="container p-3 mt-5 bg-light-ivory enroll-form">
      <h3 class="color-pink">아기 등록</h3>

      <div class="mt-4 guide-text">
        아기의 이름을 입력해 주세요.
      </div>
      <div class="input-with-label">
        <input 
          v-model="enrollData.baby.baby_name"
          v-bind:class="{errorText: error.baby_name, complete:!error.baby_name&&enrollData.baby.baby_name.length!==0}"
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
        <button class="btn girl-button" style="float:left;" :class="{selected: enrollData.baby.gender=='F'}" @click="clickGirlBtn">여자 아기</button>
        <button class="btn boy-button" style="float:right;" :class="{selected: enrollData.baby.gender=='M'}" @click="clickBoyBtn">남자 아기</button>
        <label for="gender"></label>
        <div class="error-text ml-2" v-if="error.gender">{{error.gender}}</div>
        <div style="float:left; width:100%; margin-bottom:30px"/>
      </div>

      <div class="mt-4 guide-text">
        아기의 출생일자를 선택해 주세요.
      </div>
      <div class="input-with-label">
        <input 
          v-model="enrollData.baby.birth" 
          v-bind:class="{errorText : error.birth, complete:!error.birth&&enrollData.baby.birth.length!==0}"
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
          v-model="enrollData.relationship_name" 
          
          v-bind:class="{errorText: error.relationship_name, complete:!error.relationship_name&&enrollData.relationship_name.length!==0}"
          class="inputs"
          id="relationship_name" 
          type="text"
          placeholder="관계" 
          required
        />
        <label for="relationship_name"></label>
        <div class="error-text ml-2" v-if="error.relationship_name">{{error.relationship_name}}</div>
      </div>

        <div class="mt-4" style="font-size:20px; color:#bbbbbb;">
          선택사항
        </div>

      <div class="mt-3 guide-text">
        출생 시 아기의 키를 입력해 주세요.
      </div>
      <div class="input-with-label">
        <input
          v-model="enrollData.baby.birth_height"
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
          v-model="enrollData.baby.birth_weight"
          type="number"
          id="birth_weight"
          placeholder="몸무게"
          class="inputs"
          required
          @keyup.enter="clickEnroll"
        />
        <label for="birth_weight"></label>
      </div>
      
      <div class="buttons mt-5">
        <button class="btn new-button" :class="{disabled: !isSubmit}" @click="clickEnroll">아기를 새로 등록합니다.</button>
      </div>
    </div>
    <div style="height:15vh"></div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'RegisterBaby',
  data() {
    return {
      enrollData: {
        baby: {
          baby_name: "",
          gender: "",
          birth: "",
          birth_height: "",
          birth_weight: "",
          profile_image: "profileimage",
        },
        relationship_name: ""
      },
      error: {
        baby_name: false,
        gender: false,
        birth: false,
        relationship_name: false,
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
        this.checkbaby_nameForm();
        this.checkGenderForm();
        this.checkBirthForm();
        this.checkrelationship_nameForm();
      }
    }
  },
  methods: {
    clickGirlBtn(){
      this.enrollData.baby.gender = 'F';
    },
    clickBoyBtn(){
      this.enrollData.baby.gender = 'M';
    },
    checkbaby_nameForm() {
      if ( this.enrollData.baby.baby_name.length > 0) {
        this.error.baby_name = false;
      }
      else this.error.baby_name = "아기의 이름을 입력해 주세요."
    },
    checkGenderForm() {
      if ( this.enrollData.baby.gender.length > 0) {
        this.error.gender = false;
      }
      else this.error.gender = "아기의 성별을 선택해 주세요."
    },
    checkBirthForm() {
      if ( this.enrollData.baby.birth.length > 0) {
        this.error.birth = false;
      }
      else this.error.birth = "아기의 출생일자를 선택해 주세요."
    },
    checkrelationship_nameForm() {
      if ( this.enrollData.relationship_name.length > 0) {
        this.error.relationship_name = false;
      }
      else this.error.relationship_name = "아기와의 관계를 입력해 주세요."
      
      // 버튼 활성화
      if (this.enrollData.baby.baby_name.length > 0 && this.enrollData.baby.gender.length > 0 && this.enrollData.baby.birth.length > 0 && this.enrollData.relationship_name.length > 0){
        let isSubmit = true;
        Object.values(this.error).map(v => {
          if (v) isSubmit = false;
        });
        this.isSubmit = isSubmit;
      }
    },
    clickEnroll() {
      if ( this.isSubmit ){
        this.enrollData.baby.birth_height = Number(this.enrollData.baby.birth_height)
        this.enrollData.baby.birth_weight = Number(this.enrollData.baby.birth_weight)
        console.log("HELLO")
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
.errorText, .errorText:focus {
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