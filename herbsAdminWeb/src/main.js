import Vue from 'vue'
import App from './App.vue'
import router from "./router"
import store from "./store"
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import './assets/css/admin.css'
import * as echarts from 'echarts';
import VCharts from 'v-charts'
import axios from 'axios'
Vue.use(ElementUI);
Vue.prototype.$echarts = echarts
Vue.config.productionTip = false
Vue.prototype.$axios = axios
Vue.use(VCharts)

// 获取当期页的title
Vue.directive('title', {
  update: function (el) {
    document.title = '中草药识别系统';
  }
})



new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
