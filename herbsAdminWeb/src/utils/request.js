import axios from 'axios'
import {Message} from 'element-ui'
const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    // `baseURL` 将自动加在 `url` 前面，除非 `url` 是一个绝对 URL。
    // 它可以通过设置一个 `baseURL` 便于为 axios 实例的方法传递相对 URL
    timeout: 2500,
  });


// 添加请求拦截器
instance.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    return config;
  }, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  });

// 添加响应拦截器
instance.interceptors.response.use(function (response) {
    // 对响应数据做点什么
    const res = response.data;
    console.log(res);
    if(response.status==200 || response.status==201 || response.status==204){
      return res
    }else{
        Message.error("异常错误！")
    }
  }, function (error) {
    // 对响应错误做点什么
    return Promise.reject(error);
  });



  export default instance
