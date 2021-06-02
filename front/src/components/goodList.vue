<template>
  <el-container class="home-container">
    <!-- 头部区域 -->
    <el-header>
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
    <!-- 页面主体区域 -->
    <el-container>
      <el-header class="customer-menu">
        <el-menu
          class="menu"
          background-color="#333744"
          text-color="#fff"
          active-text-color="#66ccff"
          default-active="/goodList"
          router
          mode="horizontal"
        >
          <el-menu-item index="/goodList">
            <template slot="title">
              <i class="el-icon-s-goods" />
              <span>browse all the products</span>
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
            index="5"
            disabled
          >
            <template slot="title">
              <i class="el-icon-user-solid" />
              <span>User center</span>
            </template>
          </el-menu-item>
        </el-menu>
      </el-header>
      <!-- 右侧主体内容 -->
      <el-main>
        <!-- 商品图片 -->
        <!-- <img class="goods1" src="../assets/goods1.png" alt="">
          <img class="goods2" src="../assets/goods2.png" alt=""> -->
        <!-- 商品基础信息表单 -->
        <template>
          <el-table
            :data="tableData"
            style="width: 100%"
          >
            <el-table-column type="expand">
              <template slot-scope="props">
                <el-form
                  label-position="left"
                  inline
                  class="demo-table-expand"
                >
                  <div>
                    <el-form-item label-position="top">
                      <el-image
                        :src="props.row.imageUrl"
                        style="width: 100px; height: 100px"
                      />
                    </el-form-item>
                  </div>
                  <el-form-item label="Product id:  ">
                    <span>{{ props.row.id }}</span>
                  </el-form-item>
                  <el-form-item label="Merchant name:  ">
                    <span>{{ props.row.merchantName }}</span>
                  </el-form-item>
                  <el-form-item label="Date in production：  ">
                    <span>{{ props.row.dateInProduction }}</span>
                  </el-form-item>
                  <el-form-item label="Description：  ">
                    <span>{{ props.row.briefDescription }}</span>
                  </el-form-item>
                </el-form>
              </template>
            </el-table-column>
            <el-table-column
              label="Product Name"
              prop="productName"
            />
            <el-table-column
              label="Inventory"
              prop="inventory"
            />
            <el-table-column
              label="Price"
              prop="price"
            />
            <el-table-column
              label="operation"
              disabled
            >
              <template slot-scope="scope">
                <el-button
                  type="primary"
                  icon="el-icon-edit"
                  size="mini"
                  circle
                  @click="addToCart(scope.row)"
                >
                  add to cart
                </el-button>
                <el-button
                  type="warning"
                  icon="el-icon-setting"
                  size="mini"
                  circle
                  @click="createOrder(scope.row)"
                >
                  buy now
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </template>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      tableData: [],
      s: ''
    }
  },
  created () {
    if (this.$session.get('username') === '') {
      return this.$router.push('/login')
    }
    this.loadAllProduct()
  },
  methods: {
    logout () {
      this.$session.set('username', '')
      this.$session.set('userType', '')
      this.$router.push('/login')
    },
    loadAllProduct () {
      this.$http.get('product/getAvailableProduct/').then(response => {
        console.log(response.data.data.dataArray)
        this.tableData = response.data.data.dataArray
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
    addToCart (row) {
      this.$http.post('cart/addaproducttoshoppingcart/', {
        username: this.$session.get('username'),
        productName: row.productName,
        merchantName: row.merchantName,
        price: row.price,
        inventory: 1
      }).then(response => {
        // console.log(response.data)
        this.resp = response.data
        console.log(this.resp.msg)
        if (this.resp.status === 200) {
          this.$message.success('Added product successfully！')
          this.addProductDialogVisible = false
          this.loadAllProduct()
        } else {
          this.$message.error('Failed to add the product！')
        }
      }, response => {
        console.log('error')
        this.$message.error('Failed to add the product！')
      })
    },
    createOrder (row) {
      this.$http.post('order/createorder/', {
        username: this.$session.get('username'),
        productName: row.productName,
        productId: row.id,
        merchantName: row.merchantName,
        totalprice: row.price,
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
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>
.home-container {
    height: 100%;
    background: #444356;
}

.el-header {
    background: #444356;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #dbdae4;
    size: 20px;
}

.menu {
    background: #333744;
}

.el-main {
    background: #EAEDF1;
    height:100%;
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
