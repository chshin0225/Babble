<template>
  <div>
    <div id="app">
      <nav class="nav" v-if="!this.$route.name in this.routes || authToken != null" >
        <Burger class="left-align d-flex align-items-center"></Burger>
        <div @click="clickLogo" class="logo-sect center-align d-flex align-items-center pointer">
          <span>
            <!-- <img src="https://user-images.githubusercontent.com/25967949/93062400-d9ae2600-f6af-11ea-948c-219574892c76.png"> -->
            <img src="@/assets/babble.png" />
          </span>
          <span class="logo-title color-pink">Babble</span>
        </div>
      </nav>
      <nav class="nav2 mt-5 d-flex justify-content-center" v-else-if="this.$route.name!=='DiaryCreate' && this.$route.name!=='HowToRegisterBaby'">
        <span>
          <!-- <img src="https://user-images.githubusercontent.com/25967949/93062400-d9ae2600-f6af-11ea-948c-219574892c76.png"> -->
          <img src="@/assets/babble.png" />
          </span>
        <span class="nav2-title color-pink d-flex align-items-center">Babble</span>
      </nav>
      <Sidebar class=" d-flex justify-content-between" style="clear:both; z-index:100;">
        <div class="side d-flex flex-column justify-content-between h-100">
          <div class="sidebar-panel-nav">
            <!-- 현재 babble box info -->
            <div class="upper bg-pink d-flex justify-content-between">
              <div>
                <div class="profile float-left mr-3">
                  <img src="http://bit.do/babbleprofile">
                </div>
                <span class="babble-box" v-if="currentBaby">
                  <span>{{ currentBaby.baby_name}}</span><br>
                  <span>D + {{ countDays }}</span>
                </span>
              </div>
              <div class="logout-btn" @click="clickLogout">
                <p class="text-muted pointer">로그아웃</p>
              </div>
            </div>
            

            <div class="menu-container">
              <li class="list invite"><a href="#home"><i class="fas fa-envelope color-pink mr-3"></i> 함께할 사람 초대하기</a></li>
              <hr>
              <li class="list menu"><a href="#about"><i class="fas fa-chart-bar mr-3"></i> 성장 분석 보고서</a></li>
              <li class="list menu"><a href="#contact"><i class="fas fa-video mr-3"></i> 성장 동영상</a></li>
              <li class="list menu"><a href="#contact"><i class="fas fa-concierge-bell mr-3"></i> 고객센터</a></li>
              <li class="list menu"><a href="#contact"><i class="fas fa-cog mr-3"></i> 설정</a></li>
            </div>
            
          </div>
          <div class="sidebar-bottom">
            <hr>
            <div class="d-flex justify-content-between">
              <div class="other-profile pointer">
                <img src="http://bit.do/babbleprofile">
                <p class="text-center">사랑이</p>
              </div>
              <div class="other-profile pointer">
                <img src="http://bit.do/babbleprofile">
                <p class="text-center">럭키</p>
              </div>
              <div class="other-profile pointer">
                <img src="http://bit.do/babbleprofile">
                <p class="text-center">다롱이</p>
              </div>
            </div>
            <div class="text-right mt-3">
              <p @click="clickBabblebox" class="color-pink pointer">아이들 더보기</p>
            </div>
            <div class="mb-5">
            </div>
          </div>
        </div>
        
      </Sidebar>
      
      <router-view></router-view>
      <!-- <div style="height:100px"></div> -->
      <!-- footer -->
      <div class="footer row no-gutters bg-pink">
        <div 
        class="col-4 color-gray pointer" 
        :class="{'color-red' : isAlbum()}"
        @click="clickPhoto">
          <p><i class="fas fa-images"></i></p>
          <p>Photo</p>
        </div>
        <div 
          class="col-4 color-gray pointer" 
          :class="{'color-red' : isDiary()}"
          @click="clickDiary">
          <p><i class="fas fa-book"></i></p>
          <p>Diary</p>
        </div>
        <div 
          class="col-4 color-gray pointer"
          :class="{'color-red' : isProfile()}"
          @click="clickProfile">
          <p><i class="fas fa-user"></i></p>
          <p>Profile</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import { mutations } from '@/store/index.js'
