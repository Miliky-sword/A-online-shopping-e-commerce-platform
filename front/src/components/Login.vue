<template>
  <div class="login_container">
    <div class="login_box">
      <!-- 头像区 -->
      <div class="avatar_box">
        <img src="../assets/logo.png" alt="avatar" />
      </div>
      <!-- 登录表单 -->
      <div>
        <el-form
          ref="loginFormRef"
          :model="loginForm"
          :rules="loginFormRules"
          label-width="80px"
          class="login_form"
        >
          <el-form-item label="Username" prop="username">
            <el-input v-model="loginForm.username" prefix-icon="iconfont icon-user"></el-input>
          </el-form-item>
          <el-form-item label="Password" prop="password">
            <el-input
              v-model="loginForm.password"
              type="password"
              prefix-icon="iconfont icon-3702mima"
            ></el-input>
          </el-form-item>
          <el-form-item class="btns">
            <el-button type="primary" @click="login">submit</el-button>
            <el-button type="info" @click="resetLoginForm">reset the form</el-button>
            <el-button type="primary" @click="rores">registe</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
// 引入全局变量
import globalVar from '@/components/globalVar.vue'
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
            this.$message.success('Login success!')
            globalVar.userName = this.resp.userName
            globalVar.userType = this.resp.userType
            console.log(globalVar.userName)
            console.log(globalVar.userType)
            if (globalVar.userType === 0) {
              this.$router.push('/goodList')
            } else if (globalVar.userType === 1) {
              this.$router.push('/merchantManage')
            } else {
              this.$router.push('/manage')
            }
          }
        }, response => {
          console.log('error')
        })

        // 1、将登陆成功之后的token, 保存到客户端的sessionStorage中; localStorage中是持久化的保存
        //   1.1 项目中出现了登录之外的其他API接口，必须在登陆之后才能访问
        //   1.2 token 只应在当前网站打开期间生效，所以将token保存在sessionStorage中
        // window.sessionStorage.setItem('token', res.data.token)
        // 2、通过编程式导航跳转到后台主页, 路由地址为：/home
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
  background-color: #2b4b6b;
  height: 100%;
}
.login_box {
  width: 450px;
  height: 360px;
  background-color: #fff;
  border-radius: 3px;
  position: absolute;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
  background-color: #fff;

  .avatar_box {
    width: 130px;
    height: 130px;
    border: 1px solid #eee;
    border-radius: 50%;
    padding: 10px;
    box-shadow: 0 0 10px #ddd;
    position: left;
    left: 30%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    img {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background-color: #eee;
    }
  }
}
.login_form {
  position: absolute;
  bottom: 60px;
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
</style>
