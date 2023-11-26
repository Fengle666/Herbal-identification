<template>
    <div id="bj">
        <div class="login-container">
            <div class="login-main">
                
                <div class="box">
                    <div class="title">中草药识别系统</div>
                    <el-form ref="loginForm" :model="form" :rules="rules">
                        <el-form-item prop="username">
                            <el-input v-model="form.username" prefix-icon="el-icon-login-user" class="login-user" placeholder="请输入用户名" > </el-input>
                        </el-form-item>
                        <el-form-item prop="password">
                            <el-input type="password" v-model="form.password" prefix-icon="el-icon-login-password" class="login-pwd" placeholder="请输入密码"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="login" class="login-btn" :loading="false">登录</el-button>

                        </el-form-item>
                    </el-form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import '@riophae/vue-treeselect/dist/vue-treeselect.css'
import request from '@/utils/request'
import {Message} from 'element-ui'
export default {
    name: "Login",
    data(){
        return {
            form:{
                username:'',
                password:'',
            },
            rules:{
                username:[{required:true,message:"用户名不能为空"}],
                password:[{required:true,message:"密码不能为空"}],
            },
            centerDialogVisible: false,
            organizeIdList:[],

        }
    },
    methods:{
        login(){
            this.$refs['loginForm'].validate(valid=>{
                if(valid){
                    // 用户登录请求
                    this.$store.dispatch('login',this.form).then(res=>{
                        console.log(res);
                        if(res.code==200){
                            this.$router.push('/home');
                            console.log(res);
                        }else{
                            Message.error(res.error)
                        }
                    }).catch(error=>{
                        console.log(error)
                    });
                }
            });
        },
    }
}
</script>

<style scoped>
#bj{
    background-image: url('../assets/images/bj.png');
    background-repeat:no-repeat;
    background-size: 100% 100%;
    width: 100%;
    height: 100%; 
}
.login-header{
    height: 20%;
    width: 100%;
    position: absolute;
    top: 0px;
}
.title{
    font-size: 40px;
    font-family: '黑体';
    font-weight: 600;
    letter-spacing: 10px;
}
.login-container{
    width: 100%;
    position: absolute;
    top: 20%;
    bottom: 20%;
}
.login-main{
    width: 1200px;
    height: 100%;
    margin: auto;
}
.system-title{
    font-size: 36px;
    margin-top: 5%;
    font-weight: bold;
    color: #666666;
}
.show{
    float: left;
    position: absolute;
    bottom: 0;
    left: 150px;
    top: 0;
    padding-top: 60px;
    width: 750px;
}
.show img{
    height: 100%;
    display: block;
    margin: 0 auto;
}

.login-titel{
    float: left;
    font-size: 50px;
    font-weight: 700;
    margin-top: 5%;
    color: #000;
    line-height: 300px;
    margin-right: 100px;
}

.box{
    width: 30%;
    padding: 20px 40px;
    float: right;
    background-color: rgb(255 255 255 / 50%);;
    border-radius: 5px;
    margin-top: 5%;
    float: left;
    margin-left: 400px;
}
.box .title{
    text-align: center;
    font-size: 18px;
    margin-bottom: 20px;
}
.login-btn{
    width: 100%;
    background-color: red;
    border: 0px;
}
.login-btn:hover{
    width: 100%;
    background-color: #ee9494;
    border: 0px;
}
.box >>> .el-select{
    width: 100%;
}
.login-user >>> .el-icon-login-user{
    background: url('~@/assets/images/user.png') no-repeat center left;
    margin-left: 5px;
}
.login-pwd >>> .el-icon-login-password{
    background: url('~@/assets/images/password.png') no-repeat center left;
    margin-left: 5px;
}
.login-footer{
    position: absolute;
    bottom: 0px;
    height: 20%;
    width: 100%;
    text-align: center;
    color: #999999;
    padding-top: 20px;
    font-size: 14px;
    box-sizing: border-box;
    background-color: #F0F0EE;
}
a{
    text-decoration: none;
    color: red;
    float: right;
    font-size: 18px;
}
</style>