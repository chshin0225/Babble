<template>
  <div class="d-flex flex-column justify-content-center align-items-center">
    <hr>
    <div class="d-flex jusitfy-content-center align-items-center">
      <img :src="profileImg" style="width:30vw; height:30vw; border-radius:50%; border:1px solid #888888;">
    </div>
    <hr>
    <div class="text-center mt-3">
      <p><strong>{{ currentBaby.baby_name }}</strong> 의 Babble Box를 공유해보세요!</p>
    </div>
    <hr>
    <div class="text-center" v-if="invitationURL">
      <small class="border p-2 rounded border-dark"><strong>{{ invitationURL }}</strong></small>
      <div class="mt-5 d-flex justify-content-center align-items-center">
        <button class="btn new-button mr-5" @click="clickCopyURL">초대 URL 복사하기</button>
        <button class="ml-5" @click="clickKakaoShare">
          <img width="40vw" src="https://developers.kakao.com/assets/img/about/logos/kakaolink/kakaolink_btn_medium.png"/>
        </button>
      </div>
    </div>
    <div v-else>
      <div>
        <p>초대할 사용자의 권한을 설정해주세요</p>
      </div>
      <v-combobox
        v-model="selectedRank"
        :items="ranks"
        label="권한"
        outlined
        dense
      ></v-combobox>
      <div class="mt-5 text-center">
        <button class="btn new-button" :class="{disabled: !selectedRank}" @click="clickMakeInvitation">공유 URL 생성</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapMutations, mapState } from 'vuex'
import Swal from 'sweetalert2'

export default {
  name: 'InvitationCreate',
  data() {
    return {
      selectedRank: null,
      ranks: [
        '공동 양육자',
        '손님'
      ]
    }
  },
  computed: {
    ...mapState(['myaccount', 'currentBaby', 'invitationURL']),
    profileImg() {
      if (this.currentBaby.profile_image) {
        return 'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + this.currentBaby.profile_image + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'
      } else {
        return "https://user-images.githubusercontent.com/57381062/94547705-9a283200-028a-11eb-857f-c2624de6cc21.png"
      }
    },
    rankId() {
      if (this.selectedRank === '공동 양육자') {
        return 2
      } else {
        return 3
      }
    }
  },
  methods: {
    ...mapActions(['makeInvitation']),
    ...mapMutations(['SET_INVITATION_URL']),
    clickMakeInvitation() {
      var invitationInfo = {
        rank: this.rankId
      }
      this.makeInvitation(invitationInfo)
    },
    clickKakaoShare() {
      window.Kakao.Link.sendDefault({
        objectType: 'feed',
        content: {
          title: this.currentBaby.baby_name + '의 Babble Box에 초대 받으셨습니다!',
          description: '링크로 들어와 아이를 등록을 해주세요 :)',
          imageUrl: this.profileImg,
          link: {
            mobileWebUrl: this.invitationURL,
            webUrl: this.invitationURL,
          },
        }
      })
    },
    clickCopyURL() {
      const copyText = document.createElement("input");
      copyText.value = this.invitationURL
      document.body.appendChild(copyText)
      
      copyText.select();
      document.execCommand("copy");
      document.body.removeChild(copyText)
      Swal.fire({
          icon: 'success',
          text: '주소가 복사되었습니다'
        })
    }
  },
  beforeRouteLeave(to, from, next) {
    this.SET_INVITATION_URL(null)
    next()
  }
}

</script>

<style scoped>
  .new-button{
    background-color: #FEA59C;
    color: #F8F8F8;
    /* width: 100%; */
  }

</style>