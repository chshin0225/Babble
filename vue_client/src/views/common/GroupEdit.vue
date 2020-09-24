<template>

  <div style="padding : 0 5vw;">
    <div style="width:100%;">
        <div style="float:right;">
        <!-- <button class="btn btn-outline-pink" style="">전체선택</button> -->
        <button class="btn btn-outline-pink" style="margin-left:6px !important;">그룹추가</button>
      </div>
    </div>
    <v-app style="width:100%;">
      <v-expansion-panels focusable>
        <v-expansion-panel
          v-for="group in groups"
          :key="group"
        >
          <v-expansion-panel-header>{{group.name}}
            </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-list>

              <v-list-item
                v-for="member in group.members"
                :key="member"
                :inactive="inactive"
              >
            {{member.name}}</v-list-item>
            </v-list>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-app>
  </div>
</template>

<script>


export default {
  name: 'GroupEdit',
  data() {
    return {
      
      groups:[
        {
          name:"외가",
          members:[
            {name:"박지우"},
            {name:"박명환"},
            {name:"최미숙"},
          ]
        },
        {
          name:"친가",
          members:[
            {name:"김호준"},
            {name:"김명수"},
            {name:"이명자"},
          ]
        },
        {
          name:"지인",
          members:[
            {name:"박지우"},
            {name:"김명수"},
            {name:"손유리"},
          ]
        },
        {
          name:"지인2",
          members:[
            {name:"심연우"},
            {name:"박소정"},
            {name:"김권식"},
          ]
        },
      ]
    }
  },
}
</script>

<style scoped>

</style>