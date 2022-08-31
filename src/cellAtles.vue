<template>
  <div style="margin-top:120px;">
  <h1>CellAtlas</h1>
    <div>
    <el-row>
        <el-col :span="6"><div style="border:1px solid;;border-radius:25px;border-color: #ccc;width:250px;height:300px;margin-left:60px"><img src="./assets/cellAtlas/01.png" style="width:200px;height:200px;"><p style="margin-left:-15px">Denio rerio</p><el-button type="primary" style="margin-left:-15px" v-on:click="jumpUmap">Details</el-button></div></el-col>
        <el-col :span="6"><div class="image" /><img src="./assets/test2.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="6"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="6"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
    </el-row>
    <el-row>
       <el-col :span="6"><div class="image" /><img src="./assets/test1.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;
 border-color: #4682B4"></el-col>
        <el-col :span="6"><div class="image" /><img src="./assets/test2.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="6"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="6"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
    </el-row>
    </div>
  </div>
</template>

<script>
export default {
    data(){
        return {}
    },
    methods: {
        jumpUmap(){
            this.$emit('updataGlobal', "Planarian");
        }
    }
}
</script>
<style>
.el-row {
    margin-bottom: 20px;
    }
.el-row:last-child {
    margin-bottom: 0;
    }
.el-col {
    border-radius: 4px;
    }
</style>
