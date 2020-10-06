<template>
  <div class="container">
    <h5 class="main-title text-center color-pink">{{currentBaby.baby_name}}의 몸무게 기록</h5>
    <line-graph :chart-data="chartdata" :options="options"></line-graph>
    <!-- <p>{{ weightMeasurementList }}</p> -->
    <v-simple-table class="mt-3">
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">
              날짜
            </th>
            <th class="text-center">
              몸무게 (kg)
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="measurement in weightMeasurementList"
            :key="measurement.x"
          >
            <td class="text-left">{{ measurement.x }}</td>
            <td class="text-center">{{ measurement.y }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>

    <div class="footer"></div>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import LineGraph from './LineGraph.js'

export default {
  name: 'WeightMeasurement',

  components: {
    LineGraph,
  },

  data() {
    return {
      chartdata: {},
      options: null,
      headers: [
        {
          text: '날짜',
          value: 'x'
        },
        {
          text: '몸무게',
          value: 'y'
        }
      ]
    }
  },

  computed: {
    ...mapState(['myaccount', 'currentBaby']),
    ...mapState('measurementStore', ['weightMeasurementList', ]),
    ...mapGetters('measurementStore', ['weightMeasurementFetched'])
  },

  watch: {
    weightMeasurementList() {
      this.fillData()
    },
  },

  methods: {
    ...mapActions('measurementStore', ['fetchWeightMeasurementList',]),

    fillData() {
      this.chartdata = {
        datasets: [
          {
            label: '몸무게',
            backgroundColor: 'rgba(155, 199, 255, 0.6)',
            borderColor: 'rgba(155, 199, 255, 1)',
            data: this.weightMeasurementList,
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
    this.fetchWeightMeasurementList()
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