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
  { path: '/merchantOrder', component: merchantOrder }

]

const router = new VueRouter({
  routes
})

export default router
