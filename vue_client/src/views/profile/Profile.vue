<template>
  <div>
    <div class="text-center mt-5" v-if="myaccount">
      <h3 class="main-title text-center color-pink mb-3">Profile</h3>
      <div style="width:100%; text-align:center; padding: 0 10vw;" >
        <img v-if="myaccount.profile_image" style="width:50vw; height:50vw; border-radius:50%; border: 5px solid #fea59c;"  :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + myaccount.profile_image + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" />
        <img v-else style="width:50vw; height:50vw; border-radius:50%; border: 5px solid #fea59c;" src="@/assets/babble_logo.png" />        
      </div>

      <div class="profile-info mt-10">
        <div class="d-flex align-items-center mb-3">
          <span class="badge badge-pill badge-pink mr-2" >Name</span>          
          <h5>{{ myaccount.name }}</h5>
        </div>
        <div class="d-flex align-items-center">
          <span class="badge badge-pill badge-pink mr-2" >Email</span>
          <h5>{{ myaccount.email }}</h5>
        </div>
      </div>

      <br><br>
      <router-link :to="{ name: 'ProfileInfoEdit' }" class="view pointer">
        <button class="btn new-button">
          프로필 수정하러 가기
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
  /* font-size: 1.3rem; */
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

.profile-image{
  width:70vw; height:70vw; border-radius:50%; border: 5px solid #fea59c;
}

.profile-info {
  position: relative;
  width: 90%;
  left: 3%;
}

.badge-pink {
  border: 1px solid #FEA59C;
  color: #FEA59C;
  font-size: 1.2rem;
}

h5 {
  font-weight: 400;
  margin: 0;
}

.new-button {
  background-color: #FEA59C;
  color: #f8f8f8;
}


</style>
