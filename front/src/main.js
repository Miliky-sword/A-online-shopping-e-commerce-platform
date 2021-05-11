import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui'
import './plugins/element.js'
import 'element-ui/lib/theme-chalk/index.css'

import axios from 'axios'

import VueSession from 'vue-session'
axios.defaults.baseURL = 'http://127.0.0.1:8000/'

Vue.config.productionTip = false
Vue.prototype.$http = axios
Vue.use(VueSession)
Vue.use(ElementUI)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
