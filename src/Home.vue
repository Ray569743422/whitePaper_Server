<template>
  <div>
    <p>Single Cell White Paper by BGI-Qingdao</p>
    <div>
       <p  > Please select one species:</p>
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
            curr_selected_sample : "Zebrafish",
            samples : [ { index:1, value:"Planarian",},
                    { index:2, value:"Zebrafish",},
                    { index:3, value:"Salamander",},
                    { index:4, value:"Shark",},
                    { index:5, value:"Whale",}, ],
        };
    },
    methods: {
       selectSample(item){
         var msg = {};
         msg.sample = item;
         msg.jump = '4';
         this.$emit('updataGlobal',msg)
       },
    },
};
</script>
