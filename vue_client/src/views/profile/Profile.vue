<template>
  <div>
    <div class="text-center mt-5">
      <h5 class="main-title text-center color-pink">Profile</h5>

      <div class="profile-image-outline">
        <img v-if="myaccount.profile_image" class="profile-image" :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + myaccount.profile_image + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" />
        <img v-else class="profile-image" src="@/assets/babble_logo.png" />        
      </div>

      <div class="profile-info">
        <h4 class="d-flex align-items-center">
          <span class="badge badge-pill bg-pink mr-3" >Name</span>          
          <v-text-field class ="text-info" 
            label=name    
            v-model="myaccount.name"       
            solo
            readonly
            hide-details                     
          ></v-text-field>        
          
        </h4>
        <h4 class="d-flex align-items-center">
          <span class="badge badge-pill bg-pink mr-2" >e-mail</span>
          <template>
          <v-text-field class ="text-info"
            label="email"
            v-model="myaccount.email"
            solo
            readonly
            hide-details                     
          ></v-text-field>        
          </template>
        </h4>
      </div>

      <br><br>
      <router-link :to="{ name: 'ProfileInfoEdit' }" class="view pointer">
        <button class="btn new-button" >
          프로필 수정
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: "Profile",
  computed: {
    ...mapState([ 'myaccount' ]),
  },
  data(){
    return{      
    }
  },
  methods:{
    ...mapActions("profileStore", ["testAction"]),
    ...mapActions(["findMyAccount"]),    
  },
  created(){
    this.findMyAccount();
  }
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
