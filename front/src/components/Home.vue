<template>
  <el-container class="home-container">
    <el-header class="header">
      <div>
        <span>welcome to the e-commerce platform</span>
      </div>
      <el-button
        type="info"
        @click="logout"
      >
        log out
      </el-button>
    </el-header>
    <el-container class="main-container">
      <el-header class="customer-menu">
        <el-menu
          class="menu"
          background-color="#333744"
          text-color="#fff"
          active-text-color="#66ccff"
          default-active="/Home"
          router
          mode="horizontal"
        >
          <el-menu-item index="/Home">
            <template slot="title">
              <i class="el-icon-s-goods" />
              <span>Home Page</span>
            </template>
          </el-menu-item>
          <el-menu-item
            index="/customerSearch"
          >
            <template slot="title">
              <i class="el-icon-s-goods" />
              <span>serach products</span>
            </template>
          </el-menu-item>
          <el-menu-item
            index="/goodsinfo"
          >
            <template slot="title">
              <i class="el-icon-s-goods" />
              <span>product info</span>
            </template>
          </el-menu-item>
          <el-menu-item index="/customerShoppingCart">
            <template slot="title">
              <i class="el-icon-shopping-cart-2" />
              <span>shopping cart</span>
            </template>
          </el-menu-item>
          <el-menu-item index="/customerOrder">
            <template slot="title">
              <i class="el-icon-s-order" />
              <span>My order</span>
            </template>
          </el-menu-item>
          <el-menu-item
            index="/customeruserinfo"
          >
            <template slot="title">
              <i class="el-icon-user-solid" />
              <span>User center</span>
            </template>
          </el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
        <!-- 走马灯 -->
        <el-carousel
          :interval="4000"
          type="card"
          height="400px"
        >
          <el-carousel-item
            v-for="item in imgArrag"
            :key="item"
          >
            <el-image
              class="image"
              :src="item"
            />
          </el-carousel-item>
        </el-carousel>
        <!-- 左侧图片 -->
        <div class="demo-image__placeholder">
          <div class="block">
            <span class="demonstration" />
            <el-image :src="src" />
          </div>
        </div>
        <div class="demo-image__placeholder1">
          <div class="block1">
            <el-image :src="src1" />
            <el-button
              @click="to1"
            >
              T-shirt
            </el-button>
          </div>
        </div>
        <div class="demo-image__placeholder2">
          <div class="block2">
            <el-image :src="src2" />
            <el-button
              @click="to2"
            >
              Chocolate
            </el-button>
          </div>
        </div>
        <div class="demo-image__placeholder3">
          <div class="block3">
            <el-image :src="src3" /><el-button
              @click="to3"
            >
              Ice-cream
            </el-button>
          </div>
        </div>
        <div class="demo-image__placeholder4">
          <div class="block4">
            <el-image :src="src4" /><el-button
              @click="to4"
            >
              Xbox controller
            </el-button>
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
      imgArrag: ['http://127.0.0.1:8000/static/img/AFDASUIFYIUSH.png',
        'http://127.0.0.1:8000/static/img/DJFHIAJSDFHAI.png',
        'http://127.0.0.1:8000/static/img/JKSGFIDSGF.png'],
      src: 'http://127.0.0.1:8000/static/img/5U5A8PZRU3MG74U39.png',
      src1: 'http://127.0.0.1:8000/static/img/332D411812F39C814643202395D9DA54.png',
      src2: 'http://127.0.0.1:8000/static/img/06653B43885010CB4CF9480C9F39D182.png',
      src3: 'http://127.0.0.1:8000/static/img/B3974829BCAA82437F442560A83A1C9A.png',
      src4: 'http://127.0.0.1:8000/static/img/339CD628D63E4778456A80B7DECBC2DF.png'
    }
  },
  created () {
    if (this.$session.get('username') === '' || this.$session.get('username') === null || this.$session.get('username') === undefined) {
      return this.$router.push('/login')
    }
  },
  methods: {
    logout () {
      this.$session.set('username', '')
      this.$session.set('userType', '')
      this.$router.push('/login')
    },
    to1 () {
      this.$session.set('productId', 10)
      this.$router.push('/goodsinfo')
    },
    to2 () {
      this.$session.set('productId', 9)
      this.$router.push('/goodsinfo')
    },
    to3 () {
      this.$session.set('productId', 7)
      this.$router.push('/goodsinfo')
    },
    to4 () {
      this.$session.set('productId', 8)
      this.$router.push('/goodsinfo')
    }
  }
}
</script>

<style scoped>
.el-carousel__item h3 {
    text-align: center;
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }

  .home-container {
    height: 100%;
}

.block {
  position: absolute;
  left: 5%;
  top: 65%;
  width: 400px;
  height: 400px;
}

.block1 {
  position: absolute;
  left: 35%;
  top: 65%;
  text-align: center;
  width: 300px;
  height: 300px;
}

.block2 {
  position: absolute;
  left: 67%;
  top: 65%;
  text-align: center;
  width: 300px;
  height: 300px;
}

.block3 {
  position: absolute;
  left: 35%;
  top: 105%;
  text-align: center;
  width: 300px;
  height: 300px;
}

.block4 {
  position: absolute;
  left: 67%;
  top: 105%;
  text-align: center;
  width: 300px;
  height: 300px;
}

.image {
  height: 400px;
  width: 900px;
  flex: auto;
  text-align: center;
}
.el-header {
    background: #444356;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #dbdae4;
    size: 20px;
}

  .el-carousel__item:nth-child(2n) {
    background-color:transparent;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color:transparent;
  }
</style>
