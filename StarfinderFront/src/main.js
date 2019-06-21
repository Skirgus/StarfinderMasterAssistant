import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  methods: {
    sendAuthData: function (message) {
      alert(message)
    }
  }
}).$mount('#app')
