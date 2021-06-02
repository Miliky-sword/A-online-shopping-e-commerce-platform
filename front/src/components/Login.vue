<template>
  <div class="login_container">
    <div class="login_box">
      <!-- 头像区 -->
      <!-- 登录表单 -->
      <div>
        <el-form
          ref="loginFormRef"
          :model="loginForm"
          :rules="loginFormRules"
          label-width="80px"
          class="login_form"
        >
          <el-form-item
            label="Username"
            prop="username"
          >
            <el-input
              v-model="loginForm.username"
              prefix-icon="iconfont icon-user"
            />
          </el-form-item>
          <el-form-item
            label="Password"
            prop="password"
          >
            <el-input
              v-model="loginForm.password"
              type="password"
              prefix-icon="iconfont icon-3702mima"
            />
          </el-form-item>
          <el-form-item class="btns">
            <el-button
              type="primary"
              @click="login"
            >
              submit
            </el-button>
            <el-button
              type="info"
              @click="resetLoginForm"
            >
              reset the form
            </el-button>
            <el-button
              type="primary"
              @click="rores"
            >
              registe
            </el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
    <img
      class="img_class"
      src="http://127.0.0.1:8000/static/img/1.png"
    >
  </div>
</template>

<script>
export default {
  data () {
    return {
      loginForm: {
        username: '',
        password: ''
      },
      // 表单验证
      loginFormRules: {
        username: [
          { required: true, message: 'please input your username', trigger: 'blur' },
          { min: 2, max: 10, message: 'min length : 2 ,  max length : 10', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'please input your password', trigger: 'blur' },
          { min: 2, max: 18, message: 'min length : 2 ,  max length : 18', trigger: 'blur' }
        ]
      },
      resp: []
    }
  },
  methods: {
    // 表单重置按钮
    resetLoginForm () {
      // console.log(this)
      // resetFields：element-ui提供的表单方法
      this.$refs.loginFormRef.resetFields()
    },
    login () {
      // 表单预验证
      // valid：bool类型
      this.$refs.loginFormRef.validate(valid => {
        // console.log(valid)
        if (!valid) return false
        this.$http.post('user/login/', {
          username: this.loginForm.username,
          password: this.loginForm.password
        }).then(response => {
          console.log(response.data)
          this.resp = response.data
          if (this.resp.status !== 200) {
            this.$message.error(this.resp.msg)
            this.$router.push('/login')
          } else {
            this.$session.set('username', this.resp.userName)
            this.$session.set('userType', this.resp.userType)
            this.$session.set('productId', 4)
            this.$message.success('Login success!')
            if (this.$session.get('userType') === 0) {
              this.$router.push('/home')
            } else if (this.$session.get('userType') === 1) {
              this.$router.push('/merchantManage')
            } else {
              this.$router.push('/manage')
            }
          }
        }, response => {
        })
      })
    },
    open (content, title) {
      this.$alert(content, title, {
        confirmButtonText: 'OK',
        type: 'info',
        callback: action => {
          this.$message({
            type: 'info'
            // message: `action: ${action}`
          })
        }
      })
    },
    rores () {
      this.$router.push('/registe')
    }
  }
}

</script>

<style scoped>
/* // lang="less" 支持less格式
// scoped vue的指令，只在当前组件生效 */
.login_container {
  background-color: #f3f3f3;
  height: 100%;
}
.login_box {
  width: 450px;
  height: 320px;
  background:rgba(255, 255, 255, 0.11);
  border-radius: 3px;
  position: absolute;
  left: 72%;
  top: 45%;
  -webkit-transform: translate(-50%, -50%);
  background:rgba(255, 255, 255, 0.40);
  z-index: 1;
}
.login_form {
  position: absolute;
  left: 0%;
  top: 25%;
  width: 100%;
  padding: 0 20px;
  box-sizing: border-box;
}
.btns {
  display: flex;
  justify-content: center;
}
.info {
  font-size: 13px;
  margin: 10px 15px;
}
.img_class {
  position: absolute;
  width: 1920px;
  height: 900px;
  text-align: center;
  z-index: 0;
}
</style>
