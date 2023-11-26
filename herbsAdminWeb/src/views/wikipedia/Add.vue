<template>
    <el-dialog title="新建" width="70%"  :visible.sync="param.visible" @close="param.close" :close-on-click-modal="false">
        <el-form ref="form" :model="form"  label-width="100px" :rules="rules">
            <el-form-item label="中草药名称" prop="name">
                <el-input v-model="form.name" placeholder="请输入中草药名称"></el-input>
            </el-form-item>
            <el-form-item label="图片">
            <input type="file" @change="getImageFile" id="img">
          </el-form-item>
            <el-form-item label="描述" prop="describe">
                <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 2 }" placeholder="描述"  :size="10" v-model="form.describe"></el-input>
            </el-form-item>
            <el-form-item label="功效作用" prop="efficacy">
                <el-input type="textarea" :autosize="{ minRows: 3, maxRows: 5 }" placeholder="功效作用"  :size="10" v-model="form.efficacy"></el-input>
            </el-form-item>
            <el-form-item label="生长环境" prop="environment">
                <el-input type="textarea" :autosize="{ minRows: 3, maxRows: 5 }" placeholder="生长环境"  :size="10" v-model="form.environment"></el-input>
            </el-form-item>
            <el-form-item label="栽培技术" prop="cultivation">
                <el-input type="textarea" :autosize="{ minRows: 3, maxRows: 5 }" placeholder="栽培技术"  :size="10" v-model="form.cultivation"></el-input>
            </el-form-item>
            <el-form-item style="text-align: center;"><el-button class="addroomtj" @click="save" type="danger">提交</el-button></el-form-item>
        </el-form>
    </el-dialog>
</template>
<script>
import local from "@/store/localstore";
import request from '@/utils/request'
export default {
    name: "Add",
    props:{
        param:{
            type:Object,
            default:()=>{}
        }
    },
    data(){
        return{
            form:{
                name:'',
                describe:'',
                efficacy:'',
                environment:'',
                cultivation:'',
                image:'',
            },
            options:[
                ],
            rules:{
            }
        }
    },
    mounted() {
    
    },
    methods:{
        save(){
            let flag = this.$refs['form'].validate();
                if(flag){
                    let data = new FormData();
                    data.append('name', this.form.name)
                    data.append('describe', this.form.describe)
                    data.append('efficacy', this.form.efficacy)
                    data.append('environment', this.form.environment)
                    data.append('cultivation', this.form.cultivation)
                    data.append('image', this.form.image)
                    request({url:'wikipedia/wikipedia/',method:'post',data}).then(res=>{
                        this.$message({
                              message: '创建成功！！！',
                              type: 'success'
                            });
                        console.log(this.res);
                        this.param.close();
                        this.param.callback();
                    })
                }
        },
        // 上传图片
        getImageFile:function(e) {
              let file = e.target.files[0];
              console.log(file);
              this.form.image = file;
              console.log(this.form.image);
        },
    }
}
</script>

<style scoped>
.addroomtj{
    text-align: center;
}
.avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
.avatar-uploader .el-upload:hover {
border-color: #409EFF;
}
.avatar-uploader-icon {
font-size: 28px;
color: #8c939d;
width: 178px;
height: 178px;
line-height: 178px;
border: 1px solid #ccc;
text-align: center;
}
.avatar {
width: 178px;
height: 178px;
display: block;
}
</style>