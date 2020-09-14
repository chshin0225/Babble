<template>
  <div>
    <div id="app">
      <Burger></Burger>
      <Sidebar>
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
