<template>
  <div class="container">
    <h5 class="main-title text-center color-pink">{{currentBaby.baby_name}}의 머리둘레 기록</h5>
    <line-graph :chart-data="chartdata" :options="options"></line-graph>
    <v-simple-table class="mt-3">
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">
              날짜
            </th>
            <th class="text-center">
              머리둘레 (cm)
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="measurement in headMeasurementList"
            :key="measurement.x"
          >
            <td>{{ measurement.x }}</td>
            <td class="text-center">{{ measurement.y }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
    <div class="footer"></div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import LineGraph from './LineGraph.js'

export default {
  name: 'HeadMeasurement',

  components: {
    LineGraph,
  },

  data() {
    return {
      chartdata: {},
      options: null,

    }
  },

  computed: {
    ...mapState(['myaccount', 'currentBaby']),
    ...mapState('measurementStore', ['headMeasurementList', ])
  },

  watch: {
    headMeasurementList() {
      this.fillData()
    },
  },

  methods: {
    ...mapActions('measurementStore', ['fetchHeadMeasurementList',]),

    fillData() {
      this.chartdata = {
        datasets: [
          {
            label: '머리둘레',
            backgroundColor: 'rgba(225, 200, 234, 0.6)',
            borderColor: 'rgba(225, 200, 234, 1)',
            data: this.headMeasurementList
          }
        ]
      }

      this.options = {
        scales: {
          xAxes: [
            {
              type: "time",
              time: {
                unit: 'quarter',
                displayFormats: {
                    quarter: 'YYYY.MM'
                }
              },
              gridLines: {
                display: false,
              },
            },
          ],
          yAxes: [
            {
              bounds: 'ticks',
            }
          ]
        },
        responsive: true,
        maintainAspectRatio: true,
        legend: {
          display: false,
        },
      }

    },
  },

  created() {
    this.fetchHeadMeasurementList()
  },

  mounted(){
    this.fillData()
  },
}
</script>

<style scoped>
  .footer {
    height: 100px;
  }
</style>