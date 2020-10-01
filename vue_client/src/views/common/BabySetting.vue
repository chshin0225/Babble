<template>
  <div class="grid">
    <div style="width:100%; text-align:center">
      <img src="http://bit.do/babbleprofile" style="width:50vw; height:50vw; border-radius:50%; border:1px solid #888888;">
    </div>
    <!-- <div class="input-with-title mt-3">
      <div class="input-title-wrap"><span class="input-title">아기 이름/태명</span></div>
      <div class="inputs-wrap"><input class="inputs" v-model="enrollData.baby_name" /></div>
    </div>
     -->
    
      <div class="mt-4 guide-text">
        아기의 이름을 입력해 주세요.
      </div>
      <div class="input-with-label">
        <input 
          v-model="enrollData.baby_name"
          v-bind:class="{errorText: error.baby_name, complete:!error.baby_name&&enrollData.baby_name.length!==0}"
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
        <button class="btn girl-button" style="float:left;" :class="{selected: enrollData.gender=='F'}" @click="clickGirlBtn">여자 아기</button>
        <button class="btn boy-button" style="float:right;" :class="{selected: enrollData.gender=='M'}" @click="clickBoyBtn">남자 아기</button>
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
          v-bind:class="{errorText : error.birth, complete:!error.birth&&enrollData.birth.length!==0}"
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

        <div class="mt-4" style="font-size:20px; color:#bbbbbb;">
          선택사항
        </div>

      <div class="mt-3 guide-text">
        출생 시 아기의 키를 입력해 주세요.
      </div>
      <div class="input-with-label">
        <input
          v-model="enrollData.birth_height"
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
          v-model="enrollData.birth_weight"
          type="number"
          id="birth_weight"
          placeholder="몸무게"
          class="inputs"
          required
          @keyup.enter="clickEnroll"
        />
        <label for="birth_weight"></label>
      </div> 
      <!-- -->
  
    <div class="buttons mt-2">
      <button class="btn change-button" @click="modifyBabyInfo">변경하기</button>
    </div>
    
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'BabySetting',
  data() {
    return {
      enrollData: {
        baby_name: "",
        gender: "",
        birth: "",
        birth_height: "",
        birth_weight: "",
        profile_image: "",
        id: "",
      },  
      error: {
        baby_name: false,
        gender: false,
        birth: false,
        relationship_name: false,
      },    
     
    }
  },
  computed: {
    ...mapState(['myaccount', 'currentBaby']),
  },
  mounted() {
    this.enrollData = this.currentBaby;
  },
  methods:{
    ...mapActions('babyStore', ['modifyBaby']),

    modifyBabyInfo(){
      this.modifyBaby(this.enrollData);
    },
    clickGirlBtn(){
      this.enrollData.gender = 'F';
    },
    clickBoyBtn(){
      this.enrollData.gender = 'M';
    },
  }
}
</script>

<style scoped>

.grid {
  padding: 15vw 10vw;
}

.input-title-wrap {
  width:100%;
}

.inputs-wrap {
  width:100%;
}

.input-title {
    color: #595959;
    font-size: 1rem;
    font-weight: 800;
}

.inputs {
  border-style: none;
  background-color: #f5f5f5;
  width: 100%;
  padding: 10px;
  padding-left: 10px;
  padding-right: 10px;
  margin-top: 10px;
}

.inputs:focus {
  border-style: none;
  border: 2px solid #FEA59C;
  border-radius:1vw;
  outline-style: none;
}


.change-button{
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
</style>