<template>
  <div>
    <div class="text-center mt-5">
      <h5 class="main-title text-center color-pink">Profile</h5>

      <div class="profile-image-outline">
        <img class="profile-image" src="@/assets/test.jpg" />        
      </div>

      <div class="profile-info">
        <h4 class="d-flex align-items-center">
          <span class="badge badge-pill bg-pink mr-3" >Name</span>
          <template>
          <v-text-field class ="text-info" 
            label="my name is"
            solo
            readonly
            hide-details                     
          ></v-text-field>        
          </template>
        </h4>
        <h4 class="d-flex align-items-center">
          <span class="badge badge-pill bg-pink mr-2" >e-mail</span>
          <template>
          <v-text-field class ="text-info" width="40%"
            label="dlrmsdn135@naver.com"
            solo
            readonly
            hide-details                     
          ></v-text-field>        
          </template>
        </h4>
      </div>

      <br><br>
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
  overflow: hidden;
}
.profile-image {
  margin-top: -1px;
  margin-left: -1px;
  width: 70vw;
  border-radius: 50%;
}

.profile-info {
  position: relative;
  width: 90%;
  left: 3%;
}

.new-button {
  background-color: #fea59c;
  color: #f8f8f8;
  /* width: 100%; */
}
</style>
