<template>
    <div class="header">
        <span class="collapse">
            中草药识别系统
        </span>
        <div class="user-info">
            <i class="el-icon-full-screen" @click="handleFullScreen"></i>
            <el-dropdown  @command="handleCommand">
              <span class="el-dropdown-link">
                {{account}}<i class="el-icon-caret-bottom"></i>
              </span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="logout">
                        <i class="el-icon-s-unfold"></i>
                        退出登录
                    </el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
        </div>
    </div>
</template>

<script>

    import screenfull from "screenfull";
    import local from "@/store/localstore";
    export default {
        name: "Navbar",
        data(){
            return{
            }
        },
        computed:{
          account(){
              return local.getUserInfo().name
          }
        },
        methods:{
            handleCollapse(){
                this.$emit('handleCollapse');
            },
            handleFullScreen(){
                screenfull.toggle();
            },
            handleCommand(type){
                console.log(type)
                if(type === 'logout'){
                    this.$confirm('确定要退出吗？','退出提示',).then(()=>{
                        this.$router.push('/login');
                        local.clear()
                    }).catch(()=>{});
                }
                if(type === 'home'){
                    this.$router.push('/');
                }
            }

        }
    }
</script>

<style scoped>
.header{
    height: 100px;
    background-color: #ff0000;
    width: 100%;
    padding: 0px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.user-info {
    height: 100px;
    margin-left: auto;
    margin-right: 50px;
    width: 400px;
    padding-right: 20px;
    text-align: right;
    display: flex;
    justify-content: center;
    align-items: center;
}
.user-info>i{
    cursor: pointer;
    padding: 10px 15px;
    color: #ffffff;
}
.el-dropdown{
    margin-left: 10px;
}
.el-dropdown-link{
    color: #ffffff;
    cursor: pointer;
}
.collapse{
    cursor: pointer;
    padding:0px 500px;
    color: #ffffff;
    font-size: 40px;
}
</style>