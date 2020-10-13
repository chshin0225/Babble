<template>

  <div>
    <div style="margin-top:15vh; width:100%; text-align:center">
      <img 
        v-if="currentBaby.profile_image"
        :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + currentBaby.profile_image + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" 
        style="width:50vw; height:50vw; border-radius:50%; border:5px solid #fea59c;">

      <img v-else style="width:50vw; height:50vw; border-radius:50%; border: 5px solid #fea59c;" src="@/assets/baby.png" />
    </div>
    <div class="mt-2" style="width:100%; text-align:center; font-size:6vw;">별이</div>

    <div class="buttons mt-5">
      <button class="btn setting-button" @click="clickBabySetting">아기 설정</button>
    </div>
    <div class="buttons mt-5">
      <button class="btn setting-button" @click="clickRankSetting">그룹 설정</button>
    </div>
    <div class="buttons mt-5">
      <button class="btn setting-button" @click="clickInvitationCreate">초대 링크 생성</button>
    </div>
  </div>
</template>

<script>

import { mapState } from 'vuex'

export default {
  name: 'Settings',
  
  computed: {
    ...mapState(['myaccount', 'currentBaby']),
  },
  methods:{
    clickBabySetting(){
      this.$router.push({ name: 'BabySetting'})
    },
    clickGroupSetting(){
      this.$router.push({ name: 'GroupSetting'})
    },
    clickInvitationCreate() {
      this.$router.push({ name: 'InvitationCreate' })
    },
    clickRankSetting(){
      this.$router.push({ name: 'RankSetting'})
    }
  }
}
</script>

<style scoped>
.menu:link, .menu:active, .menu:visited {
  color: black;
  text-decoration: none;
}

.menu:hover {
  text-decoration:none;
}

.row .router-link-exact-active {
  color: #FEA59C;
  border-bottom: 3px solid #FEA59C;
}

.buttons{
  text-align:center;
}

.setting-button{
  background-color: #FEA59C;
  color: #F8F8F8;
  width: 80%;
}


</style>