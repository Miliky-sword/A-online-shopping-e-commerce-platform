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
          default-active="/customerOrder"
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
      <el-main class="main">
        <el-table
          :data="this.orderTableData"
          border
          stripe
        >
          <!-- stripe: 斑马条纹  border：边框-->
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form
                label-position="left"
                inline
                class="demo-table-expand"
              >
                <el-form-item label="Product id:  ">
                  <span>{{ props.row.productId }}</span>
                </el-form-item>
                <el-form-item label="Merchant name:  ">
                  <span>{{ props.row.merchantName }}</span>
                </el-form-item>
                <el-form-item label="total price">
                  <span>{{ props.row.totalprice }}</span>
                </el-form-item>
                <el-form-item label="inventory:  ">
                  <span>{{ props.row.inventory }}</span>
                </el-form-item>
                <el-form-item label="from phone Number:  ">
                  <span>{{ props.row.fromPhoneNumber }}</span>
                </el-form-item>
                <el-form-item label="from Address:  ">
                  <span>{{ props.row.fromAddress }}</span>
                </el-form-item>
                <el-form-item label="receive phone Number：  ">
                  <span>{{ props.row.toPhoneNumber }}</span>
                </el-form-item>
                <el-form-item label="receive Address:   ">
                  <span>{{ props.row.address }}</span>
                </el-form-item>
              </el-form>
            </template>
          </el-table-column>
          <el-table-column
            prop="id"
            label="Order uid"
            width="100"
          />
          <el-table-column
            prop="productName"
            label="Product Name"
            width="200"
          />
          <el-table-column
            prop="status"
            label="Status"
            width="150"
          />
          <el-table-column
            label="Operation"
            :align="center"
            width="300"
          >
            <template
              slot-scope="scope"
              horizon
            >
              <el-button
                type="primary"
                size="mini"
                @click="payOrder(scope.row)"
              >
                pay the order
              </el-button>
              <el-button
                type="success"
                size="mini"
                @click="confirmdelivery(scope.row)"
              >
                confirm the delivery
              </el-button>
            </template>
          </el-table-column>
          <el-table-column label="Cancel">
            <template
              slot-scope="scope"
              vertical
            >
              <el-button
                icon="el-icon-delete"
                size="mini"
                @click="cancelOrder(scope.row)"
              >
                cancel the order
              </el-button>
            </template>
          </el-table-column>
          <el-table-column label="Comment">
            <template
              slot-scope="scope"
              vertical
            >
              <el-button
                type="primary"
                icon="el-icon-edit"
                size="mini"
                @click="comment(scope.row)"
              >
                comment on the product
              </el-button>
            </template>
          </el-table-column>
          </el-table-column>
        </el-table>
      </el-main>
    </el-container>
    <el-dialog
      title="Mark and Comment !"
      :visible.sync="commentDialogVisible"
      width="30%"
      @close="commentDialogClosed"
    >
      <div>
        How do you think of this product ?
      </div>
      <div style="margin: 20px 0;" />
      <div>
        Please give it stars and comment on it !
      </div>
      <div style="margin: 40px 0;" />
      <div class="block">
        <span class="demonstration" />
        <el-rate
          v-model="starValue"
          :colors="colors"
        />
      </div>
      <div style="margin: 40px 0;" />
      <el-input
        v-model="textarea1"
        type="textarea"
        autosize
        placeholder="请输入内容"
        maxlength="512"
        show-word-limit
      />
      <div style="margin: 40px 0;" />
      <span
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="commentDialogVisible = false">cancel</el-button>
        <el-button
          type="primary"
          @click="addcomment"
        >submit</el-button>
      </span>
    </el-dialog>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      orderTableData: [],
      commentDialogVisible: false,
      commentForm: {},
      starValue: 0,
      curproid: 0,
      curoid: -1,
      textarea1: '',
      colors: ['#99A9BF', '#F7BA2A', '#FF9900']
    }
  },
  created () {
    if (this.$session.get('username') === '') {
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
    openmessage (str1, str2) {
      this.$alert(str1, str2, {
        confirmButtonText: 'ok',
        callback: action => {}
      })
    },
    loadAllofOrder () {
      this.$http.post('order/getcustomerorders/', {
        username: this.$session.get('username')
      }).then(response => {
        console.log(response.data.data.dataArray)
        this.orderTableData = response.data.data.dataArray
      }, response => {
        console.log('error')
        this.$message.error('failed to load products')
      })
    },
    payOrder (row) {
      if (row.status !== 'Pending') {
        this.openmessage("Please check your order status! you can't pay for it!", 'Sorry')
        return
      }
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
      if (row.status !== 'Out for delivery') {
        this.openmessage("Please check your order status! you can't confirm delivery!", 'Sorry')
        return
      }
      this.$http.post('order/changeorderstatusdelivered/', {
        id: row.id
      }).then(response => {
        this.$message.success(response.data.msg)
        this.loadAllofOrder()
        this.curproid = row.productId
        this.curoid = row.id
        this.commentDialogVisible = true
      }, response => {
        console.log('error')
        this.$message.error(response.data.msg)
      })
    },
    cancelOrder (row) {
      if (row.status !== 'Delivered') {
        this.openmessage("Please check your order status! you can't cancel this order!", 'Sorry')
        return
      }
      this.$http.post('order/changeorderstatuscanceled/', {
        id: row.id
      }).then(response => {
        this.loadAllofOrder()
        if (response.data.status === 200) {
          this.$message.success(response.data.msg)
          this.openmessage('You have canceled this order! Your money will be refunded within three days.', 'OK')
        }
      }, response => {
        console.log('error')
        this.$message.error(response.data.msg)
      })
    },
    commentDialogClosed () {
      this.starValue = 0
      this.$refs.commentFormRef.resetFields()
      this.commentDialogVisible = false
    },
    comment (row) {
      if (row.status !== 'Delivered') {
        this.openmessage("Please check your order status! you can't comment on it!", 'Sorry')
        return
      }
      this.curproid = row.productId
      this.commentDialogVisible = true
      this.curoid = row.id
      console.log(this.curoid)
    },
    addcomment () {
      console.log(this.textarea1)
      this.$http.post('product/AddComment/', {
        productId: this.curproid,
        neirong: this.textarea1,
        star: this.starValue,
        customerName: this.$session.get('username'),
        orderId: this.curoid
      }).then(response => {
        this.loadAllofOrder()
        this.starValue = 0
        this.textarea1 = ''
        this.commentDialogVisible = false
        console.log(response.data.status)
        if (response.data.status === 501) {
          this.openmessage(response.data.msg, 'Alert')
        } else { this.openmessage('thank you for your comments', 'Success') }
      }, response => {
        console.log('error')
        this.openmessage('submit comment and score failed', 'Alert')
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
