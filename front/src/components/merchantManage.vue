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
          default-active="/merchantManage"
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
      <!-- 右侧主体内容 -->
      <el-main>
        <!-- 商品图片 -->
        <!-- <img class="goods1" src="../assets/goods1.png" alt="">
          <img class="goods2" src="../assets/goods2.png" alt=""> -->
        <!-- 商品基础信息表单 -->
        <!-- 用户列表区域 -->
        <div class="addproductbutton">
          <el-button
            type="info"
            @click="addProductDialogVisible = true"
          >
            add Product
          </el-button>
          <div style="margin: 20px 0;" />
        </div>
        <el-table
          :data="this.productTableData"
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
                <el-form-item label="inventory:  ">
                  <span>{{ props.row.inventory }}</span>
                </el-form-item>
                <el-form-item label="Profit:  ">
                  <span>{{ props.row.price - props.row.basePrice }}</span>
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
          <!-- stripe: 斑马条纹
        border：边框-->
          <el-table-column
            prop="id"
            label="id"
          />
          <el-table-column
            prop="productName"
            label="productName"
          />
          <el-table-column
            prop="price"
            label="price"
          />
          <el-table-column label="operation">
            <template slot-scope="scope">
              <el-button
                type="danger"
                icon="el-icon-delete"
                size="mini"
                @click="delProduct(scope.row)"
              >
                delete
              </el-button>
              <el-button
                icon="el-icon-add"
                size="mini"
                @click="addpicd(scope.row)"
              >
                add a picture
              </el-button>
              <el-button
                icon="el-icon-edit"
                type="primary"
                size="mini"
                @click="editproduct(scope.row)"
              >
                edit the product information
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-main>
    </el-container>

    <!-- 添加商品的对话框 -->
    <el-dialog
      title="Add Product"
      :visible.sync="addProductDialogVisible"
      width="50%"
      @close="addProductDialogClosed"
    >
      <!-- 内容主体 -->
      <el-form
        ref="addProductFormRef"
        :model="addProductForm"
        :rules="addProductFormRules"
        label-width="200px"
      >
        <el-form-item
          label="Product Name"
          prop="productName"
        >
          <el-input v-model="addProductForm.productName" />
        </el-form-item>
        <el-form-item
          label="Price"
          prop="price"
        >
          <el-input v-model="addProductForm.price" />
        </el-form-item>
        <el-form-item
          label="Cost"
          prop="cost"
        >
          <el-input v-model="addProductForm.cost" />
        </el-form-item>
        <el-form-item
          label="Date In Production"
          prop="dateInProduction"
        >
          <el-input v-model="addProductForm.dateInProduction" />
        </el-form-item>
        <el-form-item
          label="Inventory"
          prop="inventory"
        >
          <el-input v-model="addProductForm.inventory" />
        </el-form-item>
        <el-form-item
          label="Breif Description"
          prop="briefDiscription"
        >
          <el-input v-model="addProductForm.briefDescription" />
        </el-form-item>
      </el-form>
      <span
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="addProductDialogVisible = false">cancel</el-button>
        <el-button
          type="primary"
          @click="addProduct"
        >submit</el-button>
      </span>
    </el-dialog>
    <el-dialog
      title="upload a picture for this product"
      :visible.sync="picdialogVisible"
      width="30%"
      :before-close="handleClose"
    >
      <el-upload
        class="upload-demo"
        drag
        action="http://127.0.0.1:8000/product/post/"
        :data="{productId:this.curruntid}"
        multiple
      >
        <i class="el-icon-upload" />
        <div class="el-upload__text">
          drag a picture or <em>click here</em>
        </div>
        <div
          slot="tip"
          class="el-upload__tip"
        >
          only jpg or png，down 500kb
        </div>
      </el-upload>
      <span
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="picdialogVisible = false">cancel</el-button>
        <el-button
          type="primary"
          @click="picdialogVisible = false"
        >sumbit</el-button>
      </span>
    </el-dialog>
    <el-dialog
      title="Edit Product information"
      :visible.sync="editProductDialogVisible"
      width="50%"
      @close="editProductDialogClosed"
    >
      <!-- 内容主体 -->
      <el-form
        ref="editProductFormRef"
        :model="editProductForm"
        label-width="200px"
      >
        <el-form-item
          label="Price"
          prop="price"
        >
          <el-input v-model="editProductForm.price" />
        </el-form-item>
        <el-form-item
          label="Cost"
          prop="cost"
        >
          <el-input v-model="editProductForm.cost" />
        </el-form-item>
        <el-form-item
          label="Date In Production"
          prop="dateInProduction"
        >
          <el-input v-model="editProductForm.date" />
        </el-form-item>
        <el-form-item
          label="Inventory"
          prop="inventory"
        >
          <el-input v-model="editProductForm.inventory" />
        </el-form-item>
        <el-form-item
          label="Breif Description"
          prop="briefDiscription"
        >
          <el-input v-model="editProductForm.desc" />
        </el-form-item>
      </el-form>
      <span
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="editProductDialogVisible = false">cancel</el-button>
        <el-button
          type="primary"
          @click="editProductInfo"
        >submit</el-button>
      </span>
    </el-dialog>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      productTableData: [],
      addProductDialogVisible: false,
      editProductDialogVisible: false,
      picdialogVisible: false,
      curruntid: 0,
      addProductForm: {
        username: '',
        password: '',
        email: '',
        mobile: '',
        cost: undefined
      },
      editProductForm: {
        date: '',
        price: '',
        inventory: '',
        desc: '',
        cost: ''
      },
      glusername: this.$session.get('username'),

      addProductFormRules: {
        productName: [
          { required: true, message: 'please input the product name', trigger: 'blur' },
          {
            min: 1,
            max: 32,
            message: 'min length : 1  max length : 32',
            trigger: 'blur'
          }
        ],
        price: [
          { required: true, message: 'please input the price', trigger: 'blur' },
          {
            min: 1,
            max: 18,
            message: 'max length : 18',
            trigger: 'blur'
          }
        ],
        cost: [
          { required: true, message: 'please input the cost of the product', trigger: 'blur' }
        ],
        dateInProduction: [
          { required: true, message: 'please input the date in production! the format is YYYY-MM-DD', trigger: 'blur' },
          {
            min: 10,
            max: 10,
            message: 'format: YYYY-MM-DD',
            trigger: 'blur'
          }
        ]
      }
    }
  },
  created () {
    if (this.$session.get('username') === '' || this.$session.get('username') === null || this.$session.get('username') === undefined) {
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
      this.$http.post('product/getProduct/', {
        isAll: 0,
        merchantName: this.$session.get('username')
      }).then(response => {
        console.log(response.data.data.dataArray)
        this.productTableData = response.data.data.dataArray
      }, response => {
        console.log('error')
      })
    },
    addProduct () {
      this.$refs.addProductFormRef.validate(valid => {
        // console.log(valid)
        // 表单预校验失败
        if (!valid) return
        this.$http.post('product/addProduct/', {
          productName: this.addProductForm.productName,
          merchantName: this.$session.get('username'),
          price: this.addProductForm.price,
          inventory: this.addProductForm.inventory,
          dateInProduction: this.addProductForm.dateInProduction,
          briefDescription: this.addProductForm.briefDescription,
          cost: this.addProductForm.cost
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

        // 隐藏添加用户对话框
        this.addProductDialogVisible = false
        this.addProductForm = {}
        // this.getUserList()
      })
    },
    delProduct (row) {
      this.$http.post('product/delProduct/', {
        id: row.id
      }).then(response => {
        this.$message.info(response.data.msg)
      }, response => {
        this.$message.info(response.data.msg)
      })
      this.loadAllProduct()
    },
    handleClose (done) {
      this.$confirm('close？')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    },
    sumbit () {
      this.$refs.upload.submit()
    },
    addpicd (row) {
      this.curruntid = row.id
      console.log(this.curruntid)
      this.picdialogVisible = true
    },
    editproduct (row) {
      this.curruntid = row.id
      this.editProductDialogVisible = true
    },
    editProductInfo () {
      this.$http.post('product/editproinfo/', {
        pid: this.curruntid,
        price: this.editProductForm.price,
        inventory: this.editProductForm.inventory,
        cost: this.editProductForm.cost,
        date: this.editProductForm.date,
        desc: this.editProductForm.desc
      }).then(response => {
        this.editProductDialogVisible = false
        if (response.data.status === 200) {
          this.openmessage(response.data.msg)
          this.editProductForm.price = ''
          this.editProductForm.inventory = ''
          this.editProductForm.cost = ''
          this.editProductForm.date = ''
          this.editProductForm.desc = ''
        } else {
          this.openmessage(response.data.msg, 'Sorry')
        }
        this.loadAllProduct()
      })
    },
    openmessage (str1, str2) {
      this.$alert(str1, str2, {
        confirmButtonText: 'ok',
        callback: action => {}
      })
    }
  }
}
</script>

<style scoped>
.home-container {
    height: 100%;
}

.addproductbutton {
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

.el-aside {
    background: #444356;
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

</style>
