<template>
  <div id='app'>
    <title>Cluster Table</title>

    <div style="width:1503px;">
        <!-- searchable header -->
        <p class="inline_item" > Species:</p>
        <el-select class="inline_item" v-model='currentSpecies' filterable placeholder="species">
          <el-option v-for="item in Ssamples" :key="item.name" :label="item.label" :value="item.name">
          </el-option>
        </el-select>
        
        <p class="inline_item" > Celltype:</p>
        <el-select class="inline_item" v-model='currentCellType' filterable placeholder="all cell types" @change='selectCellType'>
          <el-option v-for="item in samples" :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>

        <p class="inline_item" > Search Gene:</p>
        <el-input  class="inline_item" v-model='inputGene' style='width:150px;' placeholder="contig id" @change='searchGene'></el-input>
        <!-- searchable header end -->

        <!-- cluster table content -->
        <el-table ref="clusterTable" 
        :show-header='true' class="table" 
        :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
        :highlight-current-row='true'
        :header-cell-style="{color:'#EEF1F6',background:'#021C57'}"
        stripe
        @row-click='handleRow'>
            <el-table-column prop='Gene' label='Gene'></el-table-column>
            <el-table-column prop='Best-blast hit' label='Best-blast hit'></el-table-column>
            <el-table-column prop='Accession' label='Accession'></el-table-column>
            <el-table-column prop='e-value' label='e-value'></el-table-column>
            <el-table-column prop='Species' label='Organism'></el-table-column>
            <el-table-column prop='log fold enrichment' label='log fold enrichment'></el-table-column>
            <el-table-column prop='cluster enriched in' label='cluster enriched in'></el-table-column>
            <el-table-column prop='Adjusted p-value' label='Adjusted p-value'></el-table-column>
            <el-table-column prop='AUC' label='AUC'></el-table-column>
            <el-table-column prop='Power' label='Power'></el-table-column>
            <el-table-column prop='cell_type' label='Associated cell type class'></el-table-column>
        </el-table>

        <el-pagination layout="total,sizes, prev, jumper, next"
        :total="this.tableData.length"
        :current-page="currentPage"
        @current-change="handleCurrentChange" @size-change="handleSizeChange"
        :page-sizes="[10,15,20]" :page-size="pageSize" :current-page.sync="currentPage">
        </el-pagination>
        <!-- cluster table content -->
    </div>


  </div>
</template>

