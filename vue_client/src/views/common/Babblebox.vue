<template>
  <div v-if="babbleboxes">
    <div class="scallop-down"></div>
    <div class="text-center">
      <h3 class="color-pink font-weight-bold">Babble Box</h3>
      <p>현재 <span class="color-blue font-weight-bold" v-if="myaccount">{{ myaccount.name }}</span>님께서 예뻐해주시는 아기입니다.</p>
    </div>
    <!-- <div class="scallop-down"></div> -->
    <div class="babbleboxes w-75 mt-3" v-for="babblebox in babbleboxes" :key="`babblebox-${babblebox.id}`">
      <div class="babblebox d-flex justify-content-between my-3">
        <div class="babblebox-info d-flex">
          <div class="profile mr-3">
            <img src="http://bit.do/babbleprofile">
          </div>
          <div class="babble-box">
            <p>{{ babblebox.baby.baby_name }}</p>
            <p>D + {{ babblebox.baby.birth | countDays(babblebox.baby.birth) }}</p>
          </div>
        </div>
        <div class="babblebox-enter d-flex align-items-center pointer" @click="clickBabbleBox(babblebox.baby.id)">
          <i class="fas fa-sign-in-alt"></i>
        </div>
      </div>
    </div>
    <div class="babbleboxes w-75 mt-3" >
      <div class="babblebox d-flex justify-content-between my-3">
        <div class="babblebox-info d-flex">
          <div class="profile mr-3">
            <img src="http://bit.do/babbleprofile">
          </div>
          <div class="babble-box d-flex align-items-center pointer" @click="clickCreate()">
            <p>아기 추가하기</p>
          </div>
        </div>
        <div class="babblebox-enter d-flex align-items-center pointer" @click="clickCreate()">
          <i class="fas fa-plus-circle"></i>
        </div>
      </div>
    </div>
    <div style="height: 100px"></div>

  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'Babblebox',
  data() {
    return {
      accessData: {
        baby: null,
      }
    }
  },
  computed: {
    ...mapState([ 'myaccount', 'babbleboxes']),
  },
  filters: {
    countDays(date) {
      var d1 = new Date() 
      var d2 = new Date(date)
      var days2 = Math.floor(Math.abs(d1-d2)/(8.64e+7))
      return days2

    }
  },
  methods: {
    ...mapActions(['findBaby', 'findMyAccount', 'fetchBabbleBox', 'accessBabbleBox']),
    clickCreate() {
      this.$router.push({ name: 'HowToRegisterBaby' })
    },
    clickBabbleBox(babbleboxId) {
      var babblebox = new Object()
      babblebox.baby = babbleboxId
      this.accessBabbleBox(babblebox)
    }
  },
  mounted() {
    this.findMyAccount()
    this.fetchBabbleBox()
  }
}
</script>

<style scoped>

p {
  margin: 0;
}

.profile img {
  max-width: 50px;
  height: auto;
  border-radius: 50%;
}

.babbleboxes {
  margin-left: auto;
  margin-right: auto;
}

.babblebox {
  border: 1px solid #FEA59C;
  border-radius: 50px;
  padding: 10px 30px 10px 30px;
}

.scallop-down{
  height:40px;
  /* margin-left: auto;
  margin-right: auto; */
  width:100%;
  background: -webkit-gradient(radial, 50% 0, 18, 50% 0, 31, from(#9BC7FF), color-stop(0.49, #9BC7FF), color-stop(0.51, #fff), to(white));
  -webkit-background-size: 49px 100%;
}

</style>