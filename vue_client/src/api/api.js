export default {
    URL: 'http://j3a310.p.ssafy.io:8000',
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
      relationship: '/accounts/relationship/',
      access: '/accounts/access/',
      kakao: '/accounts/login/kakao/',
      social: '/accounts/login/social/',
      invitation: '/accounts/invitation/',
      passwordChange: '/rest-auth/password/change/',
      profileChange: '/accounts/profilechange/',
      
      // diary
      diaries: '/diaries/',
      comments: '/comments/',
      measurements: 'measurements/',
      photo: 'photo/',
      
      // photos
      photos: '/photos/',
      tags: '/photos/tags/',
      babbleboxTags: '/photos/babblebox/tags/',
      searchPhoto: '/photos/search/',
      albums: '/photos/albums/',
      emotionTags: '/photos/emotions/',
    }
  }
  