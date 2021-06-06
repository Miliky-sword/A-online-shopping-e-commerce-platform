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
            <el-row>
              <el-col :span="12">
                <el-button @click="drawChart(data1)">
                  data1
                </el-button>
                <el-button @click="drawChart(data2)">
                  data2
                </el-button>
                <el-button @click="drawChart(data3)">
                  data3
                </el-button>
                <el-button @click="drawChart(data4)">
                  data4
                </el-button>
              </el-col>
              <el-col :span="12">
                <el-date-picker
                  v-model="days"
                  type="daterange"
                  range-separator="~"
                  start-placeholder="开始日期"
                  end-placeholder="结束日期"
                />
              </el-col>
            </el-row>
          </div>
          <echarts ref="tb" />
        </div>
        <el-dropdown
          class="dropdown"
          @command="loadsrc"
        >
          <el-button type="primary">
            select a product to show its sales in 30 days<i class="el-icon-arrow-down el-icon--right" />
          </el-button>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item
              v-for="item in productList"
              :key="item.productName"
              :command="item.productName"
            >
              {{ item.productName }}
            </el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        <div class="demo-image__placeholder">
          <div class="block">
            <span class="demonstration" />
            <el-image
              style="width: 900px; height: 400px"
              :src="src"
            />
          </div>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import echarts from '../components/self-components/echart.vue'
export default {
  name: 'EchartPractice',
  components: {
    echarts
  },
  data () {
    return {
      src: '',
      productList: [],
      days: ['2020-01-01', '2021-03-03'],
      data1: [20, 30, 32, 11, 22, 20, 15, 25, 35, 14],
      data2: [40, 10, 15, 21, 30, 20, 12, 15, 15, 31],
      data3: [30, 35, 21, 12, 20, 25, 14, 35, 23, 13],
      data4: [20, 23, 15, 31, 30, 30, 35, 22, 19, 24]
    }
  },
  mounted () {
    // 因为要实现点击不能的数据渲染不同的列表，所以需要通过调用组件的ref去找组件里面的渲染方法，然后让网页去重新去渲染数据
    this.$refs.tb.drawChart(this.data1)
  },
  created () {
    if (this.$session.get('username') === '') {
      return this.$router.push('/login')
    }
    this.loadAllProduct()
    this.$refs.tb.drawChart(this.data1)
  },
  methods: {
    logout () {
      this.$session.set('username', '')
      this.$session.set('userType', '')
      this.$router.push('/login')
    },
    loadAllProduct () {
      this.$http.post('product/getProduct/', {
        isAll: 0,
        merchantName: this.$session.get('username')
      }).then(response => {
        this.productList = response.data.data.dataArray
      }, response => {
        console.log('error')
      })
    },
    drawChart (index) {
      this.$refs.tb.drawChart(index)
    },
    loadsrc (command) {
      this.$http.post('order/statistic/', {
        class: 1,
        name: command
      }).then(response => {
        this.src = 'http://127.0.0.1:8000/static/statistic/' + response.data.src
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
