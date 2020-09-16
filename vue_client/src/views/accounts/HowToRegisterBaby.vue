<template>
  <div class="background1">
    <div class="container p-3 mt-5 enroll-form">
      <h3 class="color-pink">아기 등록</h3>
      <div class="image-sect" style="text-align:center;">
        <img src="https://user-images.githubusercontent.com/25967949/93062400-d9ae2600-f6af-11ea-948c-219574892c76.png">
      </div>
      <div class="mt-4" style="font-size:14px; font-weight:bold; text-align:center">
        아기의 정보를 등록해볼까요?</div>
        <div class="mt-3" style="font-size:12px; text-align:center">
          아기를 새로 등록하시거나<br>
          다른 계정에서 발급된 초대 코드를 등록해<br>
          아기의 성장일기를 함께 공유하고<br>
          만들어갈 수 있습니다.
        </div>
      <div class="buttons mt-5">
        <button class="btn btn-pink" @click="clickNewBaby">아기를 새로 등록합니다.</button>
      </div>
      <div class="buttons mt-3">
        <button class="btn btn-blue" @click="clickInviteLink">링크로 초대받았습니다.</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HowToRegisterBaby',
  data() {
    return {
    };
  },
  created() {
    this.component = this;
  },
  methods: {
    clickNewBaby() {
      this.$router.push({ name: "RegisterBaby" });
    },
    clickInviteLink() {
      this.$router.push({ name: "RegisterInviteLink" });
    },
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
.btn {
  width:100%;
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
.image-sect img {
  max-width: 40vw;
  height: auto;
}
</style>