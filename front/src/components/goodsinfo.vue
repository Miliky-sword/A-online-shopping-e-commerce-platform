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
          default-active="/goodsinfo"
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
        <!-- 图片占位 -->
        <el-carousel
          :interval="4000"
          type="card"
          height="200px"
        >
          <el-carousel-item
            v-for="item in imgArrag"
            :key="item"
          >
            <h3 class="medium">
              <el-image
                class="carousel-image"
                :src="item.path"
              />
            </h3>
          </el-carousel-item>
        </el-carousel>
        <!-- 商品参数栏 -->
        <el-table
          :data="tableData0"
          style="width: 700px"
          :show-header="false"
          class="table0"
        >
          <el-table-column
            prop="informationName"
            label="User's Name"
            width="200px"
          />
          <el-table-column
            prop="information"
            label="User"
            width="500px"
          />
        </el-table>
        <!-- 评分栏 -->
        <div class="block">
          <span class="demonstration">product scores</span>
          <el-rate
            v-model="value2"
            disabled
            show-score
            :colors="colors"
          /> There are {{ number }} people give scores for the product
        </div>
        <el-button
          type="primary"
          class="but1"
          @click="addToCart"
        >
          add to cart
        </el-button>
        <el-button
          type="success"
          class="but2"
          @click="createOrder"
        >
          buy now
        </el-button>
        <!-- 评价 -->
        <el-table
          :data="tableData1"
          height="200"
          border
          style="width: 1101px"
          class="table2"
        >
          <el-table-column
            prop="customerId"
            label="Customer Id"
            width="150px"
          />
          <el-table-column
            prop="neirong"
            label="comments"
            width="950px"
          />
        </el-table>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      tableData0: [{
        informationName: 'product Id',
        information: ''
      }, {
        informationName: 'product Name',
        information: ''
      }, {
        informationName: 'merchant Name',
        information: ''
      }, {
        informationName: 'price',
        information: ''
      }, {
        informationName: 'inventory',
        information: ''
      }, {
        informationName: 'date in product',
        information: ''
      }, {
        informationName: 'description',
        information: ''
      }],
      pid: 1,
      s: '',
      value: null,
      number: 0,
      iconClasses: ['icon-rate-face-1', 'icon-rate-face-2', 'icon-rate-face-3'], // 等同于 { 2: 'icon-rate-face-1', 4: { value: 'icon-rate-face-2', excluded: true }, 5: 'icon-rate-face-3' }
      tableData1: [],
      imgArrag: [],
      value2: null,
      colors: ['#99A9BF', '#F7BA2A', '#FF9900']
    }
  },
  created () {
    if (this.$session.get('username') === '' || this.$session.get('username') === null || this.$session.get('username') === undefined) {
      return this.$router.push('/login')
    }
    this.pid = this.$session.get('productId')
    this.loadproductdetail()
    this.loadcomment()
    this.loadpic()
  },
  methods: {
    logout () {
      this.$session.set('username', '')
      this.$session.set('userType', '')
      this.$router.push('/login')
    },
    goBack () {
      console.log('go back')
    },
    loadcomment () {
      this.$http.post('product/loadcomment/', {
        pid: this.pid
      }).then(response => {
        console.log(response.data.data.dataArray)
        this.tableData1 = response.data.data.dataArray
        console.log('222')
        console.log(this.tableData1)
      }, response => {
        console.log('error')
        this.$message.error('failed to load comments')
      })
    },
    loadpic () {
      this.$http.post('product/loadPic/', {
        pid: this.pid
      }).then(response => {
        console.log('pic imagarrag')
        console.log(response.data.data.dataArray)
        this.imgArrag = response.data.data.dataArray
        this.imgArrag.forEach(element => {
          this.s = ''
          this.s = element.path
          element.path = 'http://127.0.0.1:8000/static/media/' + this.s
        })
      })
      console.log(this.imgArrag)
      console.log('333')
    },
    loadproductdetail () {
      this.$http.post('product/getProductInfo/', {
        pid: this.pid
      }).then(response => {
        console.log(response.data.data.dataArray)
        this.tableData0[0].information = response.data.data.dataArray[0].id
        this.tableData0[1].information = response.data.data.dataArray[0].productName
        this.tableData0[2].information = response.data.data.dataArray[0].merchantName
        this.tableData0[3].information = response.data.data.dataArray[0].price
        this.tableData0[4].information = response.data.data.dataArray[0].inventory
        this.tableData0[5].information = response.data.data.dataArray[0].dateInProduction
        this.tableData0[6].information = response.data.data.dataArray[0].briefDescription
        this.value2 = response.data.data.dataArray[0].stars
        this.number = response.data.data.dataArray[0].starsNumber
        this.tableData.forEach(element => {
          this.s = ''
          this.s = element.imageUrl
          element.imageUrl = 'http://127.0.0.1:8000/static/media/' + this.s
        })
        this.$message.success('load products success！')
      }, response => {
        console.log('error')
        this.$message.error('failed to load products')
      })
    },
    addToCart () {
      this.$http.post('cart/addaproducttoshoppingcart/', {
        username: this.$session.get('username'),
        productName: this.tableData0[1].information,
        merchantName: this.tableData0[2].information,
        price: this.tableData0[3].information,
        inventory: 1
      }).then(response => {
        // console.log(response.data)
        this.resp = response.data
        console.log(this.resp.msg)
        if (this.resp.status === 200) {
          this.$message.success('Added product successfully！')
          this.loadSearchProduct('')
        } else {
          this.$message.error('Failed to add the product！')
        }
      }, response => {
        console.log('error')
        this.$message.error('Failed to add the product！')
      })
    },
    createOrder () {
      this.$http.post('order/createorder/', {
        username: this.$session.get('username'),
        productName: this.tableData0[1].information,
        productId: this.tableData0[0].information,
        merchantName: this.tableData0[2].information,
        totalprice: this.tableData0[3].information,
        inventory: 1
      }).then(response => {
        if (response.data.status === 200) {
          this.$message.success('create order successfully！')
        } else {
          this.$message.error('Failed to create the order！')
        }
      }, response => {
        console.log('error')
        this.$message.error('Failed to create the order！')
      })
    },
    columnStyle ({ row, column, rowIndex, columnIndex }) {
      if (columnIndex === 0) {
        return 'background:rgb (243, 243, 243) ; font-weight:600'
      } else {
        return 'background: ffffff;'
      }
    },
    // 和并列
    objectSpanMethod ({ row, column, rowIndex, columnIndex }) {
      if (columnIndex === 0) {
        return {
          rowspan: 1,
          colspan: 1
        }
      }
    }
  }
}
</script>

<style scoped>
.table0 {
    position: absolute;
    top: 45%;
    left: 18%;
}

.table2 {
  position: absolute;
  left: 18%;
  top: 100%;
}

.block {
  position: absolute;
  left: 18%;
  top: 85%;
}

.but1 {
  position: absolute;
  left: 70%;
  top: 85%;
}

.but2 {
  position: absolute;
  left: 78%;
  top: 85%;
}

.home-container {
    height: 100%;
}

.el-carousel__item h3 {
    color: #fff;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
.carousel-image {
  width: 200px;
  height: 200px;
}

  .el-carousel__item:nth-child(2n) {
    background-color: transparent;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: transparent;
  }

.el-header {
    background: #444356;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #dbdae4;
    size: 20px;
}

.el-aside {
    background: #333744;
}

.el-main {
    background: #EAEDF1;
}

.toggle-button{
    background: #4A5064;
    font-size: 10px;
    line-height: 24px;
    color: #fff;
    text-align: center;
    cursor: pointer;
}

.demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>
