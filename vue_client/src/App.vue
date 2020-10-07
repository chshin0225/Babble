<template>
  <v-app>
    <div>
      <div class="nav" v-if="routes.indexOf(this.$route.name) === -1">
        <Burger class="left-align d-flex align-items-center"></Burger>
        <div @click="clickLogo" class="logo-sect center-align d-flex align-items-center pointer" >
          <span>
            <img src="@/assets/babble_logo.png" />
          </span>
          <span class="logo-title color-pink">Babble</span>
        </div>
      </div>
      <nav class="nav2 mt-5 " v-else-if="authToken === null || routes2.indexOf(this.$route.name) !== -1">
        <div class="d-flex justify-content-center">
          <span>
            <img src="@/assets/babble_logo.png" />
          </span>
          <span class="nav2-title color-pink d-flex align-items-center">Babble</span>
        </div>
      </nav>
      
      <Sidebar class="d-flex justify-content-between" style="clear: both; z-index: 100">
        <div class="side d-flex flex-column justify-content-between h-100">
          <div class="sidebar-panel-nav">
            <!-- 현재 babble box info -->
            <div class="upper bg-pink d-flex justify-content-between">
              <div class="d-flex">
                <div class="profile float-left mr-3" v-if="currentBaby">
                  <img v-if="currentBaby.profile_image" :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + currentBaby.profile_image + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'">
                  <img v-else src="@/assets/babble_logo.png" />
                </div>
                <div class="babble-box" v-if="currentBaby">
                  <span>{{ currentBaby.baby_name }}</span><br />
                  <span>D + {{ countDays }}</span>
                </div>
              </div>
              <div class="logout-btn" @click="clickLogout">
                <p class="text-muted pointer">로그아웃</p>
              </div>
            </div>

            <div class="menu-container">
              <li class="list invite pointer" @click="clickInvitationCreate">
                <i class="fas fa-envelope color-pink mr-3"></i> 함께할 사람 초대하기</li>
              <hr />
              <li class="list menu pointer" @click="clickBabySettings">
                  <i class="fas fa-cog mr-3"></i> 아기 설정
              </li>
              <li class="list menu pointer" @click="clickGroupSettings">
                  <i class="fas fa-users-cog mr-3"></i> 그룹 설정
              </li>
              <li class="list menu pointer" @click="clickMeasurements">
                  <i class="fas fa-chart-bar mr-3"></i> 성장 분석 보고서
              </li>
            </div>
          </div>

          <div class="sidebar-bottom">
            <hr />
            <div class="d-flex row no-gutters" v-if="accessLog">
              <div class="other-profile pointer col-4" v-for="baby in accessLog" :key="baby.id" @click="clickOtherBaby(baby.baby)">
                <div class="d-flex justify-content-center">
                  <img v-if="baby.profile_image" :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + baby.profile_image + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'" />
                  <img v-else src="@/assets/babble_logo.png" />
                </div>
                <p class="text-center mt-1">{{ baby.baby_name }}</p>
              </div>
            </div>
            <div class="text-right mt-3">
              <p @click="clickBabblebox" class="color-pink pointer">아이들 더보기</p>
            </div>
            <div class="mb-5"></div>
          </div>
        </div>
      </Sidebar>

      <router-view></router-view>
      <!-- <div style="height:100px"></div> -->
      <!-- footer -->
      <div v-if="this.myaccount">
        <div class="footer row no-gutters bg-pink" v-if="authToken != null && this.myaccount.current_baby != null">
          <div 
            class="col-4 color-gray pointer"
            :class="{ 'color-red': isAlbum() }"
            @click="clickPhoto"
          >
            <p><i class="fas fa-images"></i></p>
            <p>Photo</p>
          </div>
          <div
            class="col-4 color-gray pointer"
            :class="{ 'color-red': isDiary() }"
            @click="clickDiary"
          >
            <p><i class="fas fa-book"></i></p>
            <p>Diary</p>
          </div>
          <div
            class="col-4 color-gray pointer"
            :class="{ 'color-red': isProfile() }"
            @click="clickProfile"
          >
            <p><i class="fas fa-user"></i></p>
            <p>Profile</p>
          </div>
        </div>
      </div>

    </div>
  </v-app>
