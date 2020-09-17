<template>
  <div>
    <div class="nav d-flex align-items-center">
      <div class="left-align pointer" @click="clickBack">
        <i class="fas fa-chevron-left"></i>
      </div>
      <div class="center-align d-flex align-items-center">
        <img class="float-left mr-2" width="30px" src="https://user-images.githubusercontent.com/25967949/93281500-2f491680-f807-11ea-97bb-3fb3a98bbabc.png">
        <h6>새 일기 작성</h6>
      </div>
    </div>
    
    <!-- 제목 -->
    <v-text-field 
      class="m-3" 
      label="제목"
      v-model="diaryData.title"
    ></v-text-field>

    <!-- 에디터 -->
     <editor 
      :options="editorOptions"
      height="80vh"
      initialEditType="wysiwyg"
      previewStyle="vertical"
      class="m-3"
      ref="toastuiEditor"
     />

    <!-- 성장 기록 -->
    <div class="mx-3 mt-5 mb-2">
      <h6>우리 아이 성장 기록</h6>
      <v-text-field
        label=" 키"
        suffix="cm"
        v-model="babyHeight"
      ></v-text-field>
      <v-text-field
        label="몸무게"
        suffix="kg"
        v-model="babyWeight"
      ></v-text-field>
      <v-text-field
        label="머리 둘레"
        suffix="cm"
        v-model="babyHead"
      ></v-text-field>
    </div>
    <div class="p-2 d-flex justify-content-end">
      <button @click="clickCreate()" class="btn btn-pink ">작성</button>
    </div>
    <div style="height:10vh"></div>
        
  </div>

  

</template>

<script>
import 'codemirror/lib/codemirror.css';
import '@toast-ui/editor/dist/toastui-editor.css';
import { mapActions } from 'vuex';

import { Editor } from '@toast-ui/vue-editor';

export default {
  name: 'DiaryCreate',
  components: {
    editor: Editor,
  },
  data() {
    return {
      // editorText: 'This is initialValue.',
      editorOptions: {
        hideModeSwitch: true,
        toolbarItems: [
          'heading', 'bold', 'italic', 'strike', 'divider','image', 'link', 'hr', 'ul', 'ol', 'task',
           'divider'
        ]
      },
      babyHead: 0,
      babyHeight: 0,
      babyWeight: 0,
      diaryData: {
        title: '',
        content: '',
        content_html: ''
      }
    };
  },
  methods: {
    ...mapActions('diaryStore', ['createDiary']),
    getHTML() {
      let html = this.$refs.toastuiEditor.invoke('getHtml');
      console.log(html)
    },
    clickBack() {
      this.$router.go(-1)
    },
    clickCreate() {
      this.diaryData.content_html = this.$refs.toastuiEditor.invoke('getHtml');
      this.diaryData.content = this.$refs.toastuiEditor.invoke('getMarkdown')
      // this.diaryData.content = this.diaryData.content_html;
      console.log(this.diaryData)
      this.createDiary(this.diaryData)
    }
  },
}
</script>

<style scoped lang="scss">
// btn
button:focus {
  outline: none;
}

/* nav */
.nav {
  background: white;
  -webkit-box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  height: 6vh;
  position: sticky;
  top: 0;
  z-index: 10000;

  .left-align {
    float: left;
    width: 33.3333%;
    text-align: left;
  }

  .center-align {
    float: left;
    width: 33.3333%;
    text-align: center;

    h6 {
      margin: 0;
      font-weight: 900;
    }
  }
}

.tui-editor-defaultUI-toolbar {
  position: sticky;
  top: 6vh;
}

.tui-editor-defaultUI {
  margin: 40px !important;
}

</style>