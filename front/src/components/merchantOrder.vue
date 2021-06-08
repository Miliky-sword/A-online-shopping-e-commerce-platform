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
          default-active="/merchantOrder"
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
      <el-main class="main">
        <el-table
          class="table"
          :data="this.orderTableData"
          border
          stripe
        >
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form
                label-position="left"
                inline
                class="demo-table-expand"
              >
                <el-form-item label="product id:   ">
                  <span>{{ props.row.productId }}</span>
                </el-form-item>
                <el-form-item label="profit:   ">
                  <span>{{ props.row.profit }}</span>
                </el-form-item>
                <el-form-item label="from phone Number:  ">
                  <span>{{ props.row.fromPhoneNumber }}</span>
                </el-form-item>
                <el-form-item label="from Address:  ">
                  <span>{{ props.row.fromAddress }}</span>
                </el-form-item>
                <el-form-item label="to phone Number：  ">
                  <span>{{ props.row.toPhoneNumber }}</span>
                </el-form-item>
                <el-form-item label="to Address:   ">
                  <span>{{ props.row.address }}</span>
                </el-form-item>
              </el-form>
            </template>
          </el-table-column>
          <!-- stripe: 斑马条纹  border：边框-->
          <el-table-column
            prop="id"
            label="order uid"
            width="100px"
          />
          <el-table-column
            prop="productName"
            label="productName"
          />
          <el-table-column
            prop="totalprice"
            label="total price"
            width="150px"
          />
          <el-table-column
            prop="status"
            label="status"
            width="150px"
          />
          <el-table-column
            prop="inventory"
            label="inventory"
            width="200px"
          />
          <el-table-column label="operation">
            <template
              slot-scope="scope"
              vertical
            >
              <el-button
                type="primary"
                icon="el-icon-edit"
                size="mini"
                @click="deliverytheproduct(scope.row)"
              >
                deliver the products
              </el-button>
              <el-button
                type="primary"
                icon="el-icon-edit"
                size="mini"
                @click="cancelorder(scope.row)"
              >
                refund the money
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      orderTableData: [],
      timercount: 0,
      timer: undefined
    }
  },
  created () {
    if (this.$session.get('username') === '' || this.$session.get('username') === null || this.$session.get('username') === undefined) {
      return this.$router.push('/login')
    }
    this.loadAllofOrder()
  },
  methods: {
    logout () {
      this.$session.set('username', '')
      this.$session.set('userType', '')
      this.$router.push('/login')
    },
    loadAllofOrder () {
      this.$http.post('order/getmerchantorders/', {
        merchantName: this.$session.get('username')
      }).then(response => {
        console.log(response.data.data.dataArray)
        this.orderTableData = response.data.data.dataArray
      }, response => {
        console.log('error')
        this.$message.error('failed to load products')
      })
    },
    payOrder (row) {
      this.$http.post('order/changeorderstatuspayed/', {
        id: row.id
      }).then(response => {
        this.$message.success(response.data.msg)
        this.loadAllofOrder()
      }, response => {
        console.log('error')
        this.$message.error(response.data.msg)
      })
    },
    confirmdelivery (row) {
      this.$http.post('order/changeorderstatusdelivered/', {
        id: row.id
      }).then(response => {
        this.$message.success(response.data.msg)
        this.loadAllofOrder()
      }, response => {
        console.log('error')
        this.$message.error(response.data.msg)
      })
    },
    canceledorder (row) {
      this.$http.post('order/changeorderstatuscanceled/', {
        id: row.id
      }).then(response => {
        this.loadAllofOrder()
      }, response => {
        console.log('error')
        this.$message.error(response.data.msg)
      })
    },
    cancelorder (row) {
      if (row.status !== 'Canceling') {
        this.openmessage("Please check your order status! you can't pay for it!", 'Sorry')
        return
      }
      this.$http.post('pay/refund/', {
        id: row.id,
        price: row.totalprice,
        pname: row.productName
      }).then(response => {
        this.$http.defaults.url = undefined
        this.$http.get(response.data.url).then(response => {
          console.log(response.data.alipay_trade_refund_response)
          if (response.data.alipay_trade_refund_response.msg === 'Success') {
            this.canceledorder(row)
            this.openmessage('The money is refunded!', 'OK')
          } else {
            this.openmessage('Please try again!', 'Sorry')
          }
        })
        this.$http.defaults.url = 'http://47.108.209.135:8080/'
        console.log('page open')
        // 先清空定时器
        clearInterval(this.timer)
        // 重新使用定时器
        this.timer = setInterval(() => {
          setTimeout(this.loadAllofOrder, 0)
          // eslint会报xxx is defined but never used，加个console.log就好了
          console.log(this.timer)
          this.timercount += 1
          if (this.timercount > 60) {
            clearInterval(this.timer)
            this.timer = undefined
            this.timercount = 0
          }
          console.log(this.timercount)
        }, 1000)
        this.$message.success(response.data.msg)
        this.loadAllofOrder()
      }, response => {
        console.log('error')
        this.$message.error(response.data.msg)
      })
    },
    openmessage (str1, str2) {
      this.$alert(str1, str2, {
        confirmButtonText: 'ok',
        callback: action => {}
      })
    },
    deliverytheproduct (row) {
      if (row.status !== 'Payed') {
        this.openmessage("You can't deliver the products! Please check the order status!", 'Sorry')
        return
      }
      this.$http.post('order/changeorderstatusdelivering/', {
        id: row.id
      }).then(response => {
        this.$message.info(response.data.msg)
        this.loadAllofOrder()
      }, response => {
        console.log('error')
        this.$message.info(response.data.msg)
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

.table {
  width: 75%;
  left: 12.5%;
  text-align: center;
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
