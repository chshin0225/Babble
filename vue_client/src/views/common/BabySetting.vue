<template>
  <div class="grid">
    <div style="width:100%; text-align:center">
      <img src="http://bit.do/babbleprofile" style="width:50vw; height:50vw; border-radius:50%; border:1px solid #888888;">
    </div>
    <div class="input-with-title mt-3">
      <div class="input-title-wrap"><span class="input-title">아기 이름/태명</span></div>
      <div class="inputs-wrap"><input class="inputs" /></div>
    </div>
  
    <div class="buttons mt-2">
      <button class="btn change-button">변경하기</button>
    </div>
    
    <div class="input-with-title mt-5">
      <div class="input-title-wrap"><span class="input-title">비밀번호</span></div>
      <div class="inputs-wrap"><input class="inputs" placeholder="현재 비밀번호" v-model="old_password"/></div>
      <div class="inputs-wrap"><input class="inputs" placeholder="새 비밀번호" v-model="new_password1"/></div>
      <div class="inputs-wrap"><input class="inputs" placeholder="새 비밀번호 확인" v-model="new_password2"/></div>
    </div>
    <div class="buttons mt-2">
      <button class="btn change-button" @click="changePW">변경하기</button>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'BabySetting',
  data() {
    return {
      old_password:"",
      new_password1:"",
      new_password2:"",      
     
    }
  },
  methods:{
    ...mapActions('accountStore', ['changePassword']),
    changePW(){
      let PWData = {
            old_password : this.old_password, 
            new_password1 : this.new_password1, 
            new_password2 : this.new_password2
          }
      this.changePassword(PWData);
    }
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

</style>