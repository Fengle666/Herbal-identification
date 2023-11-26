<template>
    <el-dialog title="修改" :visible.sync="param.visible" @close="param.close" :close-on-click-modal="false">
        <r-form ref="myForm" :rules="rules" :form="form" :items="items" :save="save"></r-form>
    </el-dialog>
</template>

<script>
    import RForm from "@/components/RForm";
    import request from '@/utils/request'
    export default {
        name: "Edit",
        components: {RForm},
        props:{
            param:{
                type:Object,
                default:()=>{}
            }
        },
        data(){
            return{
                form:{
                    username:'',
                    password:null,
                    name:'',
                    is_stats:null,
                },
                rules:{
                    username:[{required:true,message:'用户名能为空'}],
                    password:[{required:true,message:'密码不能为空'}],
                    name:[{required:true,message:'用户昵称不能为空'}],
                    is_stats:[{required:true,message:'必填项不能为空'}],
                },
                items:[
                    {type:'text',label:'用户名',prop:'username',name:'username',placeholder:'请录入用户名'},
                    {type:'password',label:'密码',prop:'password',name:'password',placeholder:'请录入密码'},
                    {type:'text',label:'用户昵称',prop:'name',name:'name',placeholder:'请录入用户昵称'},
                    {type:'switch',label:'启用状态',prop:'is_stats',name:'is_stats',placeholder:'请录入启用状态'},
                ]
            }
        },
        mounted() {
            this.form = JSON.parse(JSON.stringify(this.param.form))
        },
        methods:{
            save(){
                let flag = this.$refs['myForm'].validateForm();
                if(flag){
                    let data = new FormData();
                    data.append('username', this.form.username)
                    data.append('name', this.form.name)
                    data.append('password', this.form.password)
                    data.append('is_stats', this.form.is_stats)
                    request({url:'user/user/'+this.form.id+'/',method:'put',data}).then(res=>{
                        this.$message({
                              message: '修改成功！！！',
                              type: 'success'
                            });
                        console.log(this.res);
                        this.param.close();
                        this.param.callback();
                    })
                }
        },
        }
    }
</script>

<style scoped>

</style>
