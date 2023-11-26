<template>
<div class="main">
    <div class="box1">
        <div class="tite">
            <span>统计各中草药的浏览量</span>
        </div>
        <ve-histogram :settings="settngs" :data="chartDate"></ve-histogram>
         
    </div>
    <div class="box2">
        <div class="tite">
            <span>统计各中草药的浏览量分布</span>
        </div>
        <ve-ring :settings="settngs" :data="chartDate"></ve-ring>
         
    </div>
</div>
</template>

<script>
import request from '@/utils/request'
export default {
    name:"Tongji",
    data() {
        this.settngs ={
           metrics: ['浏览'],  
            dimension: ['中草药名称'],
            label: {
                show: true,
                position: 'outside',
            }
        }
      return {
          daipay:null,
          tuidan:null,
          wanchen:null,
          chartData: {
                columns: ["中草药名称", "浏览"],
                rows: [
                
                ]
            },
            chartDate:{
                columns:["浏览","中草药名称"],
                rows:[

                ]
            }
      }
      },
    created(){
        this.$forceUpdate();
    },
    mounted(){
       this.ordersList()
       this.$forceUpdate();
    },
    methods:{
      ordersList(){
        // http://127.0.0.1:8000/crops/count/
             request({url:'wikipedia/wikipedia/',method:'get',params:{}}).then(res=>{
                console.log(res);
                let arr = res.results;
                for(var i=0; i < arr.length; i++){
                    this.chartDate.rows.push({"中草药名称":res.results[i].name,"浏览":res.results[i].oviews})
                }
                console.log(this.chartDate.rows);
                this.$forceUpdate();
            })
        },
              
    }
}
          
    


</script>

<style scoped>
*{
    margin: 0px;
    padding: 0px;
}

.rv {
    background-color: #ffffff00;
}

.main  {
    height: 100%;
     background-color: #ffffff00;
}

.box1{
    margin-top: 10px;
    width: 700px;
    float: left;
    height: 600px;
    margin-left: 10px;
    background-color:#fff;
}
.box2{
    margin-top: 10px;
    width: 700px;
    float: left;
    height: 600px;
    margin-left: 10px;
    background-color:#fff;
}
.tite{
    line-height: 100px;
    font-size: 30px;
    text-align: center;
    width: 100%;
    margin-left: 0px;
    height: 100px;
    border-bottom: 1px solid rgb(199, 196, 196);
    box-sizing: border-box;
}
.tite span {
    padding-left: 20px;
}
.buttons{
    /* align-items: center; */
    width: 90%;
    height: 40px;
    text-align: center;
    padding: 10px;
}
.el-button+.el-button{
    margin-left: 0px;
}
.el-button{
    width: 100px;
    margin: 10px;
    height: 40px;

}

.main div #test{
    /* align-items: center; */
    width: 90%;
    height: 300px;
    margin-left: 20px;
    text-align: center;
}
.main div #yuantu{
    /* align-items: center; */
    width: 90%;
    height: 300px;
    margin-left: 20px;
    text-align: center;
}

.main div #nianxiao{
    /* align-items: center; */
    width: 90%;
    height: 300px;
    margin-left: 20px;
    text-align: center;
}
.tongjiList{
    display: flex;
    justify-content: space-around;
    padding-top: 20px;
}
.tongjiItem{
    width: 160px;
    height: 70px;
    border:  1px solid rgba(204, 204, 204, 0.233);
    background-color: rgb(255 255 255);
    text-align: center;
    font-size: 20px;
    color: rgb(255, 0, 0);
    font-weight: 600;
    margin-bottom: 28px;
}
.Tongjititile{
    margin-top: 10px;
    margin-bottom: 5px;
    text-align: center;
    font-size: 16px;
    font-weight: 100;
    color: rgba(0, 0, 0, 0.836);
}
</style>