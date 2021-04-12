<template>
  <el-container class="home-container">
    <!-- 头部区域 -->
    <el-header>
        <div>
            <span>merchant manage</span>
        </div>
        <el-button type="info" @click="logout">log out</el-button>
        <el-button type="primary" @click="addProductDialogVisible = true">add Product</el-button>
    </el-header>
    <!-- 页面主体区域 -->
    <el-container>
      <!-- 侧边栏 -->
      <el-aside width="250px">
          <div class="toggle-button">| | |</div>
          <!-- 侧边栏菜单区域 -->
          <el-menu background-color="#444356" text-color="#fff" active-text-color="#409EFF">
            <!-- 一级菜单 -->
            <el-submenu index="1">
              <!-- 一级菜单的模板区 -->
              <template slot="title">
                <!--  图标 -->
                <i class="el-icon-s-goods"></i>
                <!-- 文本 -->
                <span>product on the shelves</span>
              </template>
            </el-submenu>
            <!-- 一级菜单 -->
            <!-- 一级菜单 -->
            <el-submenu index="2">
              <!-- 一级菜单的模板区 -->
              <template slot="title">
                <!--  图标 -->
                <i class="el-icon-s-order"></i>
                <!-- 文本 -->
                <span>My order</span>
              </template>
            </el-submenu>
            <!-- 一级菜单 -->
            <el-submenu index="3">
              <!-- 一级菜单的模板区 -->
              <template slot="title">
                <!--  图标 -->
                <i class="el-icon-user-solid"></i>
                <!-- 文本 -->
                <span>User Information</span>
              </template>
              <!-- 二级菜单 -->
              <el-menu-item index="3-1">
                <template slot="title">
                  <!--  图标 -->
                  <i class="el-icon-bell"></i>
                  <!-- 文本 -->
                  <span>notification</span>
                </template>
              </el-menu-item>
              <!-- 二级菜单 -->
              <el-menu-item index="3-2">
                <template slot="title">
                  <!--  图标 -->
                  <i class="el-icon-mouse"></i>
                  <!-- 文本 -->
                  <span>manage the account</span>
                </template>
              </el-menu-item>
              <!-- 二级菜单 -->
            </el-submenu>
        </el-menu>
      </el-aside>
      <!-- 右侧主体内容 -->
      <el-main>
          <!-- 商品图片 -->
          <!-- <img class="goods1" src="../assets/goods1.png" alt="">
          <img class="goods2" src="../assets/goods2.png" alt=""> -->
          <!-- 商品基础信息表单 -->
          <!-- 用户列表区域 -->
      <el-table :data="this.productTableData" border stripe>
        <!-- stripe: 斑马条纹
        border：边框-->
        <el-table-column prop="id" label="id"></el-table-column>
        <el-table-column prop="productName" label="productName"></el-table-column>
        <el-table-column prop="price" label="price"></el-table-column>
        <el-table-column label="status">
          <template slot-scope="scope">
            <el-switch v-model="scope.row.mg_state" @change="userStateChanged(scope.row)"></el-switch>
          </template>
        </el-table-column>
        <el-table-column label="operation">
          <template slot-scope="scope">
            <el-button
              type="primary"
              icon="el-icon-edit"
              size="mini"
              circle
              @click="showEditDialog(scope.row.username)"
            ></el-button>
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
              circle
              @click="removeUserByName(scope.row.username)"
            ></el-button>
            <el-tooltip
              class="item"
              effect="dark"
              content="角色分配"
              :enterable="false"
              placement="top"
            >
              <el-button
                type="warning"
                icon="el-icon-setting"
                size="mini"
                circle
                @click="showSetRole(scope.username)"
              ></el-button>
            </el-tooltip>
          </template>
        </el-table-column>
      </el-table>
      </el-main>
    </el-container>

        <!-- 添加商品的对话框 -->
    <el-dialog title="Add Product" :visible.sync="addProductDialogVisible" width="50%" @close="addProductDialogClosed">
      <!-- 内容主体 -->
      <el-form
        :model="addProductForm"
        ref="addProductFormRef"
        :rules="addProductFormRules"
        label-width="100px"
      >
        <el-form-item label="Product Name" prop="productName">
          <el-input v-model="addProductForm.productName"></el-input>
        </el-form-item>
        <el-form-item label="Price" prop="price">
          <el-input v-model="addProductForm.price"></el-input>
        </el-form-item>
        <el-form-item label="Date In Production" prop="dateInProduction">
          <el-input v-model="addProductForm.dateInProduction"></el-input>
        </el-form-item>
        <el-form-item label="Inventory" prop="inventory">
          <el-input v-model="addProductForm.inventory"></el-input>
        </el-form-item>
        <el-form-item label="Breif Description" prop="briefDiscription">
          <el-input v-model="addProductForm.briefDescription"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="addProductDialogVisible = false">cancel</el-button>
        <el-button type="primary" @click="addProduct">submit</el-button>
      </span>
    </el-dialog>
  </el-container>
</template>

<script>
import globalVar from '@/components/globalVar.vue'
export default {
  data () {
    return {
      productTableData: [],
      addProductDialogVisible: false,
      addProductForm: {
        username: '',
        password: '',
        email: '',
        mobile: ''
      },
      glusername: globalVar.userName,

      addProductFormRules: {
        productName: [
          { required: true, message: 'please input the product name', trigger: 'blur' },
          {
            min: 1,
            max: 10,
            message: 'min length : 1  max length : 10',
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
        dateInProduction: [
          { required: true, message: 'please input the date in production! YYYY-MM-DD', trigger: 'blur' },
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
    if (globalVar.userName === '') {
      return this.$router.push('/login')
    }
    this.loadAllProduct()
  },
  methods: {
    logout () {
      window.sessionStorage.clear()
      this.$router.push('/login')
    },
    loadAllProduct () {
      console.log(this.glusername)
      this.$http.post('product/getProduct/', {
        isAll: 0,
        merchantName: this.glusername
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
        console.log(globalVar.userName)
        if (!valid) return
        this.$http.post('product/addProduct/', {
          productName: this.addProductForm.productName,
          merchantName: globalVar.userName,
          price: this.addProductForm.price,
          inventory: this.addProductForm.inventory,
          dateInProduction: this.addProductForm.dateInProduction,
          briefDescription: this.addProductForm.briefDescription
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
        // this.getUserList()
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
