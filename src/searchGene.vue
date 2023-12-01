<template>
    <div style="width:100%">
    <!-- searchable header -->
    <el-row>
        <el-col :span="24">
             <el-input v-model="geneSymbol" placeholder="Enter name to search"></el-input>
             <el-button @click="searchMarkers" type="primary">Search</el-button>
             </el-col>
        </el-col>
    </el-row>
    <!-- searchable header end -->
    <el-row>
        <el-table :data="tableData" >
              <el-table-column prop="geneSymbol" label="GeneSymbol"></el-table-column>
              <el-table-column prop="gene" label="Gene"></el-table-column>
              <el-table-column prop="browser" label="Data_Browser">
                  <template slot-scope="scope">
                      <el-button @click="jumpDataBroDa(scope.row.gene)" type="text">{{ scope.row.browser }}</el-button>
                  </template>
              </el-table-column>
        </el-table>
    </el-row>
    </div>
</template>

<script>

import DataBrowser from './DataBrowser.vue'

export default {
    data(){
      return {
        geneSymbol: '',
        tableData: []
      }
    },
    methods: {
        searchMarkers(){
            var self = this;
            let params = new URLSearchParams({
                geneSymbol: this.geneSymbol,
            });

            this.$axios.post('https://www.bgiocean.com/white_paper/api/searchGene', params)
                .then(res => {
                        self.create_table_data(res.data['ret']);
                        console.log(self.tableData);
                        });
        },

        jumpDataBroDa(gene) {
            console.log(gene);
            this.$emit('updataGlobal', {species: "Schmidtea mediterranea",gene: gene});
        },

        create_table_data(data){
            
            var self = this;

            self.tableData = [];

            for (var i =0; i<data.length; i++){
                const raw_0=data[i][0];
                const raw_1=data[i][1];
                const raw_2=data[i][2];
                self.tableData.push({
                    geneSymbol: raw_0, 
                    gene: raw_1,
                    browser: raw_2,
                    });
            }
        }
    },  
}
</script>
<style>
</style>
