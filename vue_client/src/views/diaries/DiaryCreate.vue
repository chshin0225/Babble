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
    <!-- 모달 창 -->
    <Modal ref="ytmodal" @onConfirm="addCommand" />
    <!-- 옵션 선택 -->
    <editor-menu-bar
      class="menu"
      :editor="editor" 
      v-slot="{ commands, isActive }"
    >
      <div class="menubar">
        <button 
          class="menubar__button"
          :class="{ 'is-active': isActive.bold() }" 
          @click="commands.bold"
        >
          <i class="fas fa-bold"></i>
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.italic() }"
          @click="commands.italic"
        >
          <i class="fas fa-italic"></i>
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.strike() }"
          @click="commands.strike"
        >
          <i class="fas fa-strikethrough"></i>
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.underline() }"
          @click="commands.underline"
        >
          <i class="fas fa-underline"></i>
        </button>
        <button
          class="menubar__button"
          @click="openModal(commands.image);"
        >
          <i class="fas fa-image"></i>
        </button>

        <button
          class="menubar__button"
          @click="commands.undo"
        >
          <i class="fas fa-undo"></i>
        </button>

        <button
          class="menubar__button"
          @click="commands.redo"
        >
          <i class="fas fa-redo"></i>
        </button>

      </div>

    </editor-menu-bar>

    <editor-content class="editor-content" :editor="editor" />
  </div>

</template>

<script>
import { Editor, EditorContent, EditorMenuBar } from 'tiptap'
import { Bold, Italic, Strike, Underline, HardBreak,  History, Image} from 'tiptap-extensions'
import Modal from "./Modal";

export default {
  name: 'DiaryCreate',
  components: {
    EditorContent,
    EditorMenuBar,
    Modal,
  },
  props: {
    content: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      editor: new Editor({
        content: '<p>내용을 작성해주세요!</p>',
        extensions: [
          new Bold(),
          new Italic(),
          new Strike(),
          new Underline(),
          new HardBreak(),
          new History(),
          new Image(),
        ],
        onUpdate: ({ getHTML }) => {
          let content = getHTML();
          console.log(content);
        }
      }),
    }
  },
  methods: {
    openModal(command) {
      this.$refs.ytmodal.showModal(command);
    },
    addCommand(data) {
      if (data.command !== null) {
        data.command(data.data);
      }
    },
    setContent() {
      this.editor.setContent(this.content);
    },
    clickBack() {
      this.$router.go(-1)
    }
  },
  mounted() {
    this.setContent();
  },
  beforeDestroy() {
    // Always destroy your editor instance when it's no longer needed
    this.editor.destroy()
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

// editor-menu-bar
.menu {
  background-color: white;
  color: #9BC7FF;
  -webkit-box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.1);
  width: 100%;
  position: sticky;
  z-index: 10000;
  top:6vh;
    
  .menubar__button {
    font-weight: 700;
    display: -webkit-inline-box;
    display: inline-flex;
    background: transparent;
    border: 0;
    padding: .2rem .5rem;
    margin-right: .2rem;
    border-radius: 3px;
    cursor: pointer;
  }

  .is-active {
    background-color: rgba(0,0,0,.1) !important;
  }

}

// editor content
.editor-content:focus {
  outline: none !important;
}

.editor-content {
  height: 80vh;
  .ProseMirror {
    // height: 80vh;

    p:focus {
      outline: none !important;
    }
  }
  .ProseMirror-focused, .ProseMirror:focus, .ProseMirror{
    outline: none !important;
  }
}


.tiptap-vuetify-editor__content {
  min-height: 200px;
  max-height: 200px;
}

</style>