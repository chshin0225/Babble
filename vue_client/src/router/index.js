import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store";

// Photos
import PhotoMain from "@/views/photos/PhotoMain";
import PhotoList from "@/views/photos/PhotoList";
import PhotoCreate from "@/views/photos/PhotoCreate";
import PhotoDetail from "@/views/photos/PhotoDetail";
import PhotoUpdate from "@/views/photos/PhotoUpdate";
import PhotoSearch from "@/views/photos/PhotoSearch";
import PhotoSearchResult from "@/views/photos/PhotoSearchResult";
import AlbumLibrary from "@/views/photos/AlbumLibrary";
import AlbumCreate from "@/views/photos/AlbumCreate";
import AlbumDetail from "@/views/photos/AlbumDetail";
import AlbumEdit from "@/views/photos/AlbumEdit";
import AlbumInfoEdit from "@/views/photos/AlbumInfoEdit";
import TagSelect from "@/views/photos/TagSelect";

// Diary
import Diary from "@/views/diaries/Diary";
import DiaryPhoto from "@/views/diaries/DiaryPhoto";
import DiaryCalendar from "@/views/diaries/DiaryCalendar";
import DiaryTimeline from "@/views/diaries/DiaryTimeline";
import DiaryCreate from "@/views/diaries/DiaryCreate";
import DiaryUpdate from "@/views/diaries/DiaryUpdate";
import DiaryDetail from "@/views/diaries/DiaryDetail";

// Babble Box
import Babblebox from "@/views/common/Babblebox";
import Settings from "@/views/common/Settings";
import BabySetting from "@/views/common/BabySetting";
import RankSetting from "@/views/common/RankSetting";
import RankSettingUser from "@/views/common/RankSettingUser";
import RankSettingGroup from "@/views/common/RankSettingGroup";

// Authentication
import Login from "@/views/accounts/Login";
import Signup from "@/views/accounts/Signup";
import SignupKakao from "@/views/accounts/SignupKakao";
import PasswordFind from "@/views/accounts/PasswordFind";
import PasswordFindEmail from "@/views/accounts/PasswordFindEmail";
import HowToRegisterBaby from "@/views/accounts/HowToRegisterBaby";
import RegisterBaby from "@/views/accounts/RegisterBaby";
import RegisterBabyRelate from "@/views/accounts/RegisterBabyRelate";
import RegisterInviteLink from "@/views/accounts/RegisterInviteLink";

// Profile
import Profile from "@/views/profile/Profile";
import ProfileInfoEdit from "@/views/profile/ProfileInfoEdit";

// Measurement
import MeasurementMain from "@/views/measurements/MeasurementMain"
import WeightMeasurement from "@/views/measurements/WeightMeasurement"
import HeightMeasurement from "@/views/measurements/HeightMeasurement"
import HeadMeasurement from "@/views/measurements/HeadMeasurement"

import InvitationConfirm from "@/views/common/InvitationConfirm";
import InvitationCreate from "@/views/common/InvitationCreate";

Vue.use(VueRouter);