</template>

<script>
// import { mutations } from '@/store/index.js'
// import moment from "moment"
import { mapState, mapActions } from "vuex";
import Sidebar from "./views/common/Sidebar.vue";
import Burger from "./views/common/Burger.vue";
export default {
  name: "App",
  components: {
    Sidebar,
    Burger,
  },
  data() {
    return {
      isBurgerActive: false,
      routes: [
         // Diary
        "DiaryCreate",
        "DiaryUpdate",
        "DiaryDetail",
        // Auth
        "HowToRegisterBaby",
        "Signup",
        "SignupKakao",
        "PasswordFind",
        "PasswordFindEmail",
        "Login",
        "RegisterBaby",
        "HowToRegisterBaby",
        "RegisterBabyRelate",
        "RegisterInviteLink",
        // Photo
        "PhotoDetail",
        "PhotoCreate",
        "PhotoUpdate",
        "AlbumDetail"
      ],
      routes2: [
        "Signup",
        "Login",
        "HowToRegisterBaby",
        "RegisterBaby",
        "PasswordFind",
        "PasswordFindEmail",
        "SignupKakao",
        "RegisterInviteLink",
      ],
      days: null,
    };
  },
  computed: {
    ...mapState(["myaccount", "currentBaby", "authToken"]),
    ...mapState(["myaccount", "currentBaby", "authToken", "invitationToken", "accessLog", "relationship"]),
    countDays() {
      if (this.currentBaby) {
        var d1 = new Date();
        var d2 = new Date(this.currentBaby.birth);
        var days2 = Math.ceil(Math.abs(d1 - d2) / 8.64e7);
        return days2;
      } else {
        return null;
      }
    },
  },
  watch: {
    myaccount() {
      if (this.myaccount) {
        if (!this.myaccount.current_baby) {
          if (!this.invitationToken) {
            this.$router.push({name: 'RegisterBaby'})
          } else {
            this.$router.push({name: 'InvitationConfirm', params: { token: this.invitationToken }})
          }
        } else {
          this.findBaby(this.myaccount.current_baby);
        }
      }
    },
    currentBaby() {
      if (this.currentBaby) {
        this.findRelationship()
        this.fetchAccessLog()
      }
    }
  },
  methods: {
    ...mapActions(["findBaby", "findMyAccount", "logout", "fetchAccessLog", "accessBabbleBox", "findRelationship"]),
    // Logo
    clickLogo() {
      this.$router.push({ name: "PhotoList" });
    },
    // sidebar
    toggle() {
      this.isBurgerActive = !this.isBurgerActive;
    },
    // navbar
    isAlbum() {
      if (
        this.$route.name === "PhotoMain" ||  
        this.$route.name === "PhotoList" || 
        this.$route.name === "AlbumLibrary" || 
        this.$route.name === "PhotoSearch" ||
        this.$route.name === "PhotoCreate" ||
        this.$route.name === "AlbumCreate" ||
        this.$route.name === "AlbumDetail"
      ) {
        return true;
      } else {
        return false;
      }
    },
    isDiary() {
      if (
        this.$route.name === "DiaryPhoto" ||
        this.$route.name === "DiaryTimeline" ||
        this.$route.name === "DiaryCalendar" ||
        this.$route.name === "DiaryCreate" ||
        this.$route.name === "DiaryDetail"
      ) {
        return true;
      } else {
        return false;
      }
    },
    isProfile() {
      if (
        this.$route.name === "Profile" ||
        this.$route.name == "ProfileInfoEdit"
      ) {
        return true;
      } else {
        return false;
      }
    },
    // 페이지 이동
    clickBabblebox() {
      // mutations.toggleNav
      let backdrop = document.querySelector(".sidebar-backdrop");
      backdrop.click();
      this.$router.push({ name: "Babblebox" });
    },
    clickPhoto() {
      this.$router.push({ name: "PhotoList" });
    },
    clickDiary() {
      this.$router.push({ name: "DiaryPhoto" });
    },
    clickProfile() {
      this.$router.push({
        name: "Profile",
        params: { profileId: this.myaccount.id },
      });
    },
    clickLogout() {
      let backdrop = document.querySelector(".sidebar-backdrop");
      backdrop.click();
      this.logout();
    },
    /*clickSettings() {
      let backdrop = document.querySelector(".sidebar-backdrop");
      backdrop.click();
      this.$router.push({ name: "Settings" });
    },*/
    clickBabySettings() {
      let backdrop = document.querySelector(".sidebar-backdrop");
      backdrop.click();
      this.$router.push({ name: "BabySetting" });
    },
    clickGroupSettings() {
      let backdrop = document.querySelector(".sidebar-backdrop");
      backdrop.click();
      this.$router.push({ name: "RankSetting" });
    },
    clickInvitationCreate() {
      let backdrop = document.querySelector(".sidebar-backdrop");
      backdrop.click();
      this.$router.push({ name: "InvitationCreate" });
    },
    clickMeasurements() {
      let backdrop = document.querySelector(".sidebar-backdrop");
      backdrop.click();
      this.$router.push({ name: "WeightMeasurement" })
    },
    clickOtherBaby(babyId) {
      var babblebox = new Object()
      babblebox.baby = babyId
      let backdrop = document.querySelector(".sidebar-backdrop");
      backdrop.click();
      this.accessBabbleBox(babblebox)
    }
  },
  mounted() {
    if (this.authToken) {
      this.findMyAccount();
    }
    this.fetchAccessLog()
  },
};
</script>

