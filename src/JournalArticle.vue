<template>
  <div id='app'>
    <title>Past Papers</title>

    <div>
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
        @row-click='handleRow'>
            <el-table-column prop='物种' label='物种'></el-table-column>
            <el-table-column prop='器官' label='器官'></el-table-column>
            <el-table-column prop='发育时期' label='发育时期'></el-table-column>
            <el-table-column prop='细胞数' label='细胞数'></el-table-column>
            <el-table-column prop='参考文献' label='参考文献'></el-table-column>
            <el-table-column prop='可视化网站' label='可视化网站'></el-table-column>
            <el-table-column prop='备注' label='备注'></el-table-column>
            <el-table-column prop='RDS路径' label='RDS路径'></el-table-column>
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
    var GENE_DATA_URL = "http://49.235.68.146/gene_data/download.json"


    export default {
        data(){
            return {
                // data examples :
                Samples : [ { index:1, value:"Planarian",},
                            { index:2, value:"Zebrafish",},
                            { index:3, value:"Salamander",},
                            { index:4, value:"Shark",},
                            { index:5, value:"Whale",}, ],
                Organs : [{index:1, value:"All"},
                         {index:2, value:"全部"},
                         {index:3, value:"脑"},],
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
                    if (this.allTableData[i]['器官'] == this.currentOrgan){
                        new_tableData.push(this.allTableData[i]);
                    }
                }
                this.tableData = new_tableData;
            },
            selectSample(item){
                console.log(item);
                if(item == this.currentSpecies)
                    return
                this.currentSpecies = item;
                //this.tableData = getSpeciesData(this.currentSpecies);
            },
            searchGene(item){
                console.log(currentGene);
                console.log(item);            
            },
            handleSizeChange (size) {
                this.pageSize = size;
            },
            handleCurrentChange (currentpage){
                this.currentPage = currentpage;
            },
            handleRow(row,event,column){
                this.currentGene = row.物种;
                console.log(this.currentGene);
            }
        },
        beforeMount(){
            var self = this;
            $.getJSON(GENE_DATA_URL, function(_data){
                self.tableData = _data;
                self.allTableData = _data;
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
