<template>

  <div style="padding:0 5vw">
    
    <div style="width:100%;">
        <div style="float:right;">
        <button class="btn btn-outline-pink" style="" @click="selectAll">전체선택</button>
        <!-- <button class="btn btn-outline-pink" style="margin-left:6px !important;">그룹에 추가</button> -->
        <v-bottom-sheet v-model="sheet">
          <template v-slot:activator="{ on, attrs }">
            <button 
                class="btn btn-outline-pink" 
                style="margin-left:6px !important;"
                v-bind="attrs"
                v-on="on">그룹에 추가</button>
          </template>
          <v-list>
            <v-subheader>그룹 목록</v-subheader>
            <v-list-item
              v-for="group in groups"
              :key="group.name"
              @click="sheet = false"
            >
              <v-list-item-title @click="clickGroup(group.id)">{{ group.name }}</v-list-item-title>
            </v-list-item>
            <!-- <v-list-item @click="commentModify()">
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
            </v-list-item> -->
          </v-list>
        </v-bottom-sheet>
      </div>
    </div>
    <div style="width:100%;">


      <!-- <div class="user-list" v-for="user in users" :key="`user_${user.id}`" >
        <v-checkbox v-model="checkbox1" label="강슬기"></v-checkbox>
      </div>
      <div class="user-list"><v-checkbox v-model="checkbox1" label="박선환"></v-checkbox></div>
      <div class="user-list"><v-checkbox v-model="checkbox1" label="방소윤"></v-checkbox></div>
      <div class="user-list"><v-checkbox v-model="checkbox1" label="이근우"></v-checkbox></div>
      <div class="user-list"><v-checkbox v-model="checkbox1" label="신채원"></v-checkbox></div>
      <div class="user-list"><v-checkbox v-model="checkbox1" label="신채린"></v-checkbox></div> -->
      

      <v-subheader>초대된 회원 목록</v-subheader>

      <v-list-item-group
        multiple
      >
        <v-list-item v-for="user in users" :key="user.id">
          <template v-slot:default="{ active }">
            <v-list-item-action>
              <v-checkbox
                :input-value="active"
                color="#FEA59C"
                v-model="user.isCheck"
              ></v-checkbox>
            </v-list-item-action>

            <v-list-item-content>
              <v-list-item-title>{{user.name}}</v-list-item-title>
              <v-list-item-subtitle>{{user.relationship_name}}</v-list-item-subtitle>
            </v-list-item-content>
            <v-list-item-content>
              <!-- <v-select
                :items="items"
                label="Outlined style"
                outlined
                dense
              ></v-select> -->
              
              <select 
                v-model="user.rank"
                class="selects"
                id="nickName"
                @change="changeRank(user.id, user.relationship_name, user.rank)"
              >
              <option v-for="item in items" :key="item.value" :value="item.value">
                {{ item.label }}
              </option>
              </select>
            </v-list-item-content>
            <v-list-item-icon>
              <v-icon color="red">mdi-trash-can-outline</v-icon>
            </v-list-item-icon>
          </template>
        </v-list-item>
      </v-list-item-group>
      
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'UserEdit',
  data() {
    return {
      sheet:false,
      items:[
        {label: "Master", value:"1"},
        {label: "Maintainer", value:"2"},
        {label: "Guest", value:"3"},
      ],
      users:[
        {id:"1", relationship_name:'엄마', name:'박지우', rank:"1"},
        {id:"2", relationship_name:'아빠', name:'김호준', rank:"2"},
        {id:"3", relationship_name:'할아버지', name:'박명환', rank:"3"},
        {id:"4", relationship_name:'할머니', name:'최미숙', rank:"3"},
        {id:"5", relationship_name:'할아버지', name:'김명수', rank:"3"},
        {id:"6", relationship_name:'할머니', name:'이명자', rank:"3"},
        {id:"7", relationship_name:'이모', name:'박지우', rank:"3"},
        {id:"8", relationship_name:'삼촌', name:'김명준', rank:"3"},
        {id:"9", relationship_name:'고모', name:'손유리', rank:"3"},
        {id:"10", relationship_name:'아빠친구', name:'심연우', rank:"3"},
        {id:"11", relationship_name:'이모', name:'박소정', rank:"3"},
        {id:"12", relationship_name:'숙부', name:'김권식', rank:"3"},
      ]
    }
  },
  computed: {
    //...mapState('settingStore', ['groups', 'users'])
    ...mapState('settingStore', ['groups'])
  },
  mounted() {
    this.fetchUsers();
    this.fetchGroups();
    
  },
  methods: {
    ...mapActions('settingStore', ['fetchUsers', 'fetchGroups', 'addUser', 'modifyUserRank']),
    clickBack() {
      this.$router.go(-1)
    },
    clickGroup(groupId){
      for(var i=0; i<this.users.length; i++){
        if(this.users[i].isCheck == true){
        
          let userData = {groupId : groupId, user : this.users[i].id};
          this.addUser(userData);
        }
      }
    
    },
    selectAll(){
      for(var i=0; i<this.users.length; i++){
        this.users[i].isCheck = true;
      }
    },
    changeRank(userId, userRelationship, userRank){
      let userData = {userId : userId, rank : userRank, relationship_name : userRelationship}
      this.modifyUserRank(userData);
    }
  },
}
</script>

<style scoped>

  button {
    border-radius:0.5rem;
    padding: 0.3rem 0.5rem; 
    margin: 0 !important;
  }

  .user-list {
    width:100%;
  }
  
  .selects {
    border: 1px solid #aea4a3;
    background-color: transparent;
    width: 100%;
    padding: 10px;
    padding-left: 10px;
    padding-right: 10px;
  }
</style>