<script>
    import $ from 'jquery';

    var species = require('./conf/species.js');

    var GENE_DATA_URL = "http://www.bgiocean.com:8020/code/index.php/WhitePaper/getGeneData";

    export default {
        props:['G_sample', 'G_gene'],
        data(){
            return {
                Ssamples: species,
                cellTypes: [],
                species:'Planarian',
                options: [
                        {value:'Amphimedon queenslandica',label:'Amphimedon queenslandica',},
                        {value:'Astyanax mexicanus',label:'Astyanax mexicanus',},
                        {value:'Branchiostoma floridae',label:'Branchiostoma floridae',},
                        {value:'Ciona intestinalis',label:'Ciona intestinalis',},
                        {value:'Ciona robusta(intestinalis Type A)',label:'Ciona robusta(intestinalis Type A)',},
                        {value:'Ciona savignyi',label:'Ciona savignyi',},
                        {value:'Clytia medusa',label:'Clytia medusa',},
                        {value:'Cynoglossus semilaevis',label:'Cynoglossus semilaevis',},
                        {value:'Danio rerio',label:'Danio rerio',},
                        {value:'Dreissena rostriformis',label:'Dreissena rostriformis',},
                        {value:'Hydra vulgaris',label:'Hydra vulgaris',},
                        {value:'Lytechinus variegatus',label:'Lytechinus variegatus',},
                        {value:'Mnemiopsis leidyi',label:'Mnemiopsis leidyi',},
                        {value:'Nematostella vectensis',label:'Nematostella vectensis',},
                        {value:'Octopus vulgaris',label:'Octopus vulgaris',},
                        {value:'Schistosoma mansoni',label:'Schistosoma mansoni',},
                        {value:'Schmidtea mediterranea',label:'Schmidtea mediterranea',},
                        {value:'Spongilla lacustris',label:'Spongilla lacustris',},
                        {value:'Strongylocentrotus purpuratus',label:'Strongylocentrotus purpuratus',},
                        {value:'Stylophora pistillata',label:'Stylophora pistillata',},
                        {value:'Trachemys scripta elegans',label:'Trachemys scripta elegans',},
                        {value:'Trichoplax adhaerens',label:'Trichoplax adhaerens',},
                        {value:'Xenia sp.',label:'Xenia sp.',},
                        {value:'Xenopus laevis',label:'Xenopus laevis',},
                        {value:'Xenopus tropicalis',label:'Xenopus tropicalis',},
                        ],
                aucCutoff: 0,
                currentGene: null,
                inputGene: null,
                currentCellType: null,
                tableData: [],
                allTableData: [],
                pageSize:15,
                currentPage:1,
            };
        },
        methods: {

            getMarkerDetails(url, params){
                var self = this;
                self.$axios.post(url, params)
                    .then(res=>{
                        self.res = res.data['ret'];
                        self.create_organ_type(self.res);
                        });
            },

            create_cell_type(data){
                var self = this;
                let types = [];
                self.cellTypes = [];                                                                            
                for (var i = 0; i < data.length; i++){
                    var innerArray = data[i];
                    if (innerArray.length >= 3) {
                        types.push(innerArray[3]);
                    }
                }
                types = Array.from(new Set(types));

                for (var i = 0; i < types.length; i++){
                    self.cellTypes.push(types[i])
                }
            },

            selectCellType(item){

                var self = this;
 
                if (this.currentCellType == 'All'){
                    this.tableData = this.allTableData;
                    return
                };
 
                // change table data
                var new_tableData = [];
                
                var arrayLength = this.allTableData.length;
 
               for (var i = 0; i < arrayLength; i++) {
                   if (this.allTableData[i]['Associated cell  type class'] == this.currentCellType){
                       new_tableData.push(this.allTableData[i]);
                   }
               };
 
               this.tableData = new_tableData;
            },

            selectSample(item){

                if(item == this.currentSpecies)
                    return

                this.currentSpecies = item;

                if (this.currentSpecies == 'All'){
                    this.tableData = this.allTableData;
                    return
                };

                // change table data
                var new_tableData = [];

                var arrayLength = this.allTableData.length;

                for (var i = 0; i < arrayLength; i++) {
                    if (this.allTableData[i]['Species'] == item){
                        new_tableData.push(this.allTableData[i]);
                    }
                };

                this.tableData = new_tableData;
            },

         searchGene(){
                
             var new_tableData = [];

             var arrayLength = this.allTableData.length;

             for (var i = 0; i < arrayLength; i++) {
                 if (this.allTableData[i]['Contig'].includes(this.inputGene)){
                     new_tableData.push(this.allTableData[i]);
                 }
             };

             this.tableData = new_tableData;
            },

            handleSizeChange (size) {
                this.pageSize = size;
            },

            handleCurrentChange (currentpage){
                this.currentPage = currentpage;
            },

             chandleRow(row,event,column){
                this.currentGene = row.Contig;
                console.log(this.currentGene);
            }
        },

        mounted(){
           
            if(this.G_sample != '' ){
                this.species = this.G_sample;
            }else{
                this.species = 'All';
            }

            if(this.species && this.geneNames) {
                this.params = new URLSearchParams({
                    species: this.species,
                    });
            };

            this.getMarkerDetails(GENE_DATA_URL, this.species)
            
            if(this.currentSpecies != null){
                this.selectSample(this.currentSpecies);
            };

        },
    };
</script>

<style>
.inline_item {
    display: inline-block;
    margin-left: 20px;
    vertical-align: middle;
}
</style>
