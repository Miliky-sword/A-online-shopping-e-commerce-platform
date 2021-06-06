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
    drawChart (data) {
      const myEchart = this.$echarts.init(document.getElementById('main'))
      const option = {
        title: {
          text: '折线图'
        },
        tooltip: {
          trigger: 'item', // 触发类型；轴触发，axis则鼠标hover到一条柱状图显示全部数据，item则鼠标hover到折线点显示相应数据，
          formatter: function (params) {
            return '当前温度为：' + params.data
          }
        },
        xAxis: {
          type: 'category'
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
          data: data,
          type: 'line',
          smooth: true,
          lineStyle: {
            color: 'blue'
          }
        }]
      }
      myEchart.setOption(option)
    }
  }

}
</script>

<style scoped>
#main {
  width: 600px;
  height: 400px;
  margin: auto;
  margin-top: 100px;
}
</style>
