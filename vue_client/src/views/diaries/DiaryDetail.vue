<template>
  <div class="p-3" v-if="diary" data-app>
    <div class="diary-top d-flex justify-content-between my-3">
      <div class="diary-date text-muted">
        <p>{{diary.diary.diary_date}}</p>
      </div>
      <div class="diary-writer">
        <span class="mr-3">{{diary.relationship.relationship_name}} 작성</span>
        <button class="btn btn-pink" @click="sheet = !sheet">:</button>
        <v-bottom-sheet v-model="sheet">
          <v-sheet class="text-center" height="27vh">
            <div class="py-3">
              <div class="pointer diary-option mb-3" @click="clickShare">일기 공유</div>
              <hr>
              <div class="pointer diary-option mb-3" @click="clickEdit"> 일기 수정</div>
              <hr>
              <div class="pointer diary-option" @click="clickDelete"> 일기 삭제</div>
            </div>
          </v-sheet>
        </v-bottom-sheet>
        
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
    <div class="measurement" v-if="diary.measurement">
      <div class="scallop-down"></div>
      <div class="mt-3 growth-title row no-gutters">
        <div class="col-3 text-center">
          <!-- <img width="50px" src="http://clipart-library.com/images/yckA5Azei.png" />
          <img width="50px" src="../../assets/giraffe.png" /> -->
          <img class="img-fluid" src="@/assets/giraffe.png" />
        </div>
        <div class="col-9">
          <p class="growth d-flex justify-content-center">성장 기록</p>
          <div class="d-flex justify-content-center text-center">
            <p class="growth-record mr-3 mb-3" v-if="diary.measurement.weight">
              <span class="growth-record-title">무게</span><br>{{ diary.measurement.weight }} kg
            </p>
            <p class="growth-record mr-3 mb-3" v-if="diary.measurement.height">
              <span class="growth-record-title">키</span><br> {{ diary.measurement.height }} cm
            </p>
            <p class="growth-record" v-if="diary.measurement.head_size">
              <span class="growth-record-title">머리둘레</span><br>{{ diary.measurement.head_size }} cm
            </p>          
          </div>
        </div>
      </div>
      <div class="scallop-up"></div>
    </div>
    
    <div class="comment mb-5 mt-3">
      <h5 class="comment-title mb-3">댓글</h5>
      <!-- 댓글 작성 -->
      <div class="input-group row no-gutters comment-create" style="height:65px;">
        <div class="input-group row no-gutters comment-create" style="height:65px;">
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
        
      </div>
      <!-- 댓글 리스트 -->
      <div class="comment-list">
        <div v-for="comment in comments" :key="`comment_${comment.id}`">
          <div>
            <div class="d-flex justify-content-between">
              <p class="comment-username">{{comment.user}}</p>
              <div class="d-flex">
                <p class="comment-time">{{comment.modify_date |  moment("from", "now")}}</p>
                <div class="dropdown" v-if="comment.user === myaccount.id">
                  <div class="btn-group dropleft">
                    <button type="button" class="btn btn-pink dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"></button>
                    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                      <p class="dropdown-item pointer" @click="clickInitUpdateComment(comment)">댓글 수정</p>
                      <p class="dropdown-item pointer" @click="clickDeleteComment(commentData, comment.id)">댓글 삭제</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- 댓글 수정 X - 댓글 내용 노출 -->
            <div v-if="comment.id != commentUpdateData.commentId">
              {{ comment.content }}
            </div>
            <!-- 댓글 수정 클릭했을 때 - 댓글 수정란 노출 -->
            <div v-else>
              <div class="input-group row no-gutters comment-create" style="height:65px;">
              <textarea
                class="col-10 textareaSection p-1" 
                @keyup.enter="enterUpdateComment" 
                @input="updateActiveBtn(comment.content)"
                v-model="commentUpdateData.content" 
                type="content" 
                rows="1" 
                autofocus
              ></textarea>
              <button 
                :class="{ 'btn-pink': updateBtnActive, 'pointer': updateBtnActive }"
                class="btn col-2"
                :disabled="!updateBtnActive"
                @click="clickUpdateComment(commentUpdateData)"
              >
                수정
              </button>
              </div>
            </div>
          </div>
          <hr>
        </div>
      </div>
    </div>
    <div style="height: 10vh;"></div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import Swal from 'sweetalert2'

