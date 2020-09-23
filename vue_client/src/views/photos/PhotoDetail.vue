<template>
  <div class="">
    <v-app-bar color="#FFFFFF" flat dense>
      <v-icon 
        class="top-left-icons pointer" 
        color="#FEA59C"
        @click="clickBack"
      >mdi-arrow-left</v-icon>
      <v-spacer></v-spacer>
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
        </v-list>
      </v-bottom-sheet>



    </v-app-bar>

      <div class="p-3">
      <div class="photo-content">
        <div class="photo-container">
          <!-- <img src="https://t1.daumcdn.net/tvpot/thumb/s8b90Dh8u7sDgMlccgchys3/thumb.png?ts=1541536764"> -->
          <img :src="'https://firebasestorage.googleapis.com/v0/b/babble-98541.appspot.com/o/' + photo.image_url + '?alt=media&token=fc508930-5485-426e-8279-932db09009c0'">
        </div>
        <div class="mt-3 tag-container">
          <v-chip class="ma-2" outlined color="#FEA59C" style="font-size:16px; margin-right:10px; color: #FEA59C;"> #놀이터 </v-chip>
          <v-chip class="ma-2" outlined color="#FEA59C" style="font-size:16px; color: #FEA59C;"> #할머니 집 </v-chip>
          
        </div>

        <div class="mt-2 photo-date text-muted">
          <p>{{photo.create_date | convertDate}}</p>
        </div>
        <div class="mt-2 photo-location text-muted">
          <p><v-icon>mdi-map-marker</v-icon>서울특별시 강남구 역삼동</p>
        </div>
      </div>
      <div class="mt-4 comment-content">
        
        <div class="scallop-down"></div>
        <div style="width:100%;display:inline-block;padding-bottom:5px;">
          <textarea
            style="width:100%; padding:5px; border:1px solid #a8a8a8; border-radius:5px;"
            v-model="comment_content"
            no-resize="no-resize"
            outlined="outlined"
            rows="2"
            placeholder="댓글을 입력하세요">
          </textarea>
          <button class="btn btn-outline-pink" style="float:right; padding:.15rem .75rem" @click="clickCreateComment()">등록</button>
        </div>
        <v-app id="comment_app">
        <div v-for="comment in comments" :key="`comment_${comment.id}`">
          <div>
            <div class="d-flex justify-content-between">
              <p class="nickname">{{comment.user.name}}</p>
              <p>{{comment.modify_date | diffDate}}</p>
            </div>
            <div class="d-flex justify-content-between">
              <div style="width:95%;">{{comment.content}}</div>
              <!-- <div style="width:95%;">
                <textarea
                  style="width:100%; padding:5px; border:1px solid #a8a8a8; border-radius:5px;"
                  v-model="comment.content"
                  no-resize="no-resize"
                  outlined="outlined"
                  rows="2"
                  placeholder="댓글을 입력하세요">
                </textarea>
              </div> -->
              <hr>
              <!--<v-icon v-if="comment.user.id" color="#FEA59C" @click="clickFinal()">mdi-dots-vertical</v-icon>-->

            
              <v-bottom-sheet v-model="sheet">
              <template v-slot:activator="{ on, attrs }">
                <v-icon v-if="comment.user.id" color="#FEA59C"
                  v-bind="attrs"
                  v-on="on" @click="clickCommentMenu(comment.id)">mdi-dots-vertical</v-icon>
              </template>
              <v-list>
                <!-- <v-subheader>Open in</v-subheader>
                <v-list-item
                  v-for="tile in tiles"
                  :key="tile.title"
                  @click="sheet = false"
                >
                  <v-list-item-avatar>
                    <v-avatar size="32px" tile>
                    <v-icon color="#FEA59C">{{tile.img}}</v-icon>
                    </v-avatar>
                  </v-list-item-avatar>
                  <v-list-item-title>{{ tile.title }}</v-list-item-title>
                </v-list-item> -->
                <v-list-item @click="commentModify()">
                  <v-list-item-avatar>
                    <v-avatar size="32px" tile>
                    <v-icon color="#FEA59C">mdi-pencil-outline</v-icon>
                    </v-avatar>
                  </v-list-item-avatar>
                  <v-list-item-title>댓글 수정하기</v-list-item-title>
                </v-list-item>
                <v-list-item @click="commentDelete()">
                  <v-list-item-avatar>
                    <v-avatar size="32px" tile>
                    <v-icon color="#FEA59C">mdi-trash-can-outline</v-icon>
                    </v-avatar>
                  </v-list-item-avatar>
                  <v-list-item-title>댓글 삭제하기</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-bottom-sheet>
          








            </div>
          </div>
          <hr>
        </div>
        </v-app>
      </div>
    </div>
    <div style="height:15vh"></div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'PhotoDetail',
  data() {
    return {
      comment_content : '',
      height: '45vh',
      photo_sheet: false,
      sheet: false,
      /*comment_tiles: [
        { img: 'mdi-pencil-outline', title: '댓글 수정하기' },
        { img: 'mdi-trash-can-outline', title: '댓글 삭제하기' },
      ],*/
      selectedCommentId: ""
    }
  },
  computed: {
    ...mapState('photoStore', ['photo', 'comments'])
  },
  methods: {
    ...mapActions('photoStore', ['findPhoto', 'fetchPhotoComments', 'createPhotoComment', 'modifyPhotoComment', 'deletePhotoComment', 'deletePhoto']),
    clickBack() {
      this.$router.go(-1)
    },
    clickCreateComment(){
      let commentData = {photoId : this.$route.params.photoId, content : this.comment_content};
      this.createPhotoComment(commentData);
    },
    changeHeight() {
      this.height = '57vh'
    },
    /*clickFinal() {
      //this.sheet = !this.sheet
      this.sheet = false;
      //this.createPhotos(this.photos)
    },*/
    commentModify(){
      //this.clickFinal();
      this.sheet = false;
      //console.log("commentModify", this.selectedCommentId);
    },
    commentDelete(){
      //this.clickFinal();
      this.sheet = false;
      console.log("commentDelete", this.selectedCommentId);
      if(confirm("댓글을 삭제하시겠습니까?")){
        
        let commentData = {photoId : this.$route.params.photoId, commentId : this.selectedCommentId};
        console.log("commentDelete", commentData);
        this.deletePhotoComment(commentData);
      }
      
    },
    clickCommentMenu(commentId){
      //this.clickFinal();
      console.log("clickCOmmentMenu", commentId);
      this.selectedCommentId = commentId;
    },
    clickPhotoMenu(){
      //console.log("clickCOmmentMenu", commentId);
      //this.selectedCommentId = commentId;
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
    this.fetchPhotoComments(this.$route.params.photoId);
    //alert(this.$route.params.photoId);
  }
}
</script>
<style scoped>
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
/* 
#comment_app{
  height:15vh;
} */


#app {
  min-height: 0 !important;
}

</style>