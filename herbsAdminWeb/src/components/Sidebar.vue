<template>
    <el-aside>
        <el-menu
            background-color="#000000"
            text-color="#fff"
            active-text-color="#fff"
            style="border: 0px;width: 250px;"
            router
            :default-active="active">
            <el-menu-item @click="handleMenuItem(item)" :index="item.url" v-for="(item,index) in menus" :key="index">
                <span slot="title">{{item.name}}</span>
            </el-menu-item>
        </el-menu>

    </el-aside>
</template>

<script>
    export default {
        name: "Sidebar",
        data(){
            return {
                menus:[
                    {'url':'adminUser','name':'用户管理'},
                    {'url':'wikipedia','name':'中草药信息管理'},
                    {'url':'tongji','name':'信息统计'},
                ],
                active:'',
            }
        },
        methods:{
            handleMenuItem(item){
                this.$emit('handleMenuItem',item)
            }
        }
    }
</script>

<style scoped>
.topheader{
    background-color: #000000   ;
    color: rgb(0, 0, 0);
    line-height: 50px;
    height: 50px;
    width: 250px;
    padding-left: 25px;
}
.topheader span{
    margin-left: 7px;
}
.el-aside{
    background-color: #000000;
        text-align: center;
        font-size: 20px;
    transition: width .2s;
    overflow-x: hidden;
    width: 250px !important;
    float: left;
}
</style>