<template>
  <el-container class="home-container">
    <!-- 头部区域 -->
    <el-header>
      <div>
        <span>Welcome to the online shopping e-commerce platform -- Manager</span>
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
          default-active="/managerStatisticmer"
          router
          mode="horizontal"
        >
          <el-menu-item
            index="/manage"
            router
          >
            <template slot="title">
              <i class="el-icon-s-goods" />
              <span>user list</span>
            </template>
          </el-menu-item>
          <el-menu-item index="/managerStatisticmer">
            <template slot="title">
              <i class="el-icon-s-order" />
              <span>Merchants' sales</span>
            </template>
          </el-menu-item>
          <el-menu-item
            index="/manageruserinfo"
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
      value: 'merchant'
    }
  },
  created () {
    if (this.$session.get('username') === '' || this.$session.get('username') === null || this.$session.get('username') === undefined) {
      return this.$router.push('/login')
    }
    this.loadAllMerchant()
    this.loadsalesdata()
  },
  methods: {
    logout () {
      this.$session.set('username', '')
      this.$session.set('userType', '')
      this.$router.push('/login')
    },
    loadAllMerchant () {
      this.$http.post('user/getMerchant/', {}).then(response => {
        response.data.data.dataArray.forEach(element => {
          this.options.push({
            item: element.username,
            value: element.username
          })
        })
      }, response => {
        console.log('error')
      })
    },
    loadsalesdata () {
      this.$http.post('order/loadSalesData/', {
        value: 'all',
        merchantName: this.value,
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