const routes = [
  // photos
  {
    path: "/photo",
    name: "PhotoMain",
    component: PhotoMain,
    children: [
      {
        path: "",
        component: PhotoList,
        name: "PhotoList",
      },
      {
        path: "library",
        component: AlbumLibrary,
        name: "AlbumLibrary",
      },
      {
        path: "search",
        component: PhotoSearch,
        name: "PhotoSearch",
      },
    ],
  },
  {
    path: "/photo/search/:keyword",
    component: PhotoSearchResult,
    name: "PhotoSearchResult"
  },
  {
    path: "/photo/create",
    component: PhotoCreate,
    name: "PhotoCreate",
  },
  {
    path: "/photo/:photoId",
    component: PhotoDetail,
    name: "PhotoDetail",
  },
  {
    path: "/photo/:photoId/update",
    component: PhotoUpdate,
    name: "PhotoUpdate",
  },
  {
    path: "/photo/tagselect",
    component: TagSelect,
    name: "TagSelect",
  },
  {
    path: "/photo/library/create",
    component: AlbumCreate,
    name: "AlbumCreate",
  },
  {
    path: "/photo/library/:albumId",
    component: AlbumDetail,
    name: "AlbumDetail",
  },
  {
    path: "/photo/library/:albumId/edit",
    component: AlbumEdit,
    name: "AlbumEdit",
  },
  {
    path: "/photo/library/:albumId/info",
    component: AlbumInfoEdit,
    name: "AlbumInfoEdit",
  },

  // Authentication
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/signup/kakao",
    name: "SignupKakao",
    component: SignupKakao,
  },
  {
    path: "/pwfind",
    name: "PasswordFind",
    component: PasswordFind,
  },
  {
    path: "/pwfindemail",
    name: "PasswordFindEmail",
    component: PasswordFindEmail,
  },
  {
    path: "/howtoregisterbaby",
    name: "HowToRegisterBaby",
    component: HowToRegisterBaby,
  },
  {
    path: "/registerbaby",
    name: "RegisterBaby",
    component: RegisterBaby,
  },
  {
    path: "/registerbabyrelate",
    name: "RegisterBabyRelate",
    component: RegisterBabyRelate,
  },
  {
    path: "/registerinvitelink",
    name: "RegisterInviteLink",
    component: RegisterInviteLink,
  },

  // Babble Box
  {
    path: "/babblebox",
    name: "Babblebox",
    component: Babblebox,
  },
  {
    path: "/settings",
    name: "Settings",
    component: Settings,
  },
  {
    path: "/babysetting",
    component: BabySetting,
    name: "BabySetting",
  },
  {
    path: "/invitation/:token",
    component: InvitationConfirm,
    name: "InvitationConfirm",
  },
  {
    path: "/invitation/",
    component: InvitationCreate,
    name: "InvitationCreate",
  },
  {
    path: "/ranksetting",
    name: "RankSetting",
    component: RankSetting,
    children: [
      {
        path: "",
        component: RankSettingUser,
        name: "RankSettingUser",
      },
      {
        path: "group",
        name: "RankSettingGroup",
        component: RankSettingGroup,
      },
    ],
  },
  // Diary
  {
    path: "/diary",
    name: "Diary",
    component: Diary,
    children: [
      {
        path: "",
        component: DiaryPhoto,
        name: "DiaryPhoto",
      },
      {
        path: "calendar",
        component: DiaryCalendar,
        name: "DiaryCalendar",
      },
      {
        path: "timeline",
        component: DiaryTimeline,
        name: "DiaryTimeline",
      },
    ],
  },
  {
    path: "/diary/create",
    name: "DiaryCreate",
    component: DiaryCreate,
  },
  {
    path: "/diary/:diaryId/update",
    name: "DiaryUpdate",
    component: DiaryUpdate,
  },
  {
    path: "/diary/:diaryId",
    name: "DiaryDetail",
    component: DiaryDetail,
  },
  // Profile
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
  },
  {
    path: "/profile/infoedit",
    name: "ProfileInfoEdit",
    component: ProfileInfoEdit,
  },
  // Measurement
  {
    path: "/measurement",
    name: 'MeasurementMain',
    component: MeasurementMain,
    children: [
      {
        path: "/weight",
        name: 'WeightMeasurement',
        component: WeightMeasurement,
      },
      {
        path: "/height",
        name: 'HeightMeasurement',
        component: HeightMeasurement,
      },
      {
        path: "/head",
        name: 'HeadMeasurement',
        component: HeadMeasurement,
      },
    ]
  },
  
  
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  }
})

router.beforeEach((to, from, next) => {
  const publicPages = [
    "Login",
    "Signup",
    "SignupKakao",
    "PasswordFind",
    "PasswordFindEmail",
  ]; // Login 안해도 됨
  const authPages = [
    "Login",
    "Signup",
    "SignupKakao",
    "PasswordFind",
    "PasswordFindEmail",
  ]; // Login 되어있으면 안됨
  // const pubicPages = ['Login', 'Signup'] // Login 안해도 됨
  // const authPages = ['Login', 'Signup'] // Login 되어있으면 안됨
  const authRequired = !publicPages.includes(to.name); // 로그인 해야하는 페이지면 true 반환
  const unauthRequired = authPages.includes(to.name);
  const isLoggedIn = Vue.$cookies.isKey("auth-token");

  if (unauthRequired && isLoggedIn) {
    next({ name: "PhotoList" });
  }

  if (authRequired && !isLoggedIn) {
    if (to.name === "InvitationConfirm") {
      store.commit("SET_INVITATION_TOKEN", to.params.token);
    }
    next({ name: "Login" });
  } else {
    if (to.name === "InvitationConfirm") {
      store.commit("SET_INVITATION_TOKEN", to.params.token);
    }
    next();
  }
});

export default router;
