import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import locale from 'element-ui/lib/locale/lang/en'
import axios from 'axios'

// support English
Vue.use(ElementUI,{ locale })

Vue.use(ElementUI)
Vue.prototype.$axios = axios
axios.defaults.baseURL = ''

new Vue({
  el: '#app',
  render: h => h(App)
})
