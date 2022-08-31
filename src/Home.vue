<template>
  <div>
  <h1>test</h1>
    <el-row>
        <el-col :span="8"><div class="image" /><img src="./assets/test1.jpg" style="width:400px;height:400px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="8"><div class="image" /><img src="./assets/test2.jpg" style="width:400px;height:400px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
        <el-col :span="8"><div class="image" /><img src="./assets/test3.jpg" style="width:400px;height:400px;border-style: dashed;border-radius:25px;border-color: #4682B4"></el-col>
    </el-row>
    <p>Single Cell White Paper by BGI-Qingdao</p>
    <div style="width:1450px;margin:auto;">
    <p style="text-align: justify; line-height: 24px;">Cattle have had a central role in the evolution of human cultures and are the most economically important of domesticated animal species. Until now, it formed nearly eight hundred of breeds with various traits. Here, we developed a comprehensive Bovine Genome Variation Database (BGVD) for providing six main functionalities: Gene Quick Search, Variation Search, Genomic Signature Search, Genome Browser, Alignment Search Tools (BLAT/BLAST) and Genome Coordinate Conversion Tool (LiftOver). In current version, BGVD contains 60,439,391 SNPs, 6,859,056 indels, and 76,634 CNV regions derived from 432 animals. And selective signatures were evaluated for eight cattle groups by using six methods (Pi, Hp, iHS, FST, XP-CLR and XP-EHH). Many external databases, such as NCBI, the UCSC Genome Browser, AnimalQTLdb, AmiGO 2 and KEGG were integrated into our browser. BGVD will be a useful archive for in-depth analysis in cattle biology and cattle breeding.</p>
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
