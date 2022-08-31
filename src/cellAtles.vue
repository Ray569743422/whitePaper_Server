<template>
  <div>
  <h1>cell</h1>
    <div>
    <el-row>
        <el-col :span="4"><div class="image" /><img src="./assets/test1.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="4"><div class="image" /><img src="./assets/test2.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="4"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="4"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="4"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="4"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
    </el-row>
    <el-row>
       <el-col :span="4"><div class="image" /><img src="./assets/test1.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;
 border-color: #4682B4"></el-col>
        <el-col :span="4"><div class="image" /><img src="./assets/test2.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="4"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="4"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="4"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="4"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
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
