<template>
    <div>
        <r-query-form :form="form" :items="items" @qinkong="qinkong" @search="search"></r-query-form>
        <div class="btn-panel">
            <el-button size="medium " type="success" icon="el-icon-plus" @click="create" >新增</el-button>
            <el-button size="medium " type="primary" icon="el-icon-edit" @click="update">修改</el-button>
            <el-button size="medium " type="danger" icon="el-icon-delete" @click="del">删除</el-button>
        </div>
        <r-table ref="mutipleTable" :tableData="tableData" :tableCols="tableCols">
            <template slot="slot_is_stats" slot-scope="scope">
                <el-switch 
                    v-model="scope.data.is_stats"
                    active-text="启用"
                    inactive-text="停用"
                    active-value="1"
                    inactive-value="0"
                    @change="switchState(scope.data)"
                    >
                    </el-switch>
            </template>
        </r-table>
        <r-pagination :page="page" :total="total" @handleCurrentChange="handleCurrentChange"></r-pagination>
        <Add v-if="add.visible" :param="add"></Add>
        <Edit v-if="edit.visible" :param="edit"></Edit>
    </div>
</template>

<script>
import Add from './Add'
import Edit from "./Edit";
import request from '@/utils/request'
import {message} from "@/utils/message";
import RTable from "@/components/RTable";
import RPagination from "@/components/RPagination";
import RQueryForm from "@/components/RQueryForm";
export default {
    name:"User",
    components: {RQueryForm, RPagination, Edit, Add,RTable},
    data(){
        return{
            total:0,
            page:1,
            tableData:[],
            srcList:[],
            tableCols:[
                {prop:'id', label:'ID', width:80},
                {prop:'username', label:'用户名'},
                {prop:'name', label:'用户昵称'},
                {prop:'password', label:'密码'},
                {prop:'is_stats', label:'启用状态',slot:"slot_is_stats"},
            ],
            form:{
                username:null,
            },
            items:[
                {type:'text',label:'用户名',name:'username',placeholder:'按用户名查询'},

            ],
            add:{
                visible:false,
                close:this.close,
                callback:this.search
            },
            edit:{
                visible:false,
                close:this.close,
                callback:this.search,
                form:null,
            },
        }
    },
    mounted() {
        this.list({})
    },
    methods:{
        handleCurrentChange(val){
            this.page = val;
            let params = this.form;
            params.page = this.page
            this.list(params);
        },
        search(){
            this.list(this.form);
        },
        qinkong(){
            this.form.username=null;
        },
        list(params){
            request({url:'/user/user/?page='+this.page,method:'get',params}).then(res=>{
                this.tableData= res.results;
                this.total = res.count;
                })
        },
        close(){
            this.add.visible=false;
            this.edit.visible=false;
        },
        create(){
            this.add.visible = true;
        },
        update(){
            let selection = this.$refs['mutipleTable'].selection;
            if(selection.length==1){
                this.edit.visible = true;
                this.edit.form = selection[0]
            }else{
                message.warning('请选择一条数据修改')
            }
        },
        del(){
            let selection = this.$refs['mutipleTable'].selection;
            if(selection.length>0){
                this.$confirm('确定要删除吗','删除提示').then(()=>{
                    let arr = selection.map(item=>item.id);
                    for (let property in arr) {
                        request({url:'user/user/'+arr[property],method:'delete'}).then(res=>{
                            this.search();
                        })
                    }
                    this.$message({
                        message: '删除成功！！！',
                        type: 'success'
                        });
                }).catch(()=>{})
            }else{
                message.warning('请选择要删除的数据')
            }
        },
        switchState(row) {
            // 修改启用状态
            console.log(row);
            request({url:'/user/user/'+row.id+'/',method:'put',data:row}).then(res=>{
                this.$message({
                    message: '修改成功！！！',
                    type: 'success'
                    });
                this.search();
                })
        },
    }
}
</script>

<style scoped>
.el-pagination {
    margin-top: 30px;
    text-align: center;
}
</style>