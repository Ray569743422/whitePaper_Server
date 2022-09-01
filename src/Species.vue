<template>
  <div style="margin-top:120px;">
  <h1>Species</h1>
    <div>
    <el-row>
        <el-col :span="6"><img src="./assets/species/01.png" style="width:250px;height:350px;" @click="jumpDataBroSc"></el-col>
        <el-col :span="6"><img src="./assets/species/02.png" style="width:250px;height:350px;" @click="jumpDataBroDa"></el-col>
        <el-col :span="6"><img src="./assets/species/03.png" style="width:250px;height:350px;"></el-col>
        <el-col :span="6"><img src="./assets/species/04.png" style="width:250px;height:350px;"></el-col>
    </el-row>
    <el-row>
        <el-col :span="6"><img src="./assets/species/05.png" style="width:250px;height:350px;"></el-col>
        <el-col :span="6"><img src="./assets/species/06.png" style="width:250px;height:350px;"></el-col>
        <el-col :span="6"><img src="./assets/species/07.png" style="width:250px;height:350px;"></el-col>
        <el-col :span="6"><img src="./assets/species/08.png" style="width:250px;height:350px;"></el-col>
    </el-row>
    <el-row>
        <el-col :span="6"><img src="./assets/species/09.png" style="width:250px;height:350px;"></el-col>
        <el-col :span="6"><img src="./assets/species/10.png" style="width:250px;height:350px;"></el-col>
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
                 jumpDataBroSc(){
                   this.$emit('updataGlobal', "Schmidtea mediterranea");
                    
                 },
                 jumpDataBroDa(){
                    this.$emit('updataGlobal', "Danio rerio");
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
