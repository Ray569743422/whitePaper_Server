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
            <el-table-column prop='Contig' label='Contig'></el-table-column>
            <el-table-column prop='Best-blast hit' label='Best-blast hit'></el-table-column>
            <el-table-column prop='Accession' label='Accession'></el-table-column>
            <el-table-column prop='e-value' label='e-value'></el-table-column>
            <el-table-column prop='Organism' label='Organism'></el-table-column>
            <el-table-column prop='log fold enrichment' label='log fold enrichment'></el-table-column>
            <el-table-column prop='cluster enriched in' label='cluster enriched in'></el-table-column>
            <el-table-column prop='Adjusted p-value' label='Adjusted p-value'></el-table-column>
            <el-table-column prop='AUC' label='AUC'></el-table-column>
            <el-table-column prop='Power' label='Power'></el-table-column>
            <el-table-column prop='Associated cell  type class' label='Associated cell type class'></el-table-column>
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

    // datasets
    var GENE_DATA_URL = "http://49.235.68.146/gene_data/All_Clusters.json"

    var species = require('./conf/species.js');

    export default {
        props:['G_sample', 'G_gene'],
        data(){
            return {
                // data examples :
                Ssamples : species,
                samples : [ { index:1, value:"Neoblast",},
                            { index:2, value:"Neural",},
                            { index:3, value:"Cathepsin+ cell",},
                            { index:4, value:"Epidermal",},
                            { index:5, value:"Intestine",},
                            { index:6, value:"Muscle",},
                            { index:7, value:"Phyarnx",},
                            { index:8, value:"Protonephridia",},
                            { index:9, value:"Parapharyngeal",},
                            { index:10, value:"-",}, 
                            { index:11, value:"All",},],
                currentSpecies:'Planarian',
                aucCutoff: 0,
                currentGene: null,
                inputGene: null,
                currentCellType: null,
                tableData: [],
                allTableData: [],
                pageSize:15,
                currentPage:1,
            }; // end of data return
        },
        methods: {
            selectCellType(item){
                //this.currentCellType = item;
                if (this.currentCellType == 'All'){
                    this.tableData = this.allTableData;
                    return
                }
                // change table data
                var new_tableData = [];
                var arrayLength = this.allTableData.length;
                for (var i = 0; i < arrayLength; i++) {
                    if (this.allTableData[i]['Associated cell  type class'] == this.currentCellType){
                        new_tableData.push(this.allTableData[i]);
                    }
                }
                this.tableData = new_tableData;
            },
            selectSample(item){
                if(item == this.currentSpecies)
                    return
                this.currentSpecies = item;
                //this.tableData = getSpeciesData(this.currentSpecies);
                if (this.currentSpecies == 'All'){
                    this.tableData = this.allTableData;
                    return
                }
                // change table data
                var new_tableData = [];
                var arrayLength = this.allTableData.length;
                for (var i = 0; i < arrayLength; i++) {
                    if (this.allTableData[i]['Species'] == item){
                        new_tableData.push(this.allTableData[i]);
                    }
                }
                this.tableData = new_tableData;
            },
            searchGene(){
                // change table data
                var new_tableData = [];
                var arrayLength = this.allTableData.length;
                for (var i = 0; i < arrayLength; i++) {
                    if (this.allTableData[i]['Contig'].includes(this.inputGene)){
                        new_tableData.push(this.allTableData[i]);
                    }
                }
                this.tableData = new_tableData;
            },
            handleSizeChange (size) {
                this.pageSize = size;
            },
            handleCurrentChange (currentpage){
                this.currentPage = currentpage;
            },
            handleRow(row,event,column){
                this.currentGene = row.Contig;
                console.log(this.currentGene);
            }
        },
        beforeMount(){
            var self = this;
            $.getJSON(GENE_DATA_URL, function(_data){
                self.tableData = _data;
                self.allTableData = _data;
                self.selectSample(self.currentSpecies);
            });

        },  
        mounted(){
             if(this.G_sample != '' )
                 this.currentSpecies = this.G_sample;
             else
                 this.currentSpecies = 'All';
             console.log('--------------');
             console.log(this.G_sample);
             console.log(this.G_gene);
             //.................................
             if (this.currentSpecies != null){
                 console.log('xxxx');
                this.selectSample(this.currentSpecies);
             }
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