// import moment from "moment" 
import { mapState, mapActions } from 'vuex'
import Sidebar from './views/common/Sidebar.vue';
import Burger from './views/common/Burger.vue';
export default {
  name: 'App',
  components: {
    Sidebar,
    Burger
  },
  data(){
    return {
      isBurgerActive: false,
      routes: ['DiaryCreate', 'HowToRegisterBaby', 'Signup', 'Login'],
      days: null,
    }
  },
  computed: {
    ...mapState([ 'myaccount', 'currentBaby',  'authToken']),
    countDays() {
      if (this.currentBaby) {
        var d1 = new Date() 
        var d2 = new Date(this.currentBaby.birth)
        var days2 = Math.floor(Math.abs(d1-d2)/(8.64e+7))
        return days2
      }
      else {
        return null
      }
    },
  },
  watch: {
    myaccount() {
      if (this.myaccount) {
        this.findBaby(this.myaccount.current_baby)
      }
    },
  },

  methods: {
    ...mapActions(['findBaby', 'findMyAccount', 'logout']),
    // Logo
    clickLogo() {
      this.$router.push({name: 'PhotoList'})
    },
    // sidebar
    toggle() {
      this.isBurgerActive = !this.isBurgerActive
    },
    // navbar
    isAlbum() {
      if (this.$route.name === 'PhotoMain' || this.$route.name === 'PhotoList'|| this.$route.name === 'PhotoLibrary' || this.$route.name === 'PhotoSearch' || this.$route.name === 'PhotoCreate'   ) {
        return true
      } else {
        return false
      }
    },
    isDiary() {
      if (this.$route.name === 'DiaryPhoto' || this.$route.name === 'DiaryTimeline' || this.$route.name === 'DiaryCalendar' || this.$route.name === 'DiaryCreate' ) {
        return true
      } else {
        return false
      }
    },
    isProfile() {
      if (this.$route.name === 'Profile') {
        return true
      } else {
        return false
      }
    },
    // 페이지 이동
    clickBabblebox() {
      // mutations.toggleNav
      let backdrop = document.querySelector(".sidebar-backdrop")
      backdrop.click()
      this.$router.push({name: 'Babblebox'})
    },
    clickPhoto() {
      this.$router.push({ name: 'PhotoList'})
    },
    clickDiary() {
      this.$router.push({ name: 'DiaryPhoto'})
    },
    clickProfile() {
      this.$router.push({ name: 'Profile'})
    },
    clickLogout() {
      let backdrop = document.querySelector(".sidebar-backdrop")
      backdrop.click()
      this.logout()
    }
    
  },
  mounted() {
    this.findMyAccount()
  }
};
</script>

<style scoped>
/* top-navbar */
.nav {
  -webkit-box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  height: 6vh;
}

.logo-sect img {
  max-width: 10vw;
  height: auto;
}
/* @import url('https://fonts.googleapis.com/css2?family=Audiowide&display=swap'); */
 /* @import url('https://fonts.googleapis.com/css2?family=Titan+One&display=swap'); */
 /* @import url('https://fonts.googleapis.com/css2?family=Bowlby+One+SC&display=swap'); */
 @import url('https://fonts.googleapis.com/css2?family=Rammetto+One&display=swap');
.logo-sect .logo-title {
  font-size: 6vw;
  font-family: 'Rammetto One', cursive;
}

.left-align {
  float: left;
  width: 33.3333%;
  text-align: left;
}

.center-align {
  float: left;
  width: 33.3333%;
  text-align: center;
}

.nav2 img {
  max-width: 15vw;
  height: auto;
}

.nav2 .nav2-title {
  font-size: 3rem;
  font-weight: 900;
  font-family: 'Rammetto One', cursive;
}

/* sidebar */
.side {
  overflow:hidden;
}

.upper {
  padding: 20px;
}

.logout-btn:hover {
  color: black !important;
}

.menu-container {
 padding: 20px 0 40px 40px;
  list-style: none;
}

.sidebar-bottom {
  padding: 0 20px 40px 40px;
}

.list:hover {
  left: 20px;
  transform-origin: left;
  -webkit-transform: scale(1.2);
  -ms-transform: scale(1.2);
  transform: scale(1.2);
}

a:hover {
  text-decoration: none;
}

.menu {
  margin-bottom: 20px;
}

.invite > a:link, .invite > a:active, .invite > a:visited {
  color: black;
} 

.menu > a:link, .menu > a:active, .menu > a:visited {
  color: #FEA59C !important;
}

.profile img, .other-profile img{
  max-width: 50px;
  height: auto;
  border-radius: 50%;
}




/*  footer */
.footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: white;
  color: black;
  text-align: center;
  -webkit-box-shadow: 0px -4px 5px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px -4px 5px 0px rgba(0,0,0,0.1);
  box-shadow: 0px -4px 5px 0px rgba(0,0,0,0.1);
}

p {
  margin: 0;
}

.color-red {
  color: #9bc7ff;
}

</style>