<template>

  <div style="padding:0 5vw">
    
    <div style="width:100%;">
        <div style="float:right;">
        <button class="btn btn-outline-pink" style="" @click="selectAll">{{!isCheckAll?'전체 선택':'선택 해제'}}</button>
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
              :key="group.id"
              @click="sheet = false"
            >
              <v-list-item-title @click="clickGroup(group.id)">{{ group.group_name }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-bottom-sheet>
      </div>
    </div>
    <div style="width:100%;">
      <v-subheader>초대된 회원 목록</v-subheader>

      <v-list-item-group
        multiple
      >
        <v-list-item v-for="userItem in users" :key="userItem.id">
          <template v-slot:default="{ active }">
            <v-list-item-action>
              <v-checkbox
                :input-value="active"
                color="#FEA59C"
                v-model="userItem.isCheck"
              ></v-checkbox>
            </v-list-item-action>

            <v-list-item-content>
              <v-list-item-title>{{userItem.user.name}}</v-list-item-title>
              <v-list-item-subtitle>{{userItem.relationship_name}}</v-list-item-subtitle>
            </v-list-item-content>
            <v-list-item-content>
              
              <select 
                v-model="userItem.rank"
                class="selects"
                id="nickName"
                @change="changeRank(userItem.user.id, userItem.relationship_name, userItem.rank)"
              >
              <option v-for="item in items" :key="item.value" :value="item.value">
                {{ item.label }}
              </option>
              </select>
            </v-list-item-content>
            <v-list-item-icon>
              <v-icon v-if="myaccount.id != userItem.user.id" color="red" @click="deleteUser(userItem.user.id)">mdi-trash-can-outline</v-icon>
            </v-list-item-icon>
          </template>
        </v-list-item>
      </v-list-item-group>
      
    </div>
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
  name: 'UserEdit',
  data() {
    return {
      sheet:false,
      items:[
        {label: "Master", value:"1"},
        {label: "Maintainer", value:"2"},
        {label: "Guest", value:"3"},
      ],
      isCheckAll : false,
    }
  },
  computed: {
    ...mapState('settingStore', ['groups', 'users']),
    ...mapState(['myaccount'])
  },
  mounted() {
    this.fetchUsers();
    this.fetchGroups();
    
  },
  methods: {
    ...mapActions('settingStore', ['fetchUsers', 'fetchGroups', 'addUser', 'modifyUserRank', 'deleteBabbleUser']),
    clickBack() {
      this.$router.go(-1)
    },
    clickGroup(groupId){
      for(var i=0; i<this.users.length; i++){
        if(this.users[i].isCheck == true){
        
          let userData = {groupId : groupId, user : this.users[i].user.id};
          console.log("userData", userData);
          this.addUser(userData);
        }
      }
      this.isCheckAll = false;
      
      for(var idx=0; idx<this.users.length; idx++){
        this.users[idx].isCheck = false;
      }
    },
    selectAll(){
      this.isCheckAll = !(this.isCheckAll);
      
        for(var idx=0; idx<this.users.length; idx++){
          this.users[idx].isCheck = this.isCheckAll;
        }
    },
    changeRank(userId, userRelationship, userRank){
      
      let userData = {userId : userId, rank : userRank, relationship_name : userRelationship}
      this.modifyUserRank(userData);
    },
    deleteUser(userId){
      
      this.sheet = false;
      swal.fire({
        text: "BabbleBox에서 삭제하시겠습니까?",
        showCancelButton: true,
        confirmButtonText: '네',
        cancelButtonText: '아니요',
        icon: "warning",
      })
      .then((result) => {
        if (result.value) {
          let userData = {userId : userId}
          this.deleteBabbleUser(userData)
          .then(() => {
            Swal.fire({
              icon: 'success',
              text: '삭제되었습니다.'
            })
            this.sheet = false;
            this.fetchUsers();
          });
        } 
      });

    },
    
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