<style scoped>
/* top-navbar */
.nav {
  -webkit-box-shadow: 0px 4px 5px 0px rgba(0, 0, 0, 0.1);
  -moz-box-shadow: 0px 4px 5px 0px rgba(0, 0, 0, 0.1);
  box-shadow: 0px 4px 5px 0px rgba(0, 0, 0, 0.1);
  height: 6vh;
  background-color: white;
  position: sticky;
  top: 0;
  z-index: 99;
}

.logo-sect img {
  max-width: 10vw;
  height: auto;
}
/* @import url('https://fonts.googleapis.com/css2?family=Audiowide&display=swap'); */
/* @import url('https://fonts.googleapis.com/css2?family=Titan+One&display=swap'); */
/* @import url('https://fonts.googleapis.com/css2?family=Bowlby+One+SC&display=swap'); */
@import url("https://fonts.googleapis.com/css2?family=Rammetto+One&display=swap");
.logo-sect .logo-title {
  font-size: 6vw;
  font-family: "Rammetto One", cursive;
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
  font-family: "Rammetto One", cursive;
}

.scallop-down{
  height:40px;
  /* width: 75%;
  margin-left: auto;
  margin-right: auto; */
  background: -webkit-gradient(radial, 50% 0, 18, 50% 0, 31, from(#9BC7FF), color-stop(0.49, #9BC7FF), color-stop(0.51, #fff), to(white));
  -webkit-background-size: 49px 100%;
}

/* sidebar */
.side {
  overflow: hidden;
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

.invite > a:link,
.invite > a:active,
.invite > a:visited {
  color: black;
}

.menu > a:link,
.menu > a:active,
.menu > a:visited {
  color: #fea59c !important;
}

.list {
  color: #fea59c !important;
}

.profile img,
.other-profile img {
  /*max-width: 50px;
  height: auto;*/
  width: 50px;
  height : 50px;
  border: 1px solid #fea59c;
  border-radius: 50%;
  /*background-color: white;*/
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
  -webkit-box-shadow: 0px -4px 5px 0px rgba(0, 0, 0, 0.1);
  -moz-box-shadow: 0px -4px 5px 0px rgba(0, 0, 0, 0.1);
  box-shadow: 0px -4px 5px 0px rgba(0, 0, 0, 0.1);
  z-index: 2;
}

p {
  margin: 0;
}

.color-red {
  color: #9bc7ff;
}
</style>