<template>
  <div>
    <h5 v-if="currentBaby" class="main-title text-center color-pink">{{currentBaby.baby_name}}의 캘린더</h5>
    <div class="p-3">
      <vc-calendar
        :attributes='attributes'
        is-expanded
        :max-date="new Date()"
        locale="ko-kr"
      >
        <div
          slot="day-popover"
          slot-scope="{ day, dayTitle, attributes }">
          <div class="text-xs text-gray-300 font-semibold text-center">
            {{ dayTitle }}
          </div>
          <popover-row
            v-for="attr in attributes"
            :key="attr.id"
            :attribute="attr"
          >
            <div class="pointer" v-if="attr.customData.id" @click="clickDiary(attr.customData.id)">{{ attr.customData.title }}</div>
            <div v-else>{{ attr.customData.title }}</div>
          </popover-row>
        </div>
      </vc-calendar>
    </div>
  </div>
</template>

<script>
import PopoverRow from 'v-calendar/lib/components/popover-row.umd.min'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'DiaryCalendar',
  components: {
    PopoverRow,
  },
  data() {
    return {
    }
  },
  computed: {
    ...mapState([ 'myaccount', 'currentBaby']),
    ...mapState( 'diaryStore', ['diaries', 'measurements']),
    attributes() {
      if (this.diaries && this.measurements) {
        const diaryData = []
        for (var diary of this.diaries) {
          let inputData = {
            dates: diary.diary_date,
            dot: {
              color: 'green',
              class: diary.isComplete ? 'opacity-75' : '',
            },
            popover: {
              label: diary.description,
              visibility: 'focus',
              placement: 'auto'
            },
            customData: {
              title: diary.title,
              id: diary.id
            },
          }
          diaryData.push(inputData)
        }
        for (var measurement of this.measurements) {
          let customData = {}
          customData.title = ''
          if (measurement.height) {
            customData.title = customData.title + '키: ' + measurement.height + '\n'
          }
          if (measurement.weight) {
            customData.title = customData.title + ' 체중: ' + measurement.weight + '\n'
          }
          if (measurement.head_size) {
            customData.title = customData.title + ' 머리둘레: ' + measurement.head_size
          }
          let inputData = {
            dates: measurement.measure_date,
            dot: {
              color: 'pink',
              class: diary.isComplete ? 'opacity-75' : '',
            },
            popover: {
              label: measurement.description,
              visibility: 'focus',
              placement: 'auto'
            },
            customData: customData,
          }
          diaryData.push(inputData)
        }
        return diaryData
      } else {
        return []
      }
    },
  },
  methods: {
    ...mapActions( 'diaryStore', ['fetchDiaries', 'fetchMeasurements']),
    clickDiary(diaryId) {
      console.log(diaryId)
      this.$router.push({ name: 'DiaryDetail', params: {diaryId: diaryId} })
    }
  },
  created() {
    this.fetchDiaries()
    this.fetchMeasurements()
  }

}
</script>

<style scoped>
.crying-baby {
  height: 50vh;
  width: auto;
}

.main-title {
  font-weight: 900;
  font-size: 1.3rem;
}
</style>