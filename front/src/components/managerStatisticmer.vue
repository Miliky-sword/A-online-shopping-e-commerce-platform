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
              :key="item.username"
              :command="item.username"
            >
              {{ item.username }}
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
export default {
  data () {
    return {
      src: '',
      productList: []
    }
  },
  created () {
    if (this.$session.get('username') === '') {
      return this.$router.push('/login')
    }
    this.loadAllMerchant()
  },
  methods: {
    logout () {
      this.$session.set('username', '')
      this.$session.set('userType', '')
      this.$router.push('/login')
    },
    loadAllMerchant () {
      this.$http.post('user/getMerchant/', {}).then(response => {
        this.productList = response.data.data.dataArray
      }, response => {
        console.log('error')
      })
    },
    loadsrc (command) {
      this.$http.post('order/statistic/', {
        class: 0,
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
