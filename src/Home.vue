<template>
  <div class="container" style="width:1503px;background-color:#526482">
    <div style="width:1503px;text-align:center"><img src='./assets/body.png' style="width:1380px"></div>
    <div style="width:1400px;margin:auto;">
    <p style="text-align:justify;line-height:24px;margin-top:-80px;font-size:25px;color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;Cattle have had a central role in the evolution of human cultures and are the most economically important of domesticated animal species. Until now, it formed nearly eight hundred of breeds with various traits. Here, we developed a comprehensive Bovine Genome Variation Database (BGVD) for providing six main functionalities: Gene Quick Search, Variation Search, Genomic Signature Search, Genome Browser, Alignment Search Tools (BLAT/BLAST) and Genome Coordinate Conversion Tool (LiftOver). In current version, BGVD contains 60,439,391 SNPs, 6,859,056 indels, and 76,634 CNV regions derived from 432 animals.</p>
    </div>
    <div>
       <p> Please select one species:</p>
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
<style>
</style>
