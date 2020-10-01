<template>
  <div>
    <div class="text-center mt-5">
      <h5 class="main-title text-center color-pink">Profile</h5>

      <div class="profile-image-outline">
        <img class="profile-image" src="@/assets/test.jpg" />
        <div id="circle">
          <router-link :to="{ name: 'ProfilePhotoEdit' }" class="view pointer">
            <img class="photo-edit" src="@/assets/Camera_r.png" />
          </router-link>
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

      <router-link :to="{ name: 'ProfileInfoEdit' }" class="view pointer">
        <button
          class="btn new-button"
          :class="{ disabled: !selectedRank }"
          @click="clickMakeInvitation"
        >
          프로필 수정
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "Profile",
};
</script>

<style scoped>
.main-title {
  font-size: 1.3rem;
  font-weight: 900;
  margin-top: 10%;
}
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

.profile-info {
  position: relative;
  width: 85%;
  left: 7.5%;
}
.new-button {
  background-color: #fea59c;
  color: #f8f8f8;
  /* width: 100%; */
}
</style>
