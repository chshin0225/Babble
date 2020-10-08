<template>
  <div class="mt-2">
    <div >
        <div style="float:right;">
        <!-- <button class="btn btn-outline-pink" style="">전체선택</button> -->
        <!-- <button class="btn btn-outline-pink" style="margin-left:6px !important;">그룹추가</button> -->

        <v-dialog v-model="dialog" width="70vw">
          <template v-slot:activator="{ on, attrs }">
            <button
              v-bind="attrs"
              v-on="on" 
              class="btn btn-pink mr-3" 
              style="margin-left:6px !important;"
              @click="newGroupName=''"
              @click.stop="dialog = true">그룹 생성</button>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">새 그룹 추가</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field label="그룹 이름*" required v-model="newGroupName"></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
              <v-btn color="blue darken-1" text @click="addNewGroup">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>



      </div>
    </div>
    <div style="width:100%; display:inline-block;">
      <v-list>
      <v-list-group
          v-for="group in groups"
          :key="group.id"
          v-model="group.active"
        no-action
      >
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title v-text="group.group_name"></v-list-item-title>
          </v-list-item-content>
            <v-dialog v-model="modify_dialog" width="70vw">
              <template v-slot:activator="{ on, attrs }">
                  <v-icon
                    style="margin-left:24px;"
                    v-bind="attrs"
                    v-on="on"
                    @click="newGroupName = group.group_name"
                    @click.stop="modify_dialog = true"
                  >mdi-pencil</v-icon>
                <v-icon color="pink" @click="deleteGroup(group.id)">mdi-trash-can-outline</v-icon>
              </template>
              <v-card>
                <v-card-title>
                  <span class="headline">그룹 이름 변경</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field label="그룹 이름*" required v-model="newGroupName"></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="modify_dialog = false">Close</v-btn>
                  <v-btn color="blue darken-1" text @click="modifyGroupName(group.id)">Save</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
        </template>
        <div v-if="group.members.length">
          <v-list-item
            v-for="member in group.members"
            :key="member.id"
          >
            <v-list-item-avatar>
              <!-- <v-img
                :src=""
              ></v-img> -->
              <v-icon>mdi-account</v-icon>
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title>{{member.name}}</v-list-item-title>
              <v-list-item-subtitle>{{member.relationship_name}}</v-list-item-subtitle>
            </v-list-item-content>
            <v-list-item-icon>
                <v-icon color="red" @click="deleteUser(group.id, member.user)">mdi-trash-can-outline</v-icon>
            </v-list-item-icon>
          </v-list-item>
        </div>
        <div v-else>
          <p class="pl-2">아직 해당 그룹에 속한 유저가 없습니다.</p>
        </div>
      </v-list-group>
    </v-list>


    </div>
  </div>
</template>

<script>

import { mapActions, mapState, mapGetters } from 'vuex'
import Swal from 'sweetalert2'

const swal = Swal.mixin({
  customClass: {
    confirmButton: 'btn btn-success mr-2',
    cancelButton: 'btn btn-danger'
  },
  buttonsStyling: false
})

export default {
  name: 'GroupEdit',
  data() {
    return {
      dialog:false,
      modify_dialog:false,
      newGroupName:"",
    }
  },
  computed: {
    ...mapState('settingStore', ['groups', 'users']),
    ...mapGetters(['config'])
  },
  
  methods:{
    ...mapActions('settingStore', ['fetchGroups', 'createGroup', 'deleteGroupUser', 'modifyGroup', 'deleteBabbleGroup']),
    addNewGroup(){
      let groupData = {group_name : this.newGroupName}
      this.createGroup(groupData)
        .then(() => {
          Swal.fire({
            icon: 'success',
            text: '새 그룹이 추가되었습니다.'
          })
            this.modify_dialog = false;
            this.dialog = false;
          this.fetchGroups();
        });
    },
    deleteGroup(groupId){
      swal.fire({
        text: "그룹을 삭제하시겠습니까?",
        showCancelButton: true,
        confirmButtonText: '네',
        cancelButtonText: '아니요',
        icon: "warning",
      })
      .then((result) => {
        if (result.value) {
        let groupData = {groupId : groupId}
        this.deleteBabbleGroup(groupData)
          .then(() => {
            Swal.fire({
              icon: 'success',
              text: '삭제되었습니다.'
            })
            this.modify_dialog = false;
            this.dialog = false;
            this.fetchGroups();
          });
        } 
      });
    },
    deleteUser(groupId, userId){
      swal.fire({
        text: "그룹에서 삭제하시겠습니까?",
        showCancelButton: true,
        confirmButtonText: '네',
        cancelButtonText: '아니요',
        icon: "warning",
      })
      .then((result) => {
        if (result.value) {
          let userData = {groupId : groupId , user : userId}
          this.deleteGroupUser(userData)
          .then(() => {
            this.modify_dialog = false;
            this.dialog = false;
            this.fetchGroups();
          });
        } 
      });
    },
    modifyGroupName(groupId){
      let groupData = {groupId : groupId, group_name : this.newGroupName}
      this.modifyGroup(groupData)
        .then(() => {
          Swal.fire({
            icon: 'success',
            text: '그룹 이름이 변경되었습니다.'
          })
          this.modify_dialog = false;
          this.dialog = false;
          this.fetchGroups();
        });
    },

  },

  mounted() {
    this.fetchGroups();
  },
}
</script>

<style scoped>
div >>> .v-list-group {
  border: 1px solid #FEA59C;
  border-radius: 10px;
  margin: 0 10px 10px 10px;

}

/* Style the buttons that are used to open and close the accordion panel */
.accordion {
  background-color: #eee;
  color: #444;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  text-align: left;
  border: none;
  outline: none;
  transition: 0.4s;
}

/* Add a background color to the button if it is clicked on (add the .active class with JS), and when you move the mouse over it (hover) */
.active, .accordion:hover {
  background-color: #ccc;
}

/* Style the accordion panel. Note: hidden by default */
.panel {
  padding: 0 18px;
  background-color: white;
  display: none;
  overflow: hidden;
}

.v-application--is-ltr .v-list-group--no-action > .v-list-group__items > .v-list-item{
  padding-left:16px !important;
}
.v-list-group .v-list-group__header .v-list-item__icon.v-list-group__header__append-icon{
  min-width : 36px !important;
}

</style>