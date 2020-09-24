<template>
  <div class="">
    <nav color="#FFFFFF" class="d-flex justify-content-between w-100">
      <v-icon 
        class="top-left-icons pointer" 
        color="#FEA59C"
        @click="clickBack"
      >mdi-arrow-left</v-icon>
      <v-spacer></v-spacer>
      <div>
        <v-icon class="top-right-icons" color="#FEA59C">mdi-folder-outline</v-icon>
        <v-icon class="top-right-icons" color="#FEA59C">mdi-heart-outline</v-icon>
        <!-- <v-icon class="top-right-icons" color="#FEA59C">mdi-dots-horizontal</v-icon> -->
        
        <v-bottom-sheet v-model="photo_sheet">
          <template v-slot:activator="{ on, attrs }">
            <v-icon
              class="top-right-icons"
              color="#FEA59C"
              v-bind="attrs"
              v-on="on" 
              @click="clickPhotoMenu()">mdi-dots-vertical</v-icon>
          </template>
          <v-list>
            <v-list-item @click="photoDelete()">
              <v-list-item-avatar>
                <v-avatar size="32px" tile>
                <v-icon color="#FEA59C">mdi-trash-can-outline</v-icon>
                </v-avatar>
              </v-list-item-avatar>
              <v-list-item-title>사진 삭제하기</v-list-item-title>
            </v-list-item>
            <v-list-item @click="photoTagUpdate()">
              <v-list-item-avatar>
                <v-avatar size="32px" tile>
                <v-icon color="#FEA59C">mdi-square-edit-outline</v-icon>
                </v-avatar>
              </v-list-item-avatar>
              <v-list-item-title>태그 수정하기</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-bottom-sheet>
      </div>
    </nav>

    <div class="p-3" v-if="photo">
      <div class="photo-content">
        <div class="photo-container">
          <!-- <img src="https://t1.daumcdn.net/tvpot/thumb/s8b90Dh8u7sDgMlccgchys3/thumb.png?ts=1541536764"> -->
          <img :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + photo.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'">
        </div>
        <div class="mt-3 tag-container">
          <v-chip v-for="tag in photo.photo_tags" :key="tag.id" class="ma-2" outlined color="#FEA59C" style="font-size:16px; margin-right:10px; color: #FEA59C;">#{{ tag.tag_name }}</v-chip>
          <!-- <v-chip class="ma-2" outlined color="#FEA59C" style="font-size:16px; color: #FEA59C;"> #할머니 집 </v-chip> -->
          
        </div>

        <div class="mt-2 photo-date text-muted">
          <p>{{photo.create_date | convertDate}}</p>
        </div>
        <!-- <div class="mt-2 photo-location text-muted">
          <p><v-icon>mdi-map-marker</v-icon>서울특별시 강남구 역삼동</p>
        </div> -->
      </div>
      <div class="mt-4 comment-content">
        <div class="scallop-down"></div>

        <!-- 댓글 -->
        <div class="comment mb-5 mt-3">
          <h5 class="comment-title mb-3">댓글</h5>
          <!-- 댓글 작성 -->
          <div class="input-group row no-gutters comment-create mb-3" style="height:65px;">
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
          <div class="comment-list" v-if="comments">
            <div v-if="comments.length">
              <div v-for="comment in comments" :key="`comment_${comment.id}`">
                <div>
                  <div class="d-flex justify-content-between">
                    <p class="comment-username">{{comment.user.name}}</p>
                    <div class="d-flex">
                      <p class="comment-time">{{comment.modify_date |  moment("from", "now")}}</p>
                      <div class="dropdown" v-if="comment.user.id === myaccount.id">
                        <div class="btn-group dropleft">
                          <button 
                            @click="sheet2=!sheet2" 
                            type="button" 
                            class="btn btn-pink">:</button>
                          <v-bottom-sheet v-model="sheet2">
                            <v-sheet class="text-center" height="18vh">
                              <div class="py-3">
                                <div class="pointer diary-option mb-3" @click="clickInitUpdateComment(comment)">댓글 수정</div>
                                <hr>
                                <div class="pointer diary-option"  @click="clickDeleteComment(commentData, comment.id)"> 댓글 삭제</div>
                              </div>
                            </v-sheet>
                          </v-bottom-sheet>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- 댓글 수정 X - 댓글 내용 노출 -->
                  <div v-if="comment.id != commentUpdateData.comment_id">
                    {{ comment.content }}
                  </div>
                  <!-- 댓글 수정 클릭했을 때 - 댓글 수정란 노출 -->
                  <div v-else>
                    <div class="input-group row no-gutters comment-create" style="height:65px;">
                    <textarea
                      class="col-10 textareaSection p-1" 
                      @keyup.enter="enterUpdateComment" 
                      @input="updateActiveBtn(comment.content)"
                      v-model="commentUpdateData.comment.content" 
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
        </div>
      </div>
    </div>
    <div style="height:15vh"></div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import Swal from 'sweetalert2'

const swal = Swal.mixin({
  customClass: {
    confirmButton: 'btn btn-success mr-2',
    cancelButton: 'btn btn-danger'
  },
  buttonsStyling: false
})

