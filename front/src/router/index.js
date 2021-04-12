import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import registe from '../components/registe.vue'
import manage from '../components/manage.vue'
import goodList from '../components/goodList.vue'
import merchantManage from '../components/merchantManage.vue'
Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/merchantManage' },
  { path: '/login', component: Login },
  { path: '/registe', component: registe },
  { path: '/manage', component: manage },
  { path: '/goodList', component: goodList },
  { path: '/merchantManage', component: merchantManage }

]

const router = new VueRouter({
  routes
})

export default router
