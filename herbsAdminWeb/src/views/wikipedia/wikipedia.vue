<template>
    <div>
        <r-query-form :form="form" :items="items" @qinkong="qingkong" @search="search"></r-query-form>
        <div class="btn-panel">
            <el-button size="small" type="primary" @click="create" >新增</el-button>
            <el-button size="small" type="warning"  @click="update">修改</el-button>
            <el-button size="small" type="danger" @click="del">删除</el-button>
        </div>
        <r-table ref="mutipleTable" :tableData="tableData" :tableCols="tableCols">
             <template slot="slot_imag1" slot-scope="scope">
                <template v-if="scope.data.image==null">
                  <span>暂无照片</span>
                </template>
                <el-image 
                    v-else
                    class="eimages"
                    :src="scope.data.image"
                    :preview-src-list="srcList"
                    >
                </el-image>
            </template>
        </r-table>
        <r-pagination :page="page" :page-size="pageSize" :total="total" @handleCurrentChange="handleCurrentChange"></r-pagination>
        <Add v-if="add.visible" :param="add"></Add>
        <Edit v-if="edit.visible" :param="edit"></Edit>
    </div>
</template>

<script>
    import RTable from "@/components/RTable";
    import request from '@/utils/request'
    import RPagination from "@/components/RPagination";
    import {message} from "@/utils/message";
    import RQueryForm from "@/components/RQueryForm";
    import Add from "./Add";
    import Edit from "./Edit";
import { Loading } from 'element-ui';
    export default {
        name: "Wenzhang",
        components:{Edit, Add, RQueryForm, RPagination,RTable},
        data(){
            return{
                total:0,
                page:1,
                pageSize:5,
                tableData:[],
                srcList:[],
                tableCols:[
                    {prop:'id', label:'ID', width:80},
                    {prop:'name', label:'中草药名称'},
                    {prop:'oviews', label:'浏览量'},
                    {prop:'image', label:'图片', slot:"slot_imag1"},
                ],
                form:{
                    name:'',
                },
                items:[
                    {type:'text',label:'中草药名称',name:'name',placeholder:'按关键字查询'},
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
                this.list(params);
            },
            search(){
                this.list(this.form);
            },
            list(params){
                request({url:'/wikipedia/wikipedia/?page='+this.page,method:'get',params}).then(res=>{
                    this.tableData= res.results;
                    this.total = res.count;
                    this.tableData.forEach((item)=>{
                            this.srcList.push(item.image)
                        })
                    })
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

            close(){
                this.add.visible = false;
                this.edit.visible = false;  
            },

            del(){
                let selection = this.$refs['mutipleTable'].selection;
                if(selection.length>0){
                    this.$confirm('确定要删除吗','删除提示').then(()=>{
                        let arr = selection.map(item=>item.id);
                        for (let property in arr) {
                            request({url:'wikipedia/wikipedia/'+arr[property],method:'delete'}).then(res=>{
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
            qingkong(){
                this.form.articleName = null;
                this.form.type = null;
                this.list({})
            }
        }
    }
</script>

<style scoped>
.el-pagination {
    text-align: center;
}

.el-image {
    width: 60px;
    height: 60px;
    margin: 10px 0px;
}
</style>