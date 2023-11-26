<template>
    <div>
        <el-form  ref="form" :rules="rules"  :model="form" label-width="100px">
            <template v-for="(item,index) in items">
                <el-row :key="index">
                    <el-col :span="24">
                        <template v-if="['text','password','number','email'].indexOf(item.type) != -1">
                            <el-form-item :label="item.label" :prop="item.prop">
                                <el-input :type="item.type" v-model="form[item.name]" :placeholder="item.placeholder"></el-input>
                            </el-form-item>
                        </template>
                        <template v-if="['select'].indexOf(item.type) != -1">
                            <el-form-item :label="item.label" :prop="item.prop">
                                <el-select v-model="form[item.name]" :placeholder="item.placeholder">
                                    <el-option
                                            v-for="item in item.options"
                                            :key="item.value"
                                            :label="item.label"
                                            :value="item.value">
                                    </el-option>
                                </el-select>
                            </el-form-item>
                        </template>

                        <template v-if="['treeselect'].indexOf(item.type) != -1">
                            <el-form-item :label="item.label" :prop="item.prop">
                                <treeselect v-model="form[item.name]" noChildrenText="暂无数据" :placeholder="item.placeholder" :options="item.options" />
                            </el-form-item>
                        </template>

                        <template v-if="['switch'].indexOf(item.type) != -1">
                            <el-form-item :label="item.label" :prop="item.prop">
                                <el-switch
                                        active-text="启用"
                                        inactive-text="停用"
                                        active-value="1"
                                        inactive-value="0"
                                        v-model="form[item.name]"
                                        active-color="#13ce66">
                                </el-switch>
                            </el-form-item>
                        </template>

                        <!-- <template v-if="['area'].indexOf(item.type) != -1">
                            <el-form-item :label="item.label" :prop="item.prop">
                                <mavon-editor v-model="form[item.name]"/>
                            </el-form-item>
                        </template> -->

                        <template v-if="['date'].indexOf(item.type) != -1">
                            <el-form-item :label="item.label" :prop="item.prop">
                                <el-date-picker
                                        v-model="form[item.name]"
                                        type="date"
                                        value-format="yyyy-MM-dd"
                                        placeholder="选择日期时间">
                                </el-date-picker>
                            </el-form-item>
                        </template>

                        <template v-if="['file'].indexOf(item.type) != -1">
                            <el-form-item :label="item.label" :prop="item.prop">
                               <input type="file" @change="getImageFile" id="img">
                            </el-form-item>
                        </template>

                        
                        <template v-if="['fileWenjian'].indexOf(item.type) != -1">
                            <el-form-item :label="item.label" :prop="item.prop">
                                <el-upload
                                        class="upload-demo"
                                        action="string"
                                        :data="{name:item.name}"
                                        :http-request="uploadWenjian"
                                        :before-upload="beforeUploadWenjian"
                                        :limit="1">
                                    <el-button size="small" type="primary">点击上传</el-button>
                                    <div slot="tip" class="el-upload__tip">只能上传doc/docx文件，且不超过20M</div>
                                </el-upload>
                            </el-form-item>
                        </template>
                    </el-col>
                </el-row>
            </template>
            <el-row>
                <el-form-item style="text-align: center">
                    <el-button icon="el-icon-refresh-right" @click="resetField" type="primary">重置</el-button>
                    <el-button icon="el-icon-s-claim" @click="save" type="primary">保存</el-button>
                </el-form-item>
            </el-row>
        </el-form>
    </div>
</template>

<script>
    import Treeselect from '@riophae/vue-treeselect'
    import '@riophae/vue-treeselect/dist/vue-treeselect.css'
    import request from '@/utils/request'

    export default {
        name: "RForm",
        components: { Treeselect },
        props:{
            rules:{
                type:Object,
                default:()=>{}
            },
            form:{
                type:Object,
                default:()=>{}
            },
            save:{
                type:Function,
                default:()=>{}
            },
            items:{
                type:Array,
                default:()=>{}
            }
        },
        data(){
            return{
            }
        },
        mounted() {
        },
        methods:{
            validateForm(){
                let flag = false;
                this.$refs['form'].validate(valid=>{
                    if(valid){
                        flag = true;
                    }
                })
                return flag;
            },
            resetField(){
                this.$refs['form'].resetFields();
            },
            uploadImg(param){
                const formData = new FormData();
                formData.append("file",param.file);
                //调用文件上传
                request({url:'upload',method:'post',data:formData}).then(res=>{
                    this.form[param.data.name] = res.data;
                });
            },
            getImageFile:function(e, item) {
              let file = e.target.files[0];
              console.log(item);
              this.form.image = file;
            },
            //上传之前的验证
            beforeUpload(file){
                const isIMAGE = (file.type === 'image/jpeg')|| (file.type === 'image/jpg') || (file.type === 'image/png');
                const isLt2M = file.size / 1024 / 1024 < 2;
                if (!isIMAGE) {
                    this.$message.error('上传头像图片只能是 JPG/JPEG/PNG 格式!');
                }
                if (!isLt2M) {
                    this.$message.error('上传头像图片大小不能超过 2MB!');
                }
                return isIMAGE && isLt2M;
            },
            uploadWenjian(param){
                const formData = new FormData();
                formData.append("file",param.file);
                //调用文件上传
                request({url:'upload',method:'post',data:formData}).then(res=>{
                    this.form[param.data.name] = res.data;
                });
            },
            beforeUploadWenjian(file){
                console.log(file);
                const isIMAGE = (file.type === 'application/msword')|| (file.type === 'application/vnd.openxmlformats-officedocument.wordprocessingml.document');
                const isLt2M = file.size  / 1024 / 1024 < 20;
                if (!isIMAGE) {
                    this.$message.error('上传文件只能是 doc/docx 格式!');
                }
                if (!isLt2M) {
                    this.$message.error('上传文件大小不能超过 20MB!');
                }
                return isIMAGE && isLt2M;
            }
        }
    }
</script>

<style scoped>

</style>