export default {
  name: 'PhotoDetail',
  data() {
    return {
      comment_content : '',
      height: '45vh',
      photo_sheet: false,
      sheet: false,
      sheet2: false,
      selectedCommentId: "",
      commentData: {
        content: null,
        photo_id: this.$route.params.photoId
      },
      btnActive: false,
      commentUpdateData: {
        photo_id: this.$route.params.photoId,
        comment_id: null,
        comment: {
          content: null,
        }
      },
      updateBtnActive: false,
    }
  },
  computed: {
    ...mapState(['myaccount']),
    ...mapState('photoStore', ['photo', 'comments'])
  },
  watch: {
    photo() {
      if (this.photo) {
        this.photoContent = this.photo.content
        this.fetchComments(this.$route.params.photoId)
      }
    }
  },
  methods: {
    ...mapActions('photoStore', ['findPhoto', 'fetchComments', 'createComment', 'updateComment', 'deleteComment', 'deletePhoto']),
    clickBack() {
      this.$router.go(-1)
    },
    clickCreateComment(){
      let commentData = {photoId : this.$route.params.photoId, content : this.comment_content};
      this.createComment(commentData);
    },
    changeHeight() {
      this.height = '57vh'
    },
    activeBtn() {
      if (this.commentData.content) {
        this.btnActive = true
      } else {
        this.btnActive = false
      }
    },
    updateActiveBtn(priorContent) {
      if (this.commentUpdateData.comment.content !== priorContent) {
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
          this.deleteComment({ photoId: this.$route.params.photoId, commentId: commentId })
          this.sheet2 = !this.sheet2
        }
        else {
          this.sheet2 = !this.sheet2
        } 
      });
      
    },
    clickInitUpdateComment(comment) {
      this.commentUpdateData.comment_id = comment.id 
      this.commentUpdateData.comment.content = comment.content
      this.sheet2 = !this.sheet2
    },
    clickUpdateComment(commentUpdateData) {
      console.log(this.commentUpdateData)
      this.updateComment(commentUpdateData)
      .then(() => {
        this.commentUpdateData.comment_id = null
        this.commentUpdateData.comment.content = null
        this.updateBtnActive = false
      })
    },
    enterUpdateComment() {
      if (this.commentUpdateData.comment.content.length === 1){
        this.commentUpdateData.comment.content = null
        this.updateBtnActive = false
        Swal.fire({
          icon: 'error',
          text: '댓글을 작성해주세요.'
        })
      } else {
        this.updateComment(this.commentUpdateData)
        .then(() => {
          this.commentUpdateData.comment_id = null
          this.commentUpdateData.comment.content = null
          this.updateBtnActive = false
        })  
      }
    },
    clickEdit() {
      this.$router.push({ name: 'DiaryUpdate', params: { diaryId: this.$route.params.diaryId }})
    },
    photoDelete(){
      //this.clickFinal();
      this.photo_sheet = false;
      console.log("photoDelete");
      if(confirm("사진을 삭제하시겠습니까?")){
        
        let commentData = {photoId : this.$route.params.photoId};
        console.log("commentDelete", commentData);
        this.deletePhoto(commentData);
      }
      
    },
    photoTagUpdate() {
      var photoData = {
        id: this.photo.id,
        image_url: this.photo.image_url,
        last_modified: this.photo.last_modified,
        size: this.photo.size,
        file_type: this.photo.file_type,
        tags: []
      }
      this.photo.photo_tags.forEach(tag => {
        photoData.tags.push(tag.tag_name)
      });
      this.$router.push({ name: "TagSelect", params: { photoData: photoData, photoType: "update" }})
    }
  },
  filters: {
    convertDate(val){
      //let date = new Date((new Date(val)/1000 + new Date(val).getTimezoneOffset() * 60)*1000);
      let date = new Date(val);
      let year = date.getFullYear();
      let month = date.getMonth()+1;
      let day = date.getDate();
      day = day < 10 ? '0'+day : day;
      let hour = date.getHours();
      hour = hour < 10 ? '0'+hour : hour;
      let min = date.getMinutes();
      min = min < 10 ? '0'+min : min;
      let strDate = year+"년 "+month+"월 "+day+"일 "+hour+":"+min;
      return strDate
    },
    diffDate(val) {
      //let diff = ((new Date() - (new Date(val))) / 1000) - new Date(val).getTimezoneOffset() * 60;
      let diff = (new Date() - (new Date(val))) / 1000;
      
      if(diff < 60)
        return '방금 전'
      diff /= 60;
      if(diff < 60)
        return parseInt(diff) + '분 전'
      diff /= 60;
      if(diff < 24)
        return parseInt(diff) + '시간 전'
      diff /= 24;
      if(diff < 7)
        return parseInt(diff) + '일 전'
      if (diff < 30)
        return parseInt(diff/7) + '주 전'
      if (diff < 365)
        return parseInt(diff/30) + '달 전'
      return parseInt(diff/365) + '년 전'
    }
  },
  mounted() {
    this.findPhoto(this.$route.params.photoId);
    // this.fetchComments(this.$route.params.photoId);
    //alert(this.$route.params.photoId);
  }
}
</script>
<style scoped lang="scss">
nav {
  background: white;
  position: fixed;  
}

.top-left-icons{
  font-size:28px;
}
.top-right-icons{
  margin-left:5px;
  font-size:28px;
}
.photo-container{
    text-align:center;
}
.photo-content .photo-container img{
    width: 100%;  
}

.tag-container{
   margin-top:10px;
}
.photo-date p{
  font-size:1.2rem;
}
.photo-date p, .photo-location p{
  margin:0;
}
.comment-content .nickname{
  font-weight:bold;
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