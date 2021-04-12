<template>
  <el-container class="home-container">
    <!-- 头部区域 -->
    <el-header>
        <div>
            <span>welcome to the e-commerce platform</span>
        </div>
        <el-button type="info" @click="logout">log out</el-button>
    </el-header>
    <!-- 页面主体区域 -->
    <el-container>
      <!-- 侧边栏 -->
      <el-aside width="200px">
          <div class="toggle-button">| | |</div>
          <!-- 侧边栏菜单区域 -->
          <el-menu background-color="#333744" text-color="#fff" active-text-color="#409EFF">
            <!-- 一级菜单 -->
            <el-submenu index="1">
              <!-- 一级菜单的模板区 -->
              <template slot="title">
                <!--  图标 -->
                <i class="el-icon-s-goods"></i>
                <!-- 文本 -->
                <span>browse the products</span>
              </template>
              <!-- 二级菜单 -->
              <el-menu-item index="1-1">
                <template slot="title">
                  <!--  图标 -->
                  <i class="el-icon-search"></i>
                  <!-- 文本 -->
                  <span>all Products</span>
                </template>
              </el-menu-item>
                <el-menu-item index="1-2">
                <template slot="title">
                  <!--  图标 -->
                  <i class="el-icon-search"></i>
                  <!-- 文本 -->
                  <span>search a Product</span>
                </template>
              </el-menu-item>
              <!-- 二级菜单 -->
              <el-menu-item index="1-3">
                <template slot="title">
                  <!--  图标 -->
                  <i class="el-icon-search"></i>
                  <!-- 文本 -->
                  <span>search a Merchat</span>
                </template>
              </el-menu-item>
            </el-submenu>
            <!-- 一级菜单 -->
            <el-submenu index="2">
              <!-- 一级菜单的模板区 -->
              <template slot="title">
                <!--  图标 -->
                <i class="el-icon-shopping-cart-2"></i>
                <!-- 文本 -->
                <span>shopping cart</span>
              </template>
            </el-submenu>
            <!-- 一级菜单 -->
            <el-submenu index="3">
              <!-- 一级菜单的模板区 -->
              <template slot="title">
                <!--  图标 -->
                <i class="el-icon-s-order"></i>
                <!-- 文本 -->
                <span>manage the order</span>
              </template>
            </el-submenu>
            <!-- 一级菜单 -->
            <el-submenu index="4">
              <!-- 一级菜单的模板区 -->
              <template slot="title">
                <!--  图标 -->
                <i class="el-icon-user-solid"></i>
                <!-- 文本 -->
                <span>User center</span>
              </template>
              <!-- 二级菜单 -->
              <el-menu-item index="4-1">
                <template slot="title">
                  <!--  图标 -->
                  <i class="el-icon-bell"></i>
                  <!-- 文本 -->
                  <span>notification</span>
                </template>
              </el-menu-item>
              <!-- 二级菜单 -->
              <el-menu-item index="4-2">
                <template slot="title">
                  <!--  图标 -->
                  <i class="el-icon-mouse"></i>
                  <!-- 文本 -->
                  <span>manage the accout</span>
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
          <template>
            <el-table
    :data="tableData"
    style="width: 100%">
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="Product name:  ">
            <span>{{ props.row.productName }}</span>
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
          <!-- <el-form-item label="商品预览：  ">
            <span>{{ props.row.picture }}</span>
          </el-form-item>
          <el-form-item label="商品分类">
            <span>{{ props.row.category }}</span>
          </el-form-item>
          <el-form-item label="店铺地址">
            <span>{{ props.row.address }}</span>
          </el-form-item>
          <el-form-item label="商品描述">
            <span>{{ props.row.desc }}</span>
          </el-form-item> -->
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      label="Product Name"
      prop="productName">
    </el-table-column>
    <el-table-column
      label="Inventory"
      prop="inventory">
    </el-table-column>
    <el-table-column
      label="Price"
      prop="price">
    </el-table-column>
  </el-table>
          </template>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import globalVar from '@/components/globalVar.vue'
export default {
  data () {
    return {
      tableData: []
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
      this.$http.get('product/getAvailableProduct/').then(response => {
        console.log(response.data.data.dataArray)
        this.tableData = response.data.data.dataArray
        this.$message.success('load products success！')
      }, response => {
        console.log('error')
        this.$message.error('failed to load products')
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

</style>
