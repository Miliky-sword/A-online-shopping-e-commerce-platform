import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui'
import './plugins/element.js'
import 'element-ui/lib/theme-chalk/index.css'

// self components import
import * as echarts from 'echarts'

import axios from 'axios'

import VueSession from 'vue-session'
axios.defaults.baseURL = 'http://47.108.209.135:8080/'

Vue.config.productionTip = false
Vue.prototype.$http = axios

Vue.use(VueSession)
Vue.use(ElementUI)

Vue.prototype.$echarts = echarts
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
