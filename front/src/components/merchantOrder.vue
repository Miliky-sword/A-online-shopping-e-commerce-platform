<template>
    <el-container class="home-container">
  <el-header class="header">
      <div>
            <span>welcome to the e-commerce platform</span>
        </div>
        <el-button type="info" @click="logout">log out</el-button>
    </el-header>
  <el-container class="main-container">
          <el-header class="menu-aside" width="250px">
          <el-menu class="menu" background-color="#333744" text-color="#fff" active-text-color="#66ccff" default-active="/merchantOrder" router mode="horizontal">
            <el-menu-item index="/merchantManage">
              <template slot="title">
                <i class="el-icon-s-goods"></i>
                <span>products on the shelves</span>
              </template>
            </el-menu-item>
            <el-menu-item index="/merchantOrder">
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
        <el-table :data="this.orderTableData" border stripe>
        <!-- stripe: 斑马条纹  border：边框-->
        <el-table-column prop="id" label="id"></el-table-column>
        <el-table-column prop="productName" label="productName"></el-table-column>
        <el-table-column prop="totalprice" label="price"></el-table-column>
        <el-table-column prop="status" label="status"></el-table-column>
        <el-table-column prop="inventory" label="inventory"></el-table-column>
        <el-table-column label="operation">
          <template slot-scope="scope" vertical>
              <el-button
              type="primary"
              icon="el-icon-edit"
              size="mini"
              @click="deliverytheproduct(scope.row)"
            >deliver the products</el-button>
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
      orderTableData: []
    }
  },
  created () {
    if (this.$session.get.username === '') {
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
        this.$message.success('load products success！')
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
    deliverytheproduct (row) {
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
