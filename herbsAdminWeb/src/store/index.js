import Vue from 'vue'
import Vuex from 'vuex'
import local from './localstore'
import axios from 'axios'
// import router from "@/router";
// import {resetRouter} from "@/router";

Vue.use(Vuex)

const  store = new Vuex.Store({
    state:{
        userInfo:null,
        menusList:null,
    },
    getters:{},
    mutations:{
        SET_USERINFO:(state,userInfo)=>{
            state.userInfo = userInfo
        },
        SET_MENUSLIST:(state, menusList)=>{
            state.menusList = menusList
        }
    },
    // {"userName":"admin","password":"admin","type":0}
    actions:{
        login({commit},loginUser){
            return new Promise((resolve,reject)=>{
                axios.post('http://127.0.0.1:8000/login',loginUser).then(res=>{
                    if(res){
                        console.log(res);
                        commit('SET_USERINFO',res.data.data)
                        local.setUserInfo(res.data.data)
                        resolve(res.data)
                    }
                }).catch(error=>{
                    reject(error);
                })
            })
        },
        getMenus(){
            return new Promise((resolve)=>{
                // 根据当前用户的类型获取相关菜单
                axios.post('http://localhost:8888/cylc/menu/query',{'type':local.getUserInfo().type}).then(res=>{
                    resolve(res);
                })
            })
        }
    },
});

export default store