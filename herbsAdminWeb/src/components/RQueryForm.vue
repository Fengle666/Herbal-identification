<template>
    <el-form :inline="true" :model="form">
        <template v-for="(item,index) in items">
            <template v-if="['text','number'].indexOf(item.type) !=-1">
                <el-form-item :label="item.label" :key="index">
                    <el-input v-model="form[item.name]" :placeholder="item.placeholder"></el-input>
                </el-form-item>
            </template>
            <template v-if="['select'].indexOf(item.type) !=-1">
                <el-form-item :label="item.label" :prop="item.name" :key="index">
                    <el-select clearable  v-model="form[item.name]" :placeholder="item.placeholder">
                        <el-option
                                v-for="item in item.options"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                        </el-option>
                    </el-select>
                </el-form-item>
            </template>
            <template v-if="['treeselect'].indexOf(item.type) !=-1">
                <el-form-item :label="item.label" :prop="item.name" :key="index">
                    <treeselect style="width: 260px" v-model="form[item.name]" noChildrenText="暂无数据" :placeholder="item.placeholder" :options="item.options" />
                </el-form-item>
            </template>
        </template>
        <el-form-item>
            <el-button @click="$emit('search')" icon="el-icon-search">查询</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
    import Treeselect from '@riophae/vue-treeselect'
    import '@riophae/vue-treeselect/dist/vue-treeselect.css'
    export default {
        name: "RQueryForm",
        components: { Treeselect },
        props:{
            items:{
                type:Array,
                default:()=>{}
            },
            form:{
                type:Object,
                default:()=>{}
            }
        },
    }
</script>

<style scoped>

</style>