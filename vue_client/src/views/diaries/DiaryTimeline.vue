<template>
  <div>
    <h5 v-if="currentBaby" class="main-title text-center color-pink">{{currentBaby.baby_name}}의 타임라인</h5>
    <div v-if="diaries">
      <div v-if="diaries.length">
        <v-timeline
          align-top
          dense
        >
          <div v-for="(diary, idx) in diaries" :key="diary.id">
            <v-timeline-item
              :color="pickColor(idx)"
              small
            >
              <v-row class="pt-0 no-gutters">
                <v-col cols="2" class="p-0">
                  <strong>{{diary.diary_date | moment("MM월 DD일")}}</strong>
                </v-col>
                <v-col cols="10" class="p-0">
                  <strong class="pointer" @click="clickDiary(diary.id)">{{diary.title}}</strong>
                  <div class="caption">by {{diary.creator.name }} ({{diary.relationship_name}})</div>
                  <div class="image-container" v-if="diary.cover_photo">
                    <img 
                      class="mt-3 pointer"
                      @click="clickDiary(diary.id)" 
                      :src="diary.cover_photo">
                  </div>
                  
                </v-col>
              </v-row>
            </v-timeline-item>
          </div>
          <div style="height: 15vh"></div>
        </v-timeline>
      </div>
      <div v-else>
        <div class="text-center mt-5">
          <img class="crying-baby" src="@/assets/baby.png">
          <h5>
            작성된 다이어리가 아직 없습니다.<br>
            + 버튼을 눌러 다이어리를 작성해주세요!
          </h5>
        </div>
      </div>
    </div>

  </div>

</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'DiaryTimeline',
  data() {
    return {  
      colors: ['#B9E1C3', '#FEA59C', '#9BC7FF', '#E1C8EA' ]
    }
  },
  computed: {
    ...mapState([ 'myaccount', 'currentBaby']),
    ...mapState( 'diaryStore', ['diaries']),
    
  },
  methods: {
    ...mapActions( 'diaryStore', ['fetchDiaries']),
    clickDiary(diaryId) {
      this.$router.push({ name: 'DiaryDetail', params: { diaryId: diaryId}})
    },
    pickColor(idx) {
      var color = idx % 4
      return this.colors[color]
    }
  },
  created() {
    this.fetchDiaries()
  }
}
</script>

<style scoped>
.main-title {
  font-weight: 900;
  font-size: 1.3rem;
}

.image-container img {
  max-width: 50%;
}

.crying-baby {
  height: auto;
  width: 50vw;
}
</style>