<template>
  <div id='app'>
    <title>Cluster Table</title>

    <div>
        <!-- searchable header -->
        <p class="inline_item" > select a species:</p>
        <el-select class="inline_item" v-model='currentSpecies' filterable placeholder="">
        </el-select>
        <p class="inline_item" > select a cell:</p>
        <el-select class="inline_item" v-model='currentGene' filterable placeholder="" @change="selectGene">
        </el-select>
        <p class="inline_item" > search:</p>
        <el-input  class="inline_item" style='width:150px;' placeholder="contig id"></el-input>
        <!-- searchable header end -->

        <!-- cluster table content -->
        <el-table ref="clusterTable" 
        :show-header='true' class="table" 
        :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
        :highlight-current-row='true'
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


    export default {
        data(){
            return {
                currentSpecies:null,
                currentGene: null,
                tableData: [],
                pageSize:15,
                currentPage:1,
            }; // end of data return
        },
        methods: {
            handleSizeChange (size) {
                this.pageSize = size;
            },
            handleCurrentChange (currentpage){
                this.currentPage = currentpage;
            },
            selectGene(){},
            handleRow(row,event,column){
                this.currentGene = row.Contig;
                console.log(this.currentGene);
            }
        },
        beforeMount(){
            var self = this;
            $.getJSON(GENE_DATA_URL, function(_data){
                self.tableData = _data;
            });
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
