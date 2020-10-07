<template>

  <div style="padding:0 5vw" v-if="users">
    <!-- 공동양육자 -->
    <div v-if="users.maintainers">
      <div v-if="users.maintainers.length">
        <h5>공동양육자</h5>
        <!-- <div v-for="user in users.maintainers" :key="`maintainer_${user.id}`"> -->
          
          <v-list-item 
            class="d-flex justify-content-between align-items-center"
            v-for="userItem in users.maintainers" 
            :key="`guest-${userItem.id}`"
          >
            <v-col col="3">
              <p class="m-0 mr-3 mb-5">{{ userItem.user.name }}</p>
            </v-col>
            <v-col col="9">
              <v-select
                class="ma-0 pa-0"
                :items="items"
                filled
                dense
                label="권한"
                v-model="userItem.rank"
                :item-text="'label'"
                :item-value="'value'"
                @change="changeRank(userItem.user.id, userItem.relationship_name, userItem.rank)"
              ></v-select>
            </v-col>
          </v-list-item>
        </div>
      </div>
    <!-- 손님 -->
    <div v-if="users.guests">
      <div class="d-flex justify-content-between mt-3" v-if="users.guests.length">
        <h5>손님</h5>
        <div>
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
                :key="`group_${group.id}`"
                @click="sheet = false"
              >
                <v-list-item-title @click="clickGroup(group.id)">{{ group.group_name }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-bottom-sheet>
        </div>
      </div>
    </div>

    <div v-if="users.guests">
      <div v-if="users.guests.length">
        <v-list-item-group
          multiple
        >
          <v-list-item v-for="userItem in users.guests" :key="`guest-${userItem.id}`">
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
                
                <v-select
                  :items="items"
                  filled
                  dense
                  label="권한"
                  v-model="userItem.rank"
                  :item-text="'label'"
                  :item-value="'value'"
                  @change="changeRank(userItem.user.id, userItem.relationship_name, userItem.rank)"
                ></v-select>
              </v-list-item-content>
              <v-list-item-icon>
                <v-icon v-if="myaccount.id != userItem.user.id" color="red" @click="deleteUser(userItem.user.id)">mdi-trash-can-outline</v-icon>
              </v-list-item-icon>
            </template>
          </v-list-item>
        </v-list-item-group>
        
      </div>
      <div v-else class="text-center">
        <img class="crying-baby" src="@/assets/baby.png">
        <h5>
          아직 초대된 회원이 없습니다.<br>
          다른 회원을 초대해주세요.
        </h5>
      </div>
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
        {label: "공동양육자", value:"2"},
        {label: "손님", value:"3"},
      ],
      isCheckAll : false,
    }
  },
  computed: {
    ...mapState('settingStore', ['groups', 'users']),
    ...mapState(['myaccount']),
    findStatus(rank) {
      if (rank === 2){
        return '공동양육자'
      } else {
        return '손님'
      }
    },
    
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
      for(var i=0; i<this.users.guests.length; i++){
        if(this.users.guests[i].isCheck == true){
          if(this.users.guests[i].group === null) {
            let userData = {groupId : groupId, user : this.users.guests[i].user.id};
            this.addUser(userData);
          }
        }
      }
      this.isCheckAll = false;
      
      for(var idx=0; idx<this.users.guests.length; idx++){
        this.users.guests[idx].isCheck = false;
      }
    },
    selectAll(){
      this.isCheckAll = !(this.isCheckAll);
      
        for(var idx=0; idx<this.users.guests.length; idx++){
          this.users.guests[idx].isCheck = this.isCheckAll;
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

  .crying-baby {
    margin-top: 20vh;
    height: 30vh;
    width: auto;
  }
</style>