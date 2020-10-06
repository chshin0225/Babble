<template>
  <div class="p-0" v-if="diary" data-app>
    <nav class="d-flex justify-content-between bg-pink w-100 p-2">
      <v-icon 
        class="top-left-icons pointer" 
        @click="clickBack"
        color="white"
      >mdi-arrow-left</v-icon>
      <!-- <div class="d-flex align-items-center ml-3">다른 다이어리 보러가기</div> -->
      <v-spacer></v-spacer>
      <div class="d-flex align-items-center">
        <v-bottom-sheet v-model="sheet">
          <template v-slot:activator="{ on, attrs }">
            <v-icon
              class="top-right-icons"
              color="white"
              v-bind="attrs"
              v-on="on" 
              >mdi-dots-vertical</v-icon>
          </template>
          <v-list>
             <v-list-item @click="clickShare">
              <v-list-item-avatar>
                <v-avatar size="32px" tile>
                <v-icon color="#FEA59C">mdi-share-outline</v-icon>
                </v-avatar>
              </v-list-item-avatar>
              <v-list-item-title>다이어리 공유</v-list-item-title>
            </v-list-item>
            <v-list-item @click="clickEdit">
              <v-list-item-avatar>
                <v-avatar size="32px" tile>
                <v-icon color="#FEA59C">mdi-square-edit-outline</v-icon>
                </v-avatar>
              </v-list-item-avatar>
              <v-list-item-title>다이어리 수정</v-list-item-title>
            </v-list-item>
            <v-list-item @click="clickDelete">
              <v-list-item-avatar>
                <v-avatar size="32px" tile>
                <v-icon color="#FEA59C">mdi-trash-can-outline</v-icon>
                </v-avatar>
              </v-list-item-avatar>
              <v-list-item-title>다이어리 삭제</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-bottom-sheet>
      </div>
    </nav>
    <!-- diary 시작 -->
    <div class="m-3 diary-section d-flex flex-column justify-content-between" v-if="currentBaby">
      <div>
        <div class="diary-top">
          <div class="d-flex justify-content-between">
            <h4>{{diary.diary.create_date | moment('YYYY.M.DD')}}</h4>
            <span class="color-blue font-weight-bold">#{{ currentBaby.baby_name }} 태어난지 {{ countDays }}일</span>
          </div>
        </div>
        <hr class="divider">
        <div class="diary-title">
          <h5>{{diary.diary.title}}</h5>
        </div>
        <div class="diary-content ">
          <p class="text" v-html="this.diaryContent">
          </p>
        </div>
      </div>
      <div>
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
                <p class="growth-record mb-3" v-if="diary.measurement.height">
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
        <div class="diary-bottom d-flex justify-content-end my-3">
          <div>
            <p class=" m-0 diary-creator">
              <!-- <img :src="diary.diary.creator.profile_img"> -->
              <img class="profile-img mr-2" src="https://i.pinimg.com/236x/bf/ee/d2/bfeed24a2d24b42347faff4d27d3941c.jpg">
              <span>{{diary.diary.creator.name}}({{ diary.relationship.relationship_name}})</span>
            </p>
          </div>
        </div>
      </div>

    </div>
    <div class="comment p-2">
      <p class="comment-title mb-3">댓글 </p>
      <!-- 댓글 작성 -->
      <div class="d-flex comment-create pt-2">
        <div class="col-10">
          <textarea
            class="textareaSection w-100" 
            @keyup.enter="enterComment" 
            @input="activeBtn"
            v-model="commentData.content" 
            type="content" 
            placeholder="댓글을 작성하세요 :)" 
            rows="1" 
            autofocus
          ></textarea>
        </div>
        <div class="col-2 d-flex align-items-center">
          <button 
            :class="{ 'btn-pink': btnActive, 'pointer': btnActive }"
            class="btn w-100"
            :disabled="!btnActive"
            @click="clickComment"
          >
          <i class="fas fa-paper-plane"></i></button>
        </div>
      </div>
      <!-- 댓글 리스트 -->
      <div class="comment-list">
        <div v-for="comment in comments" :key="`comment_${comment.id}`">
          <div>
            <div class="d-flex justify-content-between">
              <p class="comment-username">{{comment.user.name}}({{comment.relationship_name}})</p>
              <div class="d-flex">
                <p class="comment-time mr-3">{{comment.modify_date |  moment("from", "now")}}</p>
                <div v-if="comment.user.id === myaccount.id">
                  <div>
                    <v-bottom-sheet v-model="sheet2">
                      <template v-slot:activator="{ on, attrs }">
                        <v-icon
                          class="top-right-icons"
                          color="#FEA59C"
                          v-bind="attrs"
                          v-on="on" 
                          >mdi-dots-vertical</v-icon>
                      </template>
                      <v-list>
                        <v-list-item @click="clickInitUpdateComment(comment)">
                          <v-list-item-avatar>
                            <v-avatar size="32px" tile>
                            <v-icon color="#FEA59C">mdi-share-outline</v-icon>
                            </v-avatar>
                          </v-list-item-avatar>
                          <v-list-item-title>댓글 수정</v-list-item-title>
                        </v-list-item>
                        <v-list-item  @click="clickDeleteComment(commentData, comment.id)">
                          <v-list-item-avatar>
                            <v-avatar size="32px" tile>
                            <v-icon color="#FEA59C">mdi-square-edit-outline</v-icon>
                            </v-avatar>
                          </v-list-item-avatar>
                          <v-list-item-title>댓글 삭제</v-list-item-title>
                        </v-list-item>
                      </v-list>
                    </v-bottom-sheet>
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
              <div class="d-flex comment-create pt-2">
                <div class="col-10">
                  <textarea
                    class="textareaSection w-100" 
                    @keyup.enter="enterUpdateComment" 
                    @input="updateActiveBtn(comment.content)"
                    v-model="commentUpdateData.content" 
                    type="content" 
                    rows="1" 
                    autofocus
                  ></textarea>
                </div>
                <div class="col-2 d-flex align-items-center">
                  <button 
                    :class="{ 'btn-pink': btnActive, 'pointer': btnActive }"
                    class="btn w-100"
                    :disabled="!updateBtnActive"
                    @click="clickUpdateComment(commentUpdateData)"
                  >
                  <i class="fas fa-paper-plane"></i></button>
                </div>
              </div>
            </div>
          </div>
          <hr>
        </div>
      </div>
    </div>

    <div class="space" style="height: 6vh;"></div>
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
      sheet2: false,
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
    ...mapState(['myaccount', 'currentBaby']),
    ...mapState('diaryStore', ['diary', 'comments']),
    countDays() {
      if (this.currentBaby) {
        var d1 = new Date() 
        var d2 = new Date(this.currentBaby.birth)
        var days2 = Math.ceil(Math.abs(d1-d2)/(8.64e+7))
        return days2
      }
      else {
        return null
      }
    },
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
      this.sheet2 = !this.sheet2
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
      this.sheet2 = !this.sheet2
    },
    clickUpdateComment(comment) {
      this.updateComment(comment)
      this.commentUpdateData.commentId = null
      this.commentUpdateData.content = null
      this.updateBtnActive = false
      this.sheet2=false
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
    clickBack() {
      this.$router.go(-1)
    },
  },
  mounted() {
    this.findDiary(this.$route.params.diaryId)
  }

}
</script>