const swal = Swal.mixin({
  customClass: {
    confirmButton: 'btn btn-success mr-2',
    cancelButton: 'btn btn-danger'
  },
  buttonsStyling: false
})

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
      btnActive: false,
      commentUpdateData: {
        diaryId: this.$route.params.diaryId,
        commentId: null,
        content: null,
      },
      updateBtnActive: false,
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
    ...mapState(['myaccount']),
    ...mapState('diaryStore', ['diary', 'comments'])
  },
  methods: {
    ...mapActions('diaryStore', ['findDiary', 'fetchComments', 'createComment', 'deleteComment', 'updateComment', 'deleteDiary']),
    clickShare() {
      const copyText = document.createElement("input");
      copyText.value = `http://j3a310.p.ssafy.io/diary/${this.$route.params.diaryId}`
      document.body.appendChild(copyText)
      
      copyText.select();
      document.execCommand("copy");
      document.body.removeChild(copyText)
      this.sheet = false;
      Swal.fire({
          icon: 'success',
          text: '주소가 복사되었습니다'
        })
      
    },
    clickDelete( ){
      this.sheet = false;
      swal.fire({
        text: "정말 다이어리를 삭제하시겠습니까?",
        showCancelButton: true,
        confirmButtonText: '네',
        cancelButtonText: '아니요',
        icon: "warning",
      })
      .then((result) => {
        if (result.value) {
          this.deleteDiary(this.$route.params.diaryId)
        } 
      });
      
    },
    activeBtn() {
      if (this.commentData.content) {
        this.btnActive = true
      } else {
        this.btnActive = false
      }
    },
    updateActiveBtn(priorContent) {
      if (this.commentUpdateData.content !== priorContent) {
        this.updateBtnActive = true
      } else {
        this.updateBtnActive = false
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
      if (this.commentData.content.length === 1){
        this.commentData.content = null
        this.btnActive = false
        Swal.fire({
          icon: 'error',
          text: '댓글을 작성해주세요.'
        })
      } else {
        this.createComment(this.commentData)
        .then(() => {
          this.commentData.content = null
          this.btnActive = false
        })  
      }
    },
    clickDeleteComment(commentData, commentId){
       swal.fire({
        text: "정말 삭제하시겠습니까?",
        showCancelButton: true,
        confirmButtonText: '네',
        cancelButtonText: '아니요',
        icon: "warning",
      })
      .then((result) => {
        if (result.value) {
          this.deleteComment({ diaryId: commentData.diaryId, commentId: commentId })
        } 
      });
    },
    clickInitUpdateComment(comment) {
      this.commentUpdateData.commentId = comment.id 
      this.commentUpdateData.content = comment.content
    },
    clickUpdateComment(comment) {
      this.updateComment(comment)
      this.commentUpdateData.commentId = null
      this.commentUpdateData.content = null
      this.updateBtnActive = false
    },
    enterUpdateComment() {
      if (this.commentUpdateData.content.length === 1){
        this.commentUpdateData.content = null
        this.updateBtnActive = false
        Swal.fire({
          icon: 'error',
          text: '댓글을 작성해주세요.'
        })
      } else {
        this.updateComment(this.commentUpdateData)
        .then(() => {
          this.commentUpdateData.commentId = null
          this.commentUpdateData.content = null
          this.updateBtnActive = false
        })  
      }
    },
    clickEdit() {
      this.$router.push({ name: 'DiaryUpdate', params: { diaryId: this.$route.params.diaryId }})
    },
  },
  mounted() {
    this.findDiary(this.$route.params.diaryId)
  }

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
    .diary-option {
      font-size: 1.5rem !important;
      // &hover {
      //   color: #FEA59C;
      // }
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
}

.measurement {
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
    width:100%;
    background: -webkit-gradient(radial, 50% 0, 18, 50% 0, 31, from(#9BC7FF), color-stop(0.49, #9BC7FF), color-stop(0.51, #fff), to(white));
    -webkit-background-size: 49px 100%;
  }
  
  .growth-record {
    border: 1px solid #FEA59C;
    border-radius: 10px;
    padding: 5px 10px 5px 10px;

    .growth-record-title {
      color: #FEA59C;
      font-weight: 900;
    }
  }

}




// comment
.comment {
  .comment-title {
    font-weight: 900;
    color: #FEA59C;
  }

  .comment-create {
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
  }
  
  .comment-list {
    .comment-username {
      font-weight: 600;
    }

    .comment-time {
      color: #979797;
    }

    .dropdown {
      .btn {
        margin-left: 5px;
        padding: 1px 3px 1px 3px!important;
      }
      .dropdown-menu {
        padding: 0;
        text-align: center;
        p {
          padding: 3px 0 3px 0;
          margin: 0;
        }
      }
    }
  }
}

</style>

<style scoped>
.diary-content >>> img {
  max-width: 100%;
}
</style>