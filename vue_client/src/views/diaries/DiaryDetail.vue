<template>
  <div class="p-3" v-if="diary">
    <div class="diary-top d-flex justify-content-between my-3">
      <div class="diary-date text-muted">
        <p>{{diary.diary.create_date | moment('YYYY-MM-DD HH:mm:ss')}}</p>
      </div>
      <div class="diary-writer">
        <span class="mr-3">{{diary.relationship.relationship_name}} 작성</span>
        <button class="btn btn-pink" @click="sheet = !sheet">:</button>
        <v-app>
            <v-bottom-sheet v-model="sheet">
              <v-sheet class="text-center" height="15vh">
                <div class="py-3">
                  <p class="pointer diary-option mb-1" @click="clickShare">일기 공유</p>
                  <p class="pointer diary-option mb-1"> 일기 수정</p>
                  <p class="pointer diary-option"> 일기 삭제</p>
                </div>
              </v-sheet>
            </v-bottom-sheet>
        </v-app>
        
      </div>
    </div>
    
    <div class="diary-title">
      <h5>{{diary.diary.title}}</h5>
    </div>
    <div class="diary-content p-2">
      <p class="text" v-html="this.diaryContent">
        <!-- {{diary.content}} -->
      </p>
      <!-- <img src="https://t1.daumcdn.net/tvpot/thumb/s8b90Dh8u7sDgMlccgchys3/thumb.png?ts=1541536764"> -->
    </div>
    <div class="scallop-down"></div>
    <div class="mt-3 growth-title row no-gutters">
      <div class="col-3 text-center">
        <!-- <img width="50px" src="http://clipart-library.com/images/yckA5Azei.png" />
        <img width="50px" src="../../assets/giraffe.png" /> -->
        <img width="50px" src="@/assets/giraffe.png" />
      </div>
      <div class="col-9">
        <p class="growth">성장 기록</p>
        <p>무게 9.2Kg 🞄 키 67cm 🞄 머리둘레 20cm</p>
      </div>
      
    </div>
    <div class="scallop-up"></div>
    <div class="comment mb-5 mt-3">
      <h5 class="comment-title mb-3">댓글</h5>
      <!-- 댓글 작성 -->
      <div class="input-group row no-gutters commentSection" style="height:65px;">
        <textarea
          class="col-10 textareaSection p-1" 
          @keyup.enter="enterComment" 
          @input="activeBtn"
          v-model="commentData.content" 
          type="content" 
          placeholder="댓글을 작성하세요 :)" 
          rows="1" 
          autofocus
        ></textarea>
        <button 
          :class="{ 'btn-pink': btnActive, 'pointer': btnActive }"
          class="btn col-2"
          :disabled="!btnActive"
          @click="clickComment"
        >
        작성</button>
      </div>
      <!-- 댓글 리스트 -->
      <div class="commentList">
        <div v-for="comment in comments" :key="`comment_${comment.id}`">
          <div>
            <div class="d-flex justify-content-between">
              <p class="nickname">{{comment.user}}</p>
              <p>{{comment.modify_date | moment('YYYY-MM-DD HH:MM:SS')}}</p>
            </div>
            <div>{{comment.content}}</div>
          </div>
          <hr>
        </div>
      </div>

      <!-- <div>
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
      </div> -->

    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import Swal from 'sweetalert2'

export default {
  name: 'DiaryDetail',
  data() {
    return {
      diaryContent: null,
      sheet: false,
      commentData: {
        content: null,
        diaryId: this.$route.params.diaryId
      },
      btnActive: false
    }
  },
  watch: {
    diary() {
      if (this.diary) {
        this.diaryContent = this.diary.diary.content
        this.fetchComments(this.$route.params.diaryId)
      }
    }
  },
  computed: {
    ...mapState('diaryStore', ['diary', 'comments'])
  },
  methods: {
    ...mapActions('diaryStore', ['findDiary', 'fetchComments', 'createComment']),
    clickShare() {
      const copyText = document.createElement("input");
      copyText.value = `http://j3a310.p.ssafy.io/diary/${this.$route.params.diaryId}`
      document.body.appendChild(copyText)
      
      copyText.select();
      document.execCommand("copy");
      document.body.removeChild(copyText)
      Swal.fire({
          icon: 'success',
          text: '주소가 복사되었습니다'
        })
    },
    activeBtn() {
      if (this.commentData.content) {
        this.btnActive = true
      } else {
        this.btnActive = false
      }
    },
    clickComment() {
      console.log(this.commentData)
      this.createComment(this.commentData)
        .then(() => {
          this.commentData.content = null
          this.btnActive = false
        })  
    },
    enterComment() {
      if (this.commentCreateData.content.length === 1){
        this.commentCreateData.content = null
        this.btnActive = false
        Swal.fire({
          icon: 'error',
          text: '댓글을 작성해주세요.'
        })
      } else {
        let notiData = new Object()
        notiData = {
          to: this.selectedPost.user.id,
          dataId: this.selectedPost.id,
          isRead: false,
          type: "comment"
        }
        this.createNoti(notiData)
        this.createComment(this.commentCreateData)
        .then(() => {
          this.commentCreateData.content = null
          this.btnActive = false
        })  
      }
    },
  },
  mounted() {
    this.findDiary(this.$route.params.diaryId)
  }

}
</script>

<style scoped lang="scss">
.diary-top {
  height: 5vh;
  .diary-date {
    p {
      margin: 0;
    }
  }
  .diary-writer {
    p {
      margin: 0;
    }
    .diary-option:hover {
      color: #FEA59C;
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
    /*width: 82vw;*/ 
    width:100%; 
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

// comment
.comment {
  // textarea
  textarea {
    border: 1px solid #FEA59C;
    &:focus {
      outline-style: none; 
    }
  }
  button {
    border: 1px solid #FEA59C;
    background-color: #979797;
    color: white;
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
}


</style>