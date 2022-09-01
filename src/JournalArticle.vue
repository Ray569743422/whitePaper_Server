<template>
  <div id='app'>
    <title>Past Papers</title>

    <div style="margin-top:120px;">
        <!-- searchable header -->
        <p class="inline_item" > Species:</p>
        <el-select class="inline_item" @change='selectSpecies' v-model='currentSpecies' placeholder='species' filterable>
          <el-option v-for="item in Samples" :key="item.name" :label="item.label" :value="item.name">
          </el-option>
        </el-select>
        <p class="inline_item" > Organ:</p>
        <el-select class="inline_item" v-model='currentOrgan' filterable placeholder="organs" @change='selectOrgan'>
          <el-option v-for="item in Organs" :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
        
        <p class="inline_item" > Search a paper:</p>
        <el-input  v-model='inputPaper' @input='searchPaper' class="inline_item" style='width:150px;' placeholder="" ></el-input>
        <!-- searchable header end -->

        <!-- cluster table content -->
        <el-table ref="clusterTable" 
        :show-header='true' class="table" 
        :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
        :highlight-current-row='true'
        stripe
        :header-cell-style="{color:'#EEF1F6',fontSize:'16px',background:'#021C57'}"
        @row-click='handleRow'
        @row-dblclick='updateOrganAndJump'>
            <el-table-column prop='Load date' label='Load Date'></el-table-column>
            <el-table-column prop='Phylum ' label='Phylum'></el-table-column>
            <el-table-column prop='Species' label='Species'></el-table-column>
            <el-table-column prop='Article' label='Article'></el-table-column>
            <el-table-column prop='Organ' label='Organ'></el-table-column>
            <el-table-column prop='number of cells' label='Number of Cells'></el-table-column>
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
    var GENE_DATA_URL = "http://49.235.68.146/gene_data/pulication.json"

    //
    var species = require('./conf/species.js');
    var papers = require('./conf/papers.js');

    export default {
        props:['G_sample', 'G_gene'],
        data(){
            return {
                // data examples :
                Samples : species,
                Organs : [{index:1, value:"All"},
                         {index:2, value:"Whole organism"},
                         {index:3, value:"Brain"},
                         {index:4, value:"Tentacle and polyp"},
                        {index:5, value:"Neuron"},
                        {index:6, value:"Hindbrain"},
                        {index:7, value:"Hypothalamus"},
                        {index:8, value:"Intestine"},
                        {index:9, value:"Tail"},
                        {index:10, value:"Ovary"},
                ],
                paperResults: papers,
                currentSpecies:null,
                aucCutoff: 0,
                inputPaper: null,
                currentOrgan: null,
                tableData: [],
                allTableData: [],
                pageSize:15,
                currentPage:1,
            }; // end of data return
        },
        methods: {
            searchPaper(){
                console.log(this.inputPaper);
                // change table data
                var new_tableData = [];
                var arrayLength = this.allTableData.length;
                for (var i = 0; i < arrayLength; i++) {
                    if (this.allTableData[i]['Article'].includes(this.inputPaper)){
                        new_tableData.push(this.allTableData[i]);
                    }
                }
                this.tableData = new_tableData;
            },
            selectSpecies(item){
                console.log('xxx: selectSpecies');
                console.log(item);
                this.currentSpecies == item;
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
            selectOrgan(item){
                //this.currentCellType = item;
                if (this.currentOrgan == 'All'){
                    this.tableData = this.allTableData;
                    return
                }
                // change table data
                var new_tableData = [];
                var arrayLength = this.allTableData.length;
                for (var i = 0; i < arrayLength; i++) {
                    if (this.allTableData[i]['Organ'] == this.currentOrgan){
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
                this.currentSpecies = row.Species;
                console.log(this.currentSpecies);
                console.log(event);
            },
            updateOrganAndJump(row){
                this.currentSpecies = row.Species;
                this.$emit('updataGlobal',row.Species);
            }
        },
        beforeMount(){
            var self = this;
            $.getJSON(GENE_DATA_URL, function(_data){
                self.tableData = _data;
                self.allTableData = _data;
                console.log('before');
                console.log('self');
                console.log(self.currentSpecies);
                self.selectSpecies(self.currentSpecies);
            });
        },
        mounted(){
             if(this.G_sample != '' )
                 this.currentSpecies = this.G_sample;
             else
                 this.currentSpecies = 'All';
             console.log('--------------');
             console.log(this.G_sample);
             console.log('--------------');
                console.log(this.currentSpecies);
             console.log(this.paperResults);
                //.................................
             if (this.currentSpecies != null){
                 console.log('xxxx');
                this.selectSpecies(this.currentSpecies);
             }
         },
        computed:{
            searchPaperVague(){
                //if (!this.inputPaper){
                //    return this.paperResults
                //}
                return this.paperResults.filter(item => {
                    return item.name.includes(this.inputPaper)
                })
                return data
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