<style scoped lang="scss">
nav {
  height: 7vh;
}
.diary-section {
  min-height: 60vh; 
}

.diary-top {
  h4 {
    font-weight: 900;
  }
}

.divider {
  margin-top: 0px;
}

.diary-bottom {
  .diary-date {
    p {
      margin: 0;
      font-weight: 700;
    }
  }
  .diary-creator {
    p {
      margin: 0;
    }
    .profile-img {
      border-radius: 50%;
      width: 2rem;
      height: 2rem;
    }
    
  }
}

.diary-title {
  h5 {
    font-weight: 900;
  }
}
.diary-content {
  p {
  white-space: pre-wrap;
  word-wrap: break-word;
  }
}

.diary-footer {
  color: #979797;
}

.measurement {
  border: 1px solid #9BC7FF;
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
  background: #FAFAFA;
  min-height: 23vh;
  .comment-title {
    font-weight: 500;
    // color: #FEA59C;
  }

  .comment-create {
    background: #FAFAFA;
    .col-10 {
      padding: 0;
      padding-left: 0.5rem;
      textarea {
        background: white;
        border-radius: 15px;
        padding: 5px;
        &:focus {
          outline-style: none; 
        }
      }
    }
    .col-2 {
      padding: 0;
      button {
        color: #FEA59C;
        padding: 0;
      }
    }
    

    
  }
  
  .comment-list {
    padding-top: 0.5rem;
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

.space {
  background: white;
}

</style>

<style scoped>
.diary-content >>> img {
  max-width: 100%;
}
</style>