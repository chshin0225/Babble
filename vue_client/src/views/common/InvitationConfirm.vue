<template>
  <div class="d-flex flex-column justify-content-center align-items-center">
    <hr>
    <div class="d-flex jusitfy-content-center align-items-center">
      <img v-if="invitationData.baby.profile_image" src="invitationData.baby.profile_image" style="width:30vw; height:30vw; border-radius:50%; border:1px solid #888888;">
      <img v-else src="@/assets/babble_logo.png" style="width:30vw; height:30vw; border-radius:50%; border:1px solid #888888;">
    </div>
    <hr>
    <div class="text-center mt-3">
      <p>안녕하세요 <strong>{{ myaccount.name }}</strong>님!</p>
      <p>여기는 <strong>{{ invitationData.baby.baby_name }}</strong>의 Babble Box 입니다.</p>
      <p> 
        <strong>{{ invitationData.baby.baby_name }}</strong>의 
        <strong>{{ invitationData.rank.rank_name }}</strong>로 초대되신 걸 축하드려요 :)
      </p>
    </div>
    <hr>
    <div>
      <div class="">
        아기와의 관계를 입력해 주세요.
      </div>
      <div class="">
        <input 
          v-model="relationship_name" 
          v-bind:class="{errorText: error, complete: !error && relationship_name}"
          class="inputs"
          id="relationship_name" 
          type="text"
          placeholder="관계" 
          required
        />
        <label for="relationship_name"></label>
        <div class="error-text ml-2" v-if="error">{{error}}</div>
      </div>
      <div class="mt-5">
        <button class="btn new-button" :class="{disabled: !isSubmit}" @click="clickEnroll">아기를 등록합니다.</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'InvitationConfirm',
  data() {
    return {
      relationship_name: "",
      error: false,
      isSubmit: false,
    }
  },
  computed: {
    ...mapState(['myaccount', 'invitationData', 'invitationToken'])
  },
  watch: {
    relationship_name() {
      this.checkrelationship_nameForm();
    }
  },
  methods: {
    ...mapActions(['verifyInvitation', 'findInvitationData']),
    checkrelationship_nameForm() {
      if ( this.relationship_name.length > 0) {
        this.error = false;
        this.isSubmit = true;
      }
      else {
        this.error = "아기와의 관계를 입력해 주세요."
        this.isSubmit = false;
      }
    },
    clickEnroll() {
      if (this.isSubmit){
        var enrollData = {
          relationship_name: this.relationship_name
        }
        this.verifyInvitation(enrollData)
      }
    },
  },
  created() {
    this.findInvitationData()
  }
}
</script>

<style scoped>
  .inputs {
    border-style: none;
    border-bottom: 1px solid #aea4a3;
    background-color: transparent;
    width: 100%;
    padding: 10px;
    padding-left: 10px;
    padding-right: 10px;
    /*margin-top: 20px;*/
  }

  .new-button{
    background-color: #FEA59C;
    color: #F8F8F8;
    width: 100%;
  }

  .inputs:focus {
    border-style: none;
    border-bottom: 2px solid #D6CBBD;
    outline-style: none;
  }

  .errorText, .errorText:focus {
    border-bottom: 2px solid rgb(250, 25, 59, 0.7); 
  }

  .error-text {
    color: rgb(250, 25, 59, 0.7);
    text-align: left;
    padding-left: 0px;
  }

  
  .new-button:hover {
    background-color: #A05E58;
    color: #F8F8F8;
  }

  .new-button .disabled, .new-button .disabled:hover {
    background-color: rgb(176, 127, 122, 0.25);
    color: #F8F8F8;
    cursor: inherit;
  }
</style>