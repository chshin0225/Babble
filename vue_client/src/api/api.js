export default {
    URL: 'http://j3a310.p.ssafy.io:8000',
    // URL: 'http://127.0.0.1:8000',
    AIURL: "http://121.125.56.92:50740/tags",
    ROUTES: {
      // accounts
      signup: '/rest-auth/signup/',
      login: '/rest-auth/login/',
      logout: '/rest-auth/logout/',
      password: '/rest-auth/password/',
      groups: '/accounts/groups/',
      babies: '/babies/',
      babblebox: 'mybabblebox',
      myaccount: '/accounts/myinfo/',
      access: '/accounts/access/',
      kakao: '/accounts/login/kakao/',
      social: '/accounts/login/social/',

      // diary
      diaries: '/diaries/',
      comments: '/comments/',
      measurements: 'measurements/',
      photo: 'photo/',
      
      // photos
      photos: '/photos/',
      tags: '/photos/tags/',
      searchPhoto: '/photos/search/'
    }
  }
  