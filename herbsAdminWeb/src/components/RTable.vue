<template>
    <el-table
            :data="tableData"
            border
            @selection-change="handleSelectionChange"
            :cell-style="{height:'40px',padding:'0px'}"
            :header-cell-style="{background:'#f2f2f2',height:'40px',padding:'0px'}"
            style="width: 100%">
        <el-table-column
                v-if="isSelection"
                type="selection"
                width="40">
        </el-table-column>
        <el-table-column
                v-for="(item,index) in tableCols"
                :prop="item.prop"
                :label="item.label"
                :width="item.width"
                :key="index"
                align="center"
                >
            <template slot-scope="scope">
                <slot v-if="item.slot" :name="item.slot" :data="scope.row"></slot>
                <span v-else>{{scope.row[item.prop]}}</span>
            </template>
        </el-table-column>
    </el-table>
</template>

<script>
    export default {
        name: "RTable",
        props:{
            tableData:{
                type:Array
            },
            tableCols:{
                type:Array
            },
            isSelection:{
                type:Boolean,
                default:true,
            }
        },
        data(){
          return{
              selection:[],
          }
        },
        methods:{
            handleSelectionChange(selection){
                this.selection = selection;
            }
        }
    }
</script>

<style scoped>

</style>