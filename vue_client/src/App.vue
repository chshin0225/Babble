<template>
  <div>
    <div id="app">
      <nav class="nav">
        <Burger class="left-align d-flex align-items-center"></Burger>
        <div class="logo-sect center-align d-flex align-items-center">
          <span><img src="https://user-images.githubusercontent.com/25967949/93062400-d9ae2600-f6af-11ea-948c-219574892c76.png"></span>
          <span class="logo-title">Babble</span>
        </div>
      </nav>
      <Sidebar style="clear:both;">
        <div class="sidebar-panel-nav">
          <!-- 현재 babble box info -->
          <div class="upper bg-pink">
            <div class="profile float-left mr-3">
              <img src="http://bit.do/babbleprofile">
            </div>
            <div class="babble-box">
              <p>아롱이 (아기 이름)</p>
              <p>D + 73</p>
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
      </Sidebar>
      
      <router-view></router-view>
      <!-- footer -->
      <div class="footer row no-gutters">
        <div class="col-4 color-gray" :class="{'color-pink' : isAlbum()}">
          <p><i class="fas fa-images"></i></p>
          <p>Album</p>
        </div>
        <div class="col-4 color-gray" :class="{'color-pink' : isDiary()}">
          <p><i class="fas fa-book"></i></p>
          <p>Diary</p>
        </div>
        <div class="col-4 color-gray" :class="{'color-pink' : isProfile()}">
          <p><i class="fas fa-user"></i></p>
          <p>Profile</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
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
    }
  },
  methods: {
    // sidebar
    toggle() {
      this.isBurgerActive = !this.isBurgerActive
    },
    // navbar
    isAlbum() {
      console.log(this.$route.name)
      if (this.$route.name === 'Album') {
        return true
      } else {
        return false
      }
    },
    isDiary() {
      if (this.$route.name === 'Diary') {
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
    }
  }


};
</script>

<style scoped>
/* top-navbar */
.nav {
  -webkit-box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
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

/* sidebar */
.upper {
  padding: 20px;
}

.menu-container {
  padding: 40px;
  list-style: none;
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

.profile img{
  max-width: 50px;
  height: auto;
  border-radius: 50%;
}

/*  fotter */
.footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: ;
  color: black;
  text-align: center;
  -webkit-box-shadow: 0px -4px 5px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px -4px 5px 0px rgba(0,0,0,0.1);
  box-shadow: 0px -4px 5px 0px rgba(0,0,0,0.1);
}

p {
  margin: 0;
}

</style>
