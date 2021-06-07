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
          default-active="/manageruserinfo"
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
      <el-main>
        <!-- 用户基本信息 -->
        <el-table
          :data="tableData0"
          style="width: 700px"
          :show-header="false"
          class="table0"
        >
          <el-table-column
            prop="informationName"
            label="User's Name"
            width="200px"
          />
          <el-table-column
            prop="information"
            label="User"
            width="500px"
          />
        </el-table>
        <el-button
          class="but0"
          type="info"
          @click="dialogVisible = true"
        >
          Click here to edit your personal signature
        </el-button>
        <el-dialog
          title="Edit your personal signature"
          :visible.sync="dialogVisible"
          width="30%"
          :before-close="handleClose"
        >
          <el-input
            v-model="input0"
            placeholder="Enter your personal signature"
          />
          <span
            slot="footer"
            class="dialog-footer"
          >
            <el-button @click="dialogVisible = false">Cancel</el-button>
            <el-button
              type="primary"
              @click="addsig"
            >Confirm</el-button>
          </span>
        </el-dialog>
        <el-table
          :data="tableData1"
          style="width: 1000px"
          class="table1"
        >
          <el-table-column
            prop="informationName"
            label="User details"
            width="200px"
          />
          <el-table-column
            prop="information"
            label=""
            width="800px"
          />
        </el-table>
        <el-button
          type="info"
          class="but1"
          @click="dialogFormVisible = true"
        >
          Click here to modify personal information
        </el-button>
        <el-dialog
          title="Modify personal information"
          :visible.sync="dialogFormVisible"
          style="width: 1500px"
        >
          <el-form :model="form">
            <el-form-item
              label="Receiving address"
              :label-width="formLabelWidth"
            >
              <el-input
                v-model="form.address"
                autocomplete="off"
              />
            </el-form-item>
            <el-form-item
              label="Telephone"
              :label-width="formLabelWidth"
            >
              <el-input
                v-model="form.Telephone"
                autocomplete="off"
              />
            </el-form-item>
            <el-form-item
              label="PassWord"
              :label-width="formLabelWidth"
            >
              <el-input
                v-model="form.Password"
                autocomplete="off"
              />
            </el-form-item>
            <el-form-item
              label="Email"
              :label-width="formLabelWidth"
            >
              <el-input
                v-model="form.Email"
                autocomplete="off"
              />
            </el-form-item>
          </el-form>
          <div
            slot="footer"
            class="dialog-footer"
          >
            <el-button @click="dialogFormVisible = false">
              Cancel
            </el-button>
            <el-button
              type="primary"
              @click="editinfo"
            >
              Confirm modification
            </el-button>
          </div>
        </el-dialog>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      tableData0: [{
        informationName: 'User Name',
        information: 'username'
      },
      {
        informationName: 'Personal signature',
        information: 'Your personal signature'
      }],
      tableData1: [{
        informationName: 'Receiving address',
        information: 'Xi’an University of Electronic Science and technology, Xi’an, Shaanxi Province'
      }, {
        informationName: 'Telephone',
        information: '1XX XXXX XXXX'
      }, {
        informationName: 'Email',
        information: 'XXXXXXX@qq.com'
      }],
      dialogVisible: false,
      dialogFormVisible: false,
      input0: '',
      form: {
        address: '',
        Telephone: '',
        Email: '',
        Password: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      formLabelWidth: '180px'
    }
  },
  created () {
    if (this.$session.get('username') === '' || this.$session.get('username') === null || this.$session.get('username') === undefined) {
      return this.$router.push('/login')
    }
    this.loaduserInfo()
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
    addsig () {
      this.$http.post('user/addsig/', {
        username: this.$session.get('username'),
        sig: this.input0
      }).then(response => {
        if (response.data.status === 500) {
          this.openmessage(response.data.msg, 'Alert')
        } else {
          this.openmessage(response.data.msg, 'OK')
          this.loaduserInfo()
        }
      })
      this.dialogVisible = false
    },
    loaduserInfo () {
      this.$http.post('user/loadinfo/', {
        username: this.$session.get('username')
      }).then(response => {
        if (response.data.status === 500) {
          this.openmessage(response.data.msg, 'Alert')
        } else {
          this.tableData0[0].information = response.data.data.dataArray[0].username
          this.tableData0[1].information = response.data.data.dataArray[0].sig
          this.tableData1[0].information = response.data.data.dataArray[0].address
          this.tableData1[1].information = response.data.data.dataArray[0].phoneNumber
          this.tableData1[2].information = response.data.data.dataArray[0].email
        }
      })
    },
    editinfo () {
      this.$http.post('user/editinfo/', {
        username: this.$session.get('username'),
        address: this.form.address,
        phonenumber: this.form.Telephone,
        password: this.form.Password,
        email: this.form.Email
      }).then(response => {
        if (response.data.status === 500) {
          this.openmessage(response.data.msg, 'Alert')
        } else {
          this.dialogFormVisible = false
          this.openmessage(response.data.msg, 'Success')
          this.form.address = ''
          this.form.Telephone = ''
          this.form.Password = ''
          this.form.Email = ''
          this.loaduserInfo()
        }
      })
    }
  }
}
</script>

<style scoped>
.home-container {
    height: 100%;
}
.toggle-button{
    background: #4A5064;
    font-size: 10px;
    line-height: 24px;
    color: #fff;
    text-align: center;
    cursor: pointer;
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
    top: 20%;
    left: 20%;
}
.table1 {
    position: absolute;
    top: 40%;
    left: 20%;
}

.but0 {
    position: absolute;
    left: 71.5%;
    top: 27.5%;
}
.but1 {
    position: absolute;
    left: 40%;
    top: 65%;
}

</style>
