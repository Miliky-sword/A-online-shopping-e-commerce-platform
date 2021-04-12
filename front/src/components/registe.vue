<template>
  <div class="login_container">
    <div class="login_box">
      <!-- 登录表单 -->
      <div class="title">
          registe your account!
      </div>
      <div>
        <el-form
        :model="addUserForm"
        ref="addUserFormRef"
        :rules="resFormRules"
        label-width="100px"
      >
        <el-form-item label="Username" prop="username">
          <el-input v-model="addUserForm.username"></el-input>
        </el-form-item>
        <el-form-item label="Password" prop="password">
          <el-input v-model="addUserForm.password"></el-input>
        </el-form-item>
        <el-form-item label="User_Type" prop="usertype">
         <el-radio v-model="radio" label=0>customer</el-radio>
        <el-radio v-model="radio" label=1>merchant</el-radio>
        <el-radio v-model="radio" label=2>manager</el-radio>
        </el-form-item>
        <el-form-item label="Address" prop="address">
          <el-input v-model="addUserForm.address"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
          <div class="btns">
        <el-button @click="resetResForm">reset this form</el-button>
        <el-button type="primary" @click="addUser">submit</el-button>
        <el-button type="primary" @click="logout">cancel</el-button>
          </div>
      </span>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      addUserForm: {},
      // 表单验证
      resFormRules: {
        username: [
          { required: true, message: 'please input your username', trigger: 'blur' },
          { min: 2, max: 10, message: 'min length : 2  max length : 10', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'please input your password', trigger: 'blur' },
          { min: 2, max: 18, message: 'min length : 2  max length : 18', trigger: 'blur' }
        ],
        address: [
          { required: true, message: 'please input your address', trigger: 'blur' },
          { min: 2, max: 30, message: 'min length : 2  max length : 30', trigger: 'blur' }
        ]
      },
      resp: [],
      radio: 1
    }
  },
  methods: {
    logout () {
      window.sessionStorage.clear()
      this.$router.push('/login')
    },
    // 表单重置按钮
    resetResForm () {
      // console.log(this)
      // resetFields：element-ui提供的表单方法
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
            this.$alert('registed successfully! please log in', 'Info')
            this.$router.push('/login')
          } else {
            this.$alert('failed to registe', 'Info')
            this.$router.push('/registe')
          }
          console.log(self.resp.msg)
        }, response => {
          console.log('error')
        })

        // if (self.resp.status !== 201) {
        //  this.$message.error('添加用户失败！')
        // }
        // this.$message.success('添加用户成功！')
        // 隐藏添加用户对话框
        // this.addDialogVisible = false
        // this.getUserList()
      })
    }
  }
}
</script>

<style scoped>
.title {
  display: flex;
  justify-content: center;
}

.btns {
display: flex;
  justify-content: center;
}
</style>
