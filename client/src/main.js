import Vue from 'vue'
import App from './App.vue'
import router from './utils/routes'
import { BootstrapVue} from 'bootstrap-vue'

Vue.config.productionTip = false

Vue.use(router);
Vue.use(BootstrapVue)

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
