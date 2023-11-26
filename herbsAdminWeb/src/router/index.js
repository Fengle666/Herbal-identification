import Vue from 'vue'
import VueRouter from 'vue-router'
import {adminuserRouterMap} from './router'
Vue.use(VueRouter)

const constantRouterMap = [
    {
        path:'/',
        redirect:'/login'
    },
    {
        path:'/login',
        name:'login',
        component:()=>import('@/views/Login')
    },

]


const router = new VueRouter({
    routes:[
        ...constantRouterMap,...adminuserRouterMap
    ]

})

export default router

