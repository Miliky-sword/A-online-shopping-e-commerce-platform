import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import registe from '../components/registe.vue'
import manage from '../components/manage.vue'
import goodList from '../components/goodList.vue'
import merchantManage from '../components/merchantManage.vue'
import customerShoppingCart from '../components/customerShoppingCart.vue'
import customerOrder from '../components/customerOrder.vue'
import merchantOrder from '../components/merchantOrder.vue'
import customerSearch from '../components/customerSearch.vue'
import goodsinfo from '../components/goodsinfo.vue'
import Home from '../components/Home.vue'
import merchantStatistic from '../components/merchantStatistic.vue'
import customeruserinfo from '../components/customeruserinfo.vue'
import merchantuserinfo from '../components/merchantuserinfo.vue'
import manageruserinfo from '../components/manageruserinfo.vue'
import managerStatisticmer from '../components/managerStatisticmer.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  { path: '/registe', component: registe },
  { path: '/manage', component: manage },
  { path: '/goodList', component: goodList },
  { path: '/merchantManage', component: merchantManage },
  { path: '/customerShoppingCart', component: customerShoppingCart },
  { path: '/customerOrder', component: customerOrder },
  { path: '/merchantOrder', component: merchantOrder },
  { path: '/customerSearch', component: customerSearch },
  { path: '/goodsinfo', component: goodsinfo },
  { path: '/Home', component: Home },
  { path: '/merchantStatistic', component: merchantStatistic },
  { path: '/customeruserinfo', component: customeruserinfo },
  { path: '/merchantuserinfo', component: merchantuserinfo },
  { path: '/manageruserinfo', component: manageruserinfo },
  { path: '/managerStatisticmer', component: managerStatisticmer }
]

const router = new VueRouter({
  routes
})

export default router
