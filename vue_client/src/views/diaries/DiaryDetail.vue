<template>
  <div class="p-3">
    <div class="diary-top d-flex justify-content-between my-3">
      <div class="diary-date text-muted">
        <p>2020년 7월 8일 14:28</p>
      </div>
      <div class="diary-writer">
        <p>엄마 작성</p>
      </div>
    </div>
    
    <div class="diary-title">
      <h5>하..너무 귀엽다!!</h5>
    </div>
    <div class="diary-content p-2">
      <p class="text">
        세상에서 가장 귀여운 우리 아롱이... 오늘은 밥 많이 먹었다!
        무럭무럭 잘 크고 있는 것 같아서 엄마는 행복해.
        우리 애기가 밥 많이 먹는 모습도 귀엽고,
        오물오물하는 볼도 귀엽고,
        전부 다 귀여워! 
        딱 이대로만 예쁘게 커주길 바래.
      </p>
      <img src="https://t1.daumcdn.net/tvpot/thumb/s8b90Dh8u7sDgMlccgchys3/thumb.png?ts=1541536764">
    </div>
    <div class="scallop-down"></div>
    <div class="mt-3 growth-title row no-gutters">
      <div class="col-3 text-center">
        <img width="50px" src="http://clipart-library.com/images/yckA5Azei.png" />
      </div>
      <div class="col-9">
        <p class="growth">성장 기록</p>
        <p>무게 9.2Kg 🞄 키 67cm 🞄 머리둘레 20cm</p>
      </div>
      
    </div>
    <div class="scallop-up"></div>
    <div class="comment mb-5 mt-3">
      <h5 class="comment-title mb-3">댓글</h5>
      <div>
        <div class="d-flex justify-content-between">
          <p class="comment-username">아빠</p>
          <p class="comment-time">3시간 전</p>
        </div>
        <div>너무 귀엽다 우리 아롱이</div>
      </div>
      <hr>
      <div>
        <div class="d-flex justify-content-between">
          <p class="comment-username">할머니</p>
          <p class="comment-time">어제</p>
        </div>
        <div>예쁘게 크렴</div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'DiaryDetail',
}
</script>

<style scoped lang="scss">
.diary-top {
  .diary-date {
    p {
      margin: 0;
    }
  }
  .diary-writer {
    p {
      margin: 0;
    }
  }
}

.diary-title {
  h5 {
    margin: 0.5rem;
    border-bottom: 1px solid black;
  }
}
.diary-content {
  p {
  white-space: pre-wrap;
  word-wrap: break-word;
  }

  img {
    width: 82vw;  
  }
}
.growth {
  font-weight: 900;
  font-size: 1.5rem;
}


.scallop-up{
  height:40px;
  width:100%;
  background: -webkit-gradient(radial, 50% 100%, 10, 50% 100%, 40, from(#9BC7FF), color-stop(0.49, #9BC7FF), color-stop(0.51, #fff), to(white));
-webkit-background-size: 49px 100%;
}


.scallop-down{
  height:40px;
  /* margin-left: auto;
  margin-right: auto; */
  width:100%;
  background: -webkit-gradient(radial, 50% 0, 18, 50% 0, 31, from(#9BC7FF), color-stop(0.49, #9BC7FF), color-stop(0.51, #fff), to(white));
  -webkit-background-size: 49px 100%;
}

.comment-title {
  font-weight: 900;
  color: #FEA59C;
}

.comment-username {
  font-weight: 600;
}

.comment-time {
  color: #979797;
}

</style>