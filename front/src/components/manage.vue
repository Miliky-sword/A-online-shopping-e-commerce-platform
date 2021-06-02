<template>
  <el-container class="home-container">
    <!-- 头部区域 -->
    <el-header>
      <div>
        <span>Welcome to the online shopping e-commerce platform -- Manager</span>
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
          default-active="/manage"
          router
          mode="horizontal"
        >
          <el-menu-item
            index="/manage"
            router
          >
            <template slot="title">
              <i class="el-icon-s-goods" />
              <span>user list</span>
            </template>
          </el-menu-item>
          <el-menu-item index="/managerStatisticmer">
            <template slot="title">
              <i class="el-icon-s-order" />
              <span>Merchants' sales</span>
            </template>
          </el-menu-item>
          <el-menu-item
            index="/manageruserinfo"
          >
            <template slot="title">
              <i class="el-icon-user-solid" />
              <span>User center</span>
            </template>
          </el-menu-item>
        </el-menu>
      </el-header>
      <!-- 用户列表区域 -->
      <el-table
        :data="this.userlist"
        border
        stripe
        class="table0"
      >
        <!-- stripe: 斑马条纹
        border：边框-->
        <el-table-column
          prop="username"
          label="username"
        />
        <el-table-column
          prop="user_type"
          label="role"
        />
        <el-table-column
          prop="address"
          label="address"
        />
        <!--
        <el-table-column label="status">
          <template slot-scope="scope">
            <el-switch v-model="scope.row.mg_state" @change="userStateChanged(scope.row)"></el-switch>
          </template>
        </el-table-column>
        -->
        <el-table-column label="operation">
          <template slot-scope="scope">
            <!--
            <el-button
              type="primary"
              icon="el-icon-edit"
              size="mini"
              circle
              @click="showEditDialog(scope.row.username)"
            ></el-button>
            -->
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
              @click="removeUserByName(scope.row.username)"
            >
              delete user
            </el-button>
            <!--
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
            -->
          </template>
        </el-table-column>
      </el-table>
      <!-- 分页区域
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="queryInfo.pagenum"
        :page-sizes="[2, 5, 10, 15]"
        :page-size="queryInfo.pagesize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="totle"
      ></el-pagination>-->
      </el-card>
    </el-container>

    <!-- 添加用户的对话框 -->
    <el-dialog
      title="添加用户"
      :visible.sync="addDialogVisible"
      width="50%"
      @close="addDialogClosed"
    >
      <!-- 内容主体 -->
      <el-form
        ref="addUserFormRef"
        :model="addUserForm"
        :rules="addUserFormRules"
        label-width="100px"
      >
        <el-form-item
          label="Username"
          prop="username"
        >
          <el-input v-model="addUserForm.username" />
        </el-form-item>
        <el-form-item
          label="Password"
          prop="password"
        >
          <el-input v-model="addUserForm.password" />
        </el-form-item>
        <el-form-item
          label="User Type"
          prop="usertype"
        >
          <el-radio
            v-model="radio"
            label="0"
          >
            customer
          </el-radio>
          <el-radio
            v-model="radio"
            label="1"
          >
            merchant
          </el-radio>
          <el-radio
            v-model="radio"
            label="2"
          >
            manager
          </el-radio>
        </el-form-item>
        <el-form-item
          label="Delivery Address"
          prop="address"
        >
          <el-input v-model="addUserForm.address" />
        </el-form-item>
      </el-form>
      <span
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="addDialogVisible = false">cancel</el-button>
        <el-button
          type="primary"
          @click="addUser"
        >submit</el-button>
      </span>
    </el-dialog>
    </div>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      // 获取用户列表查询参数对象
      queryInfo: {
        query: '',
        // 当前页数
        pagenum: 1,
        // 每页显示多少数据
        pagesize: 5
      },
      resp: [],
      userlist: [],
      totle: 0,
      // 添加用户对话框
      addDialogVisible: false,
      // 用户添加
      addUserForm: {},
      // 用户添加表单验证规则
      addUserFormRules: {
        username: [
          { required: true, message: 'please input your username', trigger: 'blur' },
          {
            min: 2,
            max: 10,
            message: 'min length : 2  max length : 10',
            trigger: 'blur'
          }
        ],
        password: [
          { required: true, message: 'please input your password', trigger: 'blur' },
          {
            min: 2,
            max: 18,
            message: 'min length : 2  max length : 18',
            trigger: 'blur'
          }
        ],
        address: [
          { required: true, message: 'please input your address', trigger: 'blur' },
          { min: 2, max: 18, message: 'min length : 2  max length : 30', trigger: 'blur' }
        ]
      },
      // 修改用户
      editDialogVisible: false,
      editUserForm: {},
      // 分配角色对话框
      setRoleDialogVisible: false,
      // 当前需要被分配角色的用户
      userInfo: {},
      // 所有角色数据列表
      rolesLsit: [],
      // 已选中的角色Id值
      selectRoleId: '',
      radio: 1
    }
  },
  created () {
    if (this.$session.get('username') === '') {
      this.$router.push('/login')
    }
    this.getUserList()
  },
  methods: {
    logout () {
      this.$session.set('username', '')
      this.$session.set('userType', '')
      this.$router.push('/login')
    },
    getUserList () {
      const { data: res } = this.$http.get('user/allusers/', {
        params: this.queryInfo
      }).then(response => {
        console.log('userlist')
        this.userlist = response.data.data.data
        this.$message.success('got user list successfully！')
        console.log(self.userlist)
      }, response => {
        console.log('error')
      })
      if (res.meta.status !== 200) {
        return this.$message.error('failed to get user list！')
      }
      this.userlist = res.data.users
      this.totle = res.data.totle
    },
    // 监听 pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getUserList()
    },
    // 监听 页码值 改变事件
    handleCurrentChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagenum = newSize
      this.getUserList()
    },
    // 监听 switch开关 状态改变
    async userStateChanged (userInfo) {
      // console.log(userInfo)
      const { data: res } = await this.$http.put(
        `users/${userInfo.id}/state/${userInfo.mg_state}`
      )
      if (res.meta.status !== 200) {
        userInfo.mg_state = !userInfo.mg_state
        return this.$message.error('更新用户状态失败')
      }
      this.$message.success('更新用户状态成功！')
    },
    // 监听 添加用户对话框的关闭事件
    addDialogClosed () {
      this.$refs.addUserFormRef.resetFields()
    },
    // 添加用户
    addUser () {
      // 提交请求前，表单预验证
      this.$refs.addUserFormRef.validate(async valid => {
        // console.log(valid)
        // 表单预校验失败
        console.log(this.addUserForm.username)
        if (!valid) return
        this.$http.post('user/register/', {
          username: this.addUserForm.username,
          password: this.addUserForm.password,
          address: this.addUserForm.address,
          user_type: this.radio
        }).then(response => {
          console.log(response.data)
          this.resp = response.data
          if (this.resp.status === 200) {
            this.$alert('add user success', 'Info')
            this.addDialogVisible = false
          } else {
            this.$alert('failed to registe', 'Info')
            // his.$router.push('/registe')
          }
          console.log(self.resp.msg)
        }, response => {
          console.log('error')
        })
      })
    },
    // 编辑用户信息
    async showEditDialog (id) {
      const { data: res } = await this.$http.get('users/' + id)
      if (res.meta.status !== 200) {
        return this.$message.error('查询用户信息失败！')
      }
      this.editUserForm = res.data
      this.editDialogVisible = true
    },
    // 监听修改用户对话框的关闭事件
    editDialogClosed () {
      this.$refs.editUserFormRef.resetFields()
    },
    // 修改用户信息
    editUser () {
      // 提交请求前，表单预验证
      this.$refs.editUserFormRef.validate(async valid => {
        // console.log(valid)
        // 表单预校验失败
        if (!valid) return
        const { data: res } = await this.$http.put(
          'users/' + this.editUserForm.id,
          {
            email: this.editUserForm.email,
            mobile: this.editUserForm.mobile
          }
        )
        if (res.meta.status !== 200) {
          this.$message.error('更新用户信息失败！')
        }
        // 隐藏添加用户对话框
        this.editDialogVisible = false
        this.$message.success('更新用户信息成功！')
        this.getUserList()
      })
    },
    // 删除用户
    async removeUserByName (username) {
      console.log(username)
      const confirmResult = await this.$confirm(
        'Alert! this operation will delete the user!',
        'Info',
        {
          confirmButtonText: 'submit',
          cancelButtonText: 'cancel',
          type: 'warning'
        }
      ).catch(err => err)
      // 点击确定 返回值为：confirm
      // 点击取消 返回值为： cancel
      if (confirmResult === 'cancel') {
        return this.$message.info('delete canceled!')
      }
      this.$http.post('user/removeUserByName/', {
        username: username
      }).then(response => {
        // console.log(response.data)
        self.resp = response.data
        console.log(self.resp.msg)
        this.getUserList()
      }, response => {
        console.log('error')
      })
    },
    // 展示分配角色的对话框
    async showSetRole (role) {
      this.userInfo = role
      // 展示对话框之前，获取所有角色列表
      const { data: res } = await this.$http.get('roles')
      if (res.meta.status !== 200) {
        return this.$message.error('获取角色列表失败！')
      }
      this.rolesLsit = res.data
      this.setRoleDialogVisible = true
    },
    // 分配角色
    async saveRoleInfo () {
      if (!this.selectRoleId) {
        return this.$message.error('请选择要分配的角色')
      }
      const { data: res } = await this.$http.put(`users/${this.userInfo.id}/role`, { rid: this.selectRoleId })
      if (res.meta.status !== 200) {
        return this.$message.error('更新用户角色失败！')
      }
      this.$message.success('更新角色成功！')
      this.getUserList()
      this.setRoleDialogVisible = false
    },
    // 分配角色对话框关闭事件
    setRoleDialogClosed () {
      this.selectRoleId = ''
      this.userInfo = {}
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

.table0 {
    position: absolute;
    width: 70%;
    top: 20%;
    left: 15%;
}
</style>
