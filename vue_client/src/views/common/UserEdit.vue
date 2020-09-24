<template>

  <div style="padding:0 5vw">
    
    <div style="width:100%;">
        <div style="float:right;">
        <button class="btn btn-outline-pink" style="">전체선택</button>
        <button class="btn btn-outline-pink" style="margin-left:6px !important;">그룹에 추가</button>
      </div>
    </div>
    <v-app style="width:100%;">


      <v-checkbox v-model="checkbox1" label="강슬기"></v-checkbox>
      <v-checkbox v-model="checkbox1" label="박선환"></v-checkbox>
      <v-checkbox v-model="checkbox1" label="방소윤"></v-checkbox>
      <v-checkbox v-model="checkbox1" label="이근우"></v-checkbox>
      <v-checkbox v-model="checkbox1" label="신채원"></v-checkbox>
      <v-checkbox v-model="checkbox1" label="신채린"></v-checkbox>

    </v-app>
  </div>
</template>

<script>


export default {
  name: 'UserEdit',
  data() {
    return {
      
    }
  },
}
</script>

<style scoped>

  button {
    border-radius:0.5rem;
    padding: 0.3rem 0.5rem; 
    margin: 0 !important;
  }
</style>