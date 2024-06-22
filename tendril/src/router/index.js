import Vue from 'vue'
import Router from 'vue-router'
import plofile from '@/components/profile.vue'
import hello from '@/components/hello.vue'

Vue.use(Router)

export default new Router({
    routes: [
      {
        path: '/',
        name: 'hello',
        component: hello
      },                 // , の追加を忘れずに
      {
        path: '/plofile',   // new add
        name: 'plofile',    // new add
        component: plofile  // new add
      }
    ]
  })