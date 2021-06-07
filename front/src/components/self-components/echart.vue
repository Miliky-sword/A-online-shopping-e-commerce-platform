<template>
  <div id="main" />
</template>

<script>
export default {
  name: 'EchartPractice',
  data () {
    return {

    }
  },
  methods: {
    drawChart (valueY, labelX, interval = 0, title = 'line chart') {
      this.$echarts.dispose(document.getElementById('main'))
      const myEchart = this.$echarts.init(document.getElementById('main'))
      const option = {
        title: {
          text: title
        },
        tooltip: {
          trigger: 'item', // 触发类型；轴触发，axis则鼠标hover到一条柱状图显示全部数据，item则鼠标hover到折线点显示相应数据，
          formatter: function (params) {
            return params.data
          }
        },
        xAxis: {
          type: 'category',
          data: labelX,
          axisLabel: { interval: interval }
        },
        yAxis: {
          type: 'value',
          splitLine: {
            show: true,
            lineStyle: {
              type: 'dashed'
            }
          }
        },
        series: [{
          data: valueY,
          type: 'line',
          smooth: true,
          lineStyle: {
            color: 'black'
          },
          itemStyle: { normal: { label: { show: true } } }
        }]
      }
      myEchart.setOption(option)
    }
  }

}
</script>

<style scoped>
#main {
  width: 1400px;
  height: 600px;
  margin: auto;
  margin-top: 50px;
}
</style>
