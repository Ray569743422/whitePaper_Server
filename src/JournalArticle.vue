<template>
  <div id='app'>
    <title>Past Papers</title>

    <div style="margin-top:120px;">
        <!-- searchable header -->
        <p class="inline_item" > Species:</p>
        <el-select class="inline_item" v-model='currentSpecies' filterable placeholder="">
          <el-option v-for="item in Samples" :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
        <p class="inline_item" > Organ:</p>
        <el-select class="inline_item" v-model='currentOrgan' filterable placeholder="organs" @change='selectOrgan'>
          <el-option v-for="item in Organs" :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
        <!-- searchable header end -->

        <!-- cluster table content -->
        <el-table ref="clusterTable" 
        :show-header='true' class="table" 
        :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
        :highlight-current-row='true'
        stripe
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


    export default {
        props:['G_sample', 'G_gene'],
        data(){
            return {
                // data examples :
                Samples : [ { index:1, value:"Planarian",},
                            { index:2, value:"Zebrafish",},
                            { index:3, value:"Salamander",},
                            { index:4, value:"Shark",},
                            { index:5, value:"Whale",}, ],
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
                currentSpecies:'Planarian',
                aucCutoff: 0,
                currentGene: null,
                currentOrgan: null,
                tableData: [],
                allTableData: [],
                pageSize:15,
                currentPage:1,
            }; // end of data return
        },
        methods: {
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
            });
        },
        mounted(){
             if(this.G_sample != '' )
                 this.currentSpecies = this.G_sample;
             else
                 this.currentSpecies = 'Planarian';
             console.log('--------------');
             console.log(this.G_sample);
             console.log('--------------');
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
