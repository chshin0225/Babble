<template>
  <div>
    <div class="text-center mt-5">
      <h5 class="main-title text-center color-pink">Profile</h5>

      <div class="profile-image-outline">
        <img class="profile-image" src="@/assets/test.jpg" />
        <div id="circle">
          <img class="photo-edit" src="@/assets/Camera_r.png" />
        </div>
      </div>

      <div class="profile-info">
        <v-text-field
          value="아기의 아버지"
          label="User Name"
          outlined
          readonly
        ></v-text-field>
        <v-text-field
          value="dlrmsdn135@naver.com"
          label="E-mail"
          outlined
          readonly
        ></v-text-field>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Profile",
};
</script>

<style scoped>
.profile-image-outline {
  border: 5px solid #fea59c;
  border-radius: 50%;
  margin: 5vh auto;
  height: 70vw;
  width: 70vw;
}
.profile-image {
  margin-top: -1px;
  margin-left: -1px;
  width: 70vw;
  border-radius: 50%;
}
#circle {
  position: relative;
  left: 70%;
  bottom: 20%;
  width: 20%;
  height: 20%;

  background-color: #fea59c;
  border-radius: 50%;
}
.photo-edit {
  width: 60%;
  transform: translate(0%, 30%);
}

.main-title {
  font-size: 1.3rem;
  font-weight: 900;
  margin-top: 20%;
}
.profile-info {
  position: relative;
  width: 85%;
  left: 7.5%;
}
</style>
