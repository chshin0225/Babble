<template>

  <div style="padding : 0 5vw;">
    <div style="width:100%;">
        <div style="float:right;">
        <!-- <button class="btn btn-outline-pink" style="">전체선택</button> -->
        <!-- <button class="btn btn-outline-pink" style="margin-left:6px !important;">그룹추가</button> -->

        <v-dialog v-model="dialog" width="70vw">
          <template v-slot:activator="{ on, attrs }">
            <button
              v-bind="attrs"
              v-on="on" 
              class="btn btn-outline-pink" 
              style="margin-left:6px !important;"
              @click.stop="dialog = true">그룹추가</button>
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
    <div style="width:100%;">
      <v-expansion-panels focusable accordion>
        <v-expansion-panel
          v-for="group in groups"
          :key="group.id"
        >
          <v-expansion-panel-header>
            {{group.group_name}}
            <v-spacer></v-spacer>
            <!-- <v-icon>mdi-pencil</v-icon> -->
                
            <v-dialog v-model="modify_dialog" width="70vw">
              <template v-slot:activator="{ on, attrs }">
                <!-- <button
                  v-bind="attrs"
                  v-on="on" 
                  class="btn btn-outline-pink" 
                  style="margin-left:6px !important;"
                  @click.stop="dialog = true">그룹추가</button> -->
                  <v-icon
                    v-bind="attrs"
                    v-on="on"
                    @click.stop="modify_dialog = true"
                  >mdi-pencil</v-icon>
                <v-icon color="red" @click="deleteGroup(group.id)">mdi-trash-can-outline</v-icon>
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



            
            </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-list>

              <v-list-item
                v-for="member in group.members"
                :key="member.id"
              >
                <!-- {{member.relationship_name}}{{member.name}} -->
                <v-list-item-content>
                  <v-list-item-title>{{member.user.name}}</v-list-item-title>
                  <v-list-item-subtitle>{{member.relationship_name}}</v-list-item-subtitle>
                </v-list-item-content>
                <v-spacer></v-spacer>
                <v-icon color="red" @click="deleteUser(group.id, member.id)">mdi-trash-can-outline</v-icon>
              </v-list-item>
            </v-list>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>



    </div>
  </div>
</template>

<script>

import { mapActions, mapState } from 'vuex'

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
    ...mapState('settingStore', ['groups', 'users'])
  },
  mounted() {
    this.fetchGroups();
    
  },
  methods:{
    ...mapActions('settingStore', ['fetchGroups', 'createGroup', 'deleteGroupUser', 'modifyGroup', 'deleteBabbleGroup']),
    addNewGroup(){
      let groupData = {group_name : this.newGroupName}
      this.createGroup(groupData);
    },
    deleteGroup(groupId){
      if(confirm("그룹을 삭제하시겠습니까?")){
        let groupData = {groupId : groupId}
        this.deleteBabbleGroup(groupData);
      }
    },
    deleteUser(groupId, userId){
      if(confirm("그룹에서 삭제하시겠습니까?")){
        let userData = {groupId : groupId , user : userId}
        this.deleteGroupUser(userData);
      }
    },
    modifyGroupName(groupId){
      let groupData = {groupId : groupId, group_name : this.newGroupName}
      this.modifyGroup(groupData);
    }
  },
}
</script>

<style scoped>
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

</style>