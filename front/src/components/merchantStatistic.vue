<template>
  <el-container class="home-container">
    <!-- 头部区域 -->
    <el-header>
      <div>
        <span>Welcome to the online shopping e-commerce platform -- Merchant</span>
      </div>
      <el-button
        type="info"
        @click="logout"
      >
        log out
      </el-button>
    </el-header>
    <!-- 页面主体区域 -->
    <el-container>
      <!-- 侧边栏 -->
      <el-header
        class="menu-aside"
        width="250px"
      >
        <el-menu
          class="menu"
          background-color="#333744"
          text-color="#fff"
          active-text-color="#66ccff"
          default-active="/merchantStatistic"
          router
          mode="horizontal"
        >
          <el-menu-item
            index="/merchantManage"
            router
          >
            <template slot="title">
              <i class="el-icon-s-goods" />
              <span>products on the shelves</span>
            </template>
          </el-menu-item>
          <el-menu-item index="/merchantOrder">
            <template slot="title">
              <i class="el-icon-s-order" />
              <span>My order</span>
            </template>
          </el-menu-item>
          <el-menu-item
            index="/merchantStatistic"
          >
            <template slot="title">
              <i class="el-icon-user-solid" />
              <span>statistic the sales</span>
            </template>
          </el-menu-item>
          <el-menu-item
            index="/merchantStatisticProfit"
          >
            <template slot="title">
              <i class="el-icon-user-solid" />
              <span>statistic the profit</span>
            </template>
          </el-menu-item>
          <el-menu-item
            index="/merchantuserinfo"
          >
            <template slot="title">
              <i class="el-icon-user-solid" />
              <span>User center</span>
            </template>
          </el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
        <div class="EchartPractice">
          <div>
            <div style="margin: 40px;" />
            <el-row>
              <el-col
                :span="6"
                :offset="6"
              >
                <el-select
                  v-model="value"
                  placeholder="Please select a product"
                  @change="loadsalesdata()"
                  @blur="loadsalesdata()"
                >
                  <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  />
                </el-select>
              </el-col>
              <el-col :span="4">
                <el-date-picker
                  v-model="days"
                  type="daterange"
                  range-separator="~"
                  start-placeholder="date start"
                  end-placeholder="date end"
                  @change="loadsalesdata()"
                  @blur="loadsalesdata()"
                />
              </el-col>
            </el-row>
          </div>
          <Echart
            ref="tb"
          />
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import Echart from './self-components/echart.vue'
export default {
  name: 'EchartPractice',
  components: {
    Echart
  },
  data () {
    return {
      src: '',
      productList: [],
      days: ['2021-05-15', '2021-06-15'],
      valueY: [],
      labelX: [],
      interval: 0,
      options: [],
      value: 'all'
    }
  },
  mounted () {
    // 因为要实现点击不能的数据渲染不同的列表，所以需要通过调用组件的ref去找组件里面的渲染方法，然后让网页去重新去渲染数据
    this.$refs.tb.drawChart(this.valueY, this.labelX, this.interval)
    console.log('mount end')
  },
  created () {
    if (this.$session.get('username') === '' || this.$session.get('username') === null || this.$session.get('username') === undefined) {
      return this.$router.push('/login')
    }
    this.loadAllProduct()
    this.loadsalesdata()
  },
  methods: {
    logout () {
      this.$session.set('username', '')
      this.$session.set('userType', '')
      this.$router.push('/login')
    },
    loadAllProduct () {
      this.options = [{
        item: 'all',
        value: 'all'
      }]
      this.$http.post('product/getProduct/', {
        isAll: 0,
        merchantName: this.$session.get('username')
      }).then(response => {
        response.data.data.dataArray.forEach(element => {
          this.options.push({
            item: element.productName,
            value: element.productName
          })
        })
      }, response => {
        console.log('error')
      })
    },
    loadsalesdata () {
      this.$http.post('order/loadSalesData/', {
        value: this.value,
        merchantName: this.$session.get('username'),
        startdate: this.days[0],
        enddate: this.days[1]
      }).then(response => {
        this.valueY = response.data.valueY
        this.labelX = response.data.labelX
        this.interval = response.data.interval
        this.drawChart(this.valueY, this.labelX, this.interval, this.value + ' sales chart')
      })
    },
    drawChart (valueY, labelX, interval) {
      this.$refs.tb.drawChart(valueY, labelX, interval, this.value + ' sales chart')
    },
    loadsrc (command) {
      this.$http.post('order/statistic/', {
        class: 1,
        name: command
      }).then(response => {
        this.src = 'http://47.108.209.135:8080/static/statistic/' + response.data.src
        console.log(this.src)
      })
    }
  }
}
</script>

<style scoped>
  .home-container {
    height: 100%;
}
.el-header {
    background: #444356;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #dbdae4;
    size: 20px;
}
  .el-dropdown-link {
    cursor: pointer;
    color: #409EFF;
  }
  .el-icon-arrow-down {
    font-size: 12px;
  }
  .dropdown {
      position: absolute;
      left: 25%;
      top: 20%;
  }
  .block {
      height: 530px;
      width: 530px;
      position: absolute;
      left: 20%;
      top: 29%;
  }
</style>
