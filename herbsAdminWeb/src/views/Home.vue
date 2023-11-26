<template>
    <el-container class="container">
        <el-header>
                <Navbar ></Navbar>
            </el-header>
        <el-container>
            <Sidebar  @handleMenuItem="handleMenuItem"></Sidebar>
            <el-main>
                <el-breadcrumb separator-class="el-icon-arrow-right">
                    <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
                    <el-breadcrumb-item>{{menuName}}</el-breadcrumb-item>
                </el-breadcrumb>
                <router-view class="rv"></router-view>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
    import Sidebar from "@/components/Sidebar";
    import Navbar from "@/components/Navbar";
    export default {
        name: "Home",
        components:{
            Sidebar,Navbar
        },
        data(){
          return {
              isCollapse:false,
              menuName:'',
          };
        },
        methods:{
            handleMenuItem(item){
                this.menuName = item.name
                this.$forceUpdate();
            }
        }
    }
</script>

<style scoped>
.container{
    width: 100%;
    height: 100%;
}
.el-header{
    width: 100%;
    height: 100px !important;
    padding: 0px !important;
}
.el-main{
    float: left;
    width: calc(100% - 250px) ;
    padding: 0px !important;
    background-color: #f2f2f2;
    overflow: none;
}
.el-breadcrumb{
    background-color: #ffffff;
    height: 40px;
    line-height: 40px;
    border-bottom: 1px solid #e2dddd;
    padding-left: 10px;
    box-sizing: border-box;
}
.rv{
    background-color: #ffffff;
    margin: 10px;
    padding: 10px;
    border-radius: 4px;
}
</style>