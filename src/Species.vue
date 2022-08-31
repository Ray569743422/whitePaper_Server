<template>
  <div style="margin-top:120px;">
  <h1>Species</h1>
    <div>
    <el-row>
        <el-col :span="6"><div class="image" /><img src="./assets/test1.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="6"><div class="image" /><img src="./assets/test2.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="6"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="6"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
    </el-row>
    <el-row>
        <el-col :span="6"><div class="image" /><img src="./assets/test1.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="6"><div class="image" /><img src="./assets/test2.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="6"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="6"><div class="image" /><img src="./assets/test3.jpg" style="width:200px;height:200px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
    </el-row>
    <el-select  v-model="curr_selected_sample" filterable placeholder="" @change="selectSample" >
        <el-option v-for="item in samples" :key="item.value"
        :label="item.label" :value="item.value">
        </el-option>
    </el-select>
    </div>
  </div>
</template>

<script>
export default {
    data(){
        return {
            curr_selected_sample:'',
            samples : [ { index:1, value:"Planarian",},
                    { index:2, value:"Zebrafish",},
                    { index:3, value:"Salamander",},
                    { index:4, value:"Shark",},
                    { index:5, value:"Whale",}, ],
        }
    },
    methods: {
                 selectSample(item){
                     self.curr_selected_sample = item;
                     this.$emit('updataGlobal',self.curr_selected_sample)
                 },
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
