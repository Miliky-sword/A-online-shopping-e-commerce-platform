<template>
    <el-container class="home-container">
  <el-header class="header">
      <div>
            <span>welcome to the e-commerce platform</span>
        </div>
        <el-button type="info" @click="logout">log out</el-button>
    </el-header>
  <el-container class="main-container">
      <el-header class="customer-menu">
          <el-menu class="menu" background-color="#333744" text-color="#fff" active-text-color="#66ccff" default-active="/customerShoppingCart"
          router  mode="horizontal">
            <el-menu-item index="/goodList">
              <template slot="title">
                <i class="el-icon-s-goods"></i>
                <span>browse all the products</span>
              </template>
            </el-menu-item>
            <el-menu-item index="2" disabled>
              <template slot="title">
                <i class="el-icon-s-goods"></i>
                <span>serach products</span>
              </template>
            </el-menu-item>
            <el-menu-item index="/customerShoppingCart">
              <template slot="title">
                <i class="el-icon-shopping-cart-2"></i>
                <span>shopping cart</span>
              </template>
            </el-menu-item>
            <el-menu-item index="/customerOrder">
              <template slot="title">
                <i class="el-icon-s-order"></i>
                <span>My order</span>
              </template>
            </el-menu-item>
            <el-menu-item index="5" disabled>
              <template slot="title">
                <i class="el-icon-user-solid"></i>
                <span>User center</span>
              </template>
            </el-menu-item>
        </el-menu>
      </el-header>
    <el-main class="main">
        <el-table :data="this.cartTableData" border stripe>
        <!-- stripe: 斑马条纹  border：边框-->
        <el-table-column prop="productName" label="ProductName"></el-table-column>
        <el-table-column prop="productName" label="productName"></el-table-column>
        <el-table-column prop="price" label="price"></el-table-column>
        <el-table-column prop="inventory" label="inventory"></el-table-column>
        <el-table-column label="operation">
          <template slot-scope="scope">
            <el-button
              type="primary"
              icon="el-icon-edit"
              size="mini"
              @click="delFromCart(scope.row)"
            >del from cart</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-button type="info" @click="createallorder">submit</el-button>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      cartTableData: []
    }
  },
  created () {
    if (this.$session.get.username === '') {
      return this.$router.push('/login')
    }
    this.loadAllinCart()
  },
  methods: {
    logout () {
      this.$session.set('username', '')
      this.$session.set('userType', '')
      this.$router.push('/login')
    },
    loadAllinCart () {
      this.$http.post('cart/allproductsofshoppingcart/', {
        username: this.$session.get('username')
      }).then(response => {
        console.log(response.data.data.dataArray)
        this.cartTableData = response.data.data.dataArray
        this.$message.success('load products success！')
      }, response => {
        console.log('error')
        this.$message.error('failed to load products')
      })
    },
    delFromCart (row) {
      this.$http.post('cart/removeaproductfromshoppingcart/', {
        username: this.$session.get('username'),
        merchantName: row.merchantName,
        productName: row.productName
      }).then(response => {
        console.log(response.data.msg)
        this.$message.success('del products success！')
        this.loadAllinCart()
      }, response => {
        console.log('error')
        this.$message.error('failed to del products')
      })
    },
    createallorder () {
      console.log(this.cartTableData)
      this.cartTableData.forEach(element => {
        this.$http.post('order/createorder/', {
          username: element.username,
          productName: element.productName,
          merchantName: element.merchantName,
          totalprice: element.price,
          inventory: element.inventory
        }).then(response => {
          if (response.data.status === 200) {
            this.$message.success('create order successfully！')
            this.delFromCart(element)
          } else {
            this.$message.error('Failed to create the order！')
            this.loadAllinCart()
          }
        }, response => {
          console.log('error')
          this.$message.error('Failed to create the order！')
        })
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

.menu-aside {
    background: #333744;
    height:100%
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

.menu {
    background: #333744;
    height:100%
}

</style>
