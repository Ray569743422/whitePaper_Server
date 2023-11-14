<template>
  <div>
      <div style="margin-left:0%;background-color: rgb(238, 241, 246); border: 3px solid #eee;" >
          <!-- select gene start -->
          <p class="inline_item" > Please select one species:</p>
          <el-select class="inline_item" v-model="curr_selected_sample" filterable placeholder="" @change="selectSample" >
            <el-option v-for="item in samples" :key="item.name"
               :label="item.name" :value="item.name">
            </el-option>
          </el-select>
          <!-- select gene start -->
          <p class="inline_item" > Please type the gene name:</p>
          <el-input  class="inline_item" style='width:250px;' v-model="input_gene" placeholder=""></el-input>
         <el-button class='inline_item' @click.native="submit_gene">Submit</el-button>
          <!-- select gene start -->
          <p class="inline_item" > Or try examples:</p>
          <el-select class="inline_item" v-model="selected_example" filterable placeholder="" @change="selectGene" >
            <el-option v-for="item in genes" :key="item.value"
               :label="item.value" :value="item.value">
            </el-option>
          </el-select>
      </div>
        <el-row>
            <el-col :span="12">
            <div style="margin-left:30px;">
              <p>The celltype in Umap2D space</p>
              <v-chart ref="my_cell_echarts"  :option="cell_option" style="width:650px;height:650px;" />
            </div>
           </el-col>
            <el-col :span="12">
            <div style="margin-left:50px">
              <p>The gene in Umap2D space</p>
              <v-chart ref="my_gene_echarts"  :option="gene_option" style="width:650px;height:650px;" />
            </div>
            </el-col>
        </el-row>
  </div>
</template>

<script>
  import $ from 'jquery';
  import * as echarts from 'echarts';
  import VChart from "vue-echarts";
  var CT_URL='http://www.bgiocean.com:8020/code/index.php/WhitePaper/celltypeUmap'
  var GENE_URL='http://www.bgiocean.com:8020/code/index.php/WhitePaper/expressionUmap'
  var species = require('./conf/species.js');
  export default {
    name : "Umap2D",
    components: {
        VChart
    },
    props:['G_sample','G_gene'],
    data(){
      return {
        // data buffering
        input_gene : null,
        selected_example : null,
        curr_cell_data : null,
        curr_gene_data : null,
        // selection tags :
        //curr_selected_sample : 'Schmidtea mediterranea',
        curr_selected_sample : null,
        curr_selected_gene : null,
        curr_db_key : null,
        // data examples :
        samples : species,

        genes : [   { index:1, value:"dd-Smed-v4-1000-0-1",},
                    { index:2, value:"dd-Smed-v4-100-0-1",},
                    { index:3, value:"dd-Smed-v4-10001-0-1",},
                    { index:4, value:"dd-Smed-v4-10002-0-1",},
                    { index:5, value:"dd-Smed-v4-100026-0-1",},
                    { index:6, value:"dd-Smed-v4-10003-0-1",},
                ],
        // echarts options
        gene_option : {backgroundColor:'#FFFFFF',},
        cell_option : {backgroundColor:'#FFFFFF',},
       };
     },
     methods: {
       /*********************functions for datas start**********************/
       clean_gene_buffer(){
         this.curr_selected_gene == null;
         this.curr_gene_data = null;
         this.$refs.my_gene_echarts.setOption(this.get_gene_option(),true);
       },
       clean_cell_buffer(){
         this.curr_selected_gene == null;
         this.curr_cell_data = null;
         this.$refs.my_cell_echarts.setOption(this.get_cell_option(),true);
       },
       clean_buffer(){
         this.clean_gene_buffer();
         this.clean_cell_buffer();
       },
       loading_gene_data(){
          var self = this;
          let params = new URLSearchParams({
               species:this.curr_db_key,
               gene : this.curr_selected_gene,
          });
          this.$axios.post(GENE_URL, params)
              .then(res=>{
                      self.curr_gene_data = res.data['ret'];
                      self.gene_option = self.get_gene_option();
          })
       },
       loading_cell_data(){
          var self = this;
          let params = new URLSearchParams({
               species:this.curr_db_key,
          });
          this.$axios.post(CT_URL, params)
              .then(res=>{
                      self.set_cell_data(res.data['ret']);
                      self.cell_option = self.get_cell_option();
                      self.gene_option = self.get_gene_option();
          })
       },
       set_cell_data(data){
           this.curr_cell_data = {}
           for(var i=0 ; i< data.length; i++){
                var item = data[i];
                var key = item[2];
                if ( key in this.curr_cell_data ){
                    this.curr_cell_data[key].push([item[0],item[1]])
                } else {
                    this.curr_cell_data[key] = [];
                    this.curr_cell_data[key].push([item[0],item[1]])
                }
           }
       },
       /*********************functions for datas end**********************/

       /*********************functions for user selection start**********************/
       submit_gene(){
          this.selected_example = null;
          this.selectGene(this.input_gene);
       },
       selectGene(item){
         console.log(item);
         this.clean_gene_buffer()
         this.curr_selected_gene = item;
         this.loading_gene_data()
       },
       updateCurrSample(item){
         this.curr_selected_sample = item;
         for(var i=0 ; i< this.samples.length; i++){
            var tt =  this.samples[i];
            if (tt.name == item ){
                this.curr_db_key = tt.DBKey;
                this.genes = tt.exampleGene;
            }
         }
       },
       selectSample(item){
         this.clean_buffer();
         this.updateCurrSample(item);
         this.loading_cell_data();
       },
       /*********************functions for user selection end  **********************/

       /*********************functions for echarts option start**********************/
       placeholder_option(msg){
         return  {
           backgroundColor:'#FFFFFF',
           title : {
               text : msg,
               left: "center",
               top: "center",
               textStyle: {
                  color: '#000000'
               },
           }
         };
       },
       get_cell_option(){
          if( this.curr_cell_data == null ) {
              return this.placeholder_option('Loading data ... ');
          }
          var series_list = [];
          for (const [celltype, coords] of Object.entries(this.curr_cell_data)) {
              var one_ct = {
                 name: celltype,
                 type: 'scatter',
                 data: coords,
                 dimensions: ['x', 'y'],
                 symbolSize: 3,
                 itemStyle: {
                   opacity: 0.6
                 },
                 large: true
              };
              series_list.push(one_ct)
          };
          var option = {
              backgroundColor:'#FFFFFF',
              title : {
                   text : '',
                   left: "center",
                   top: "center",
                   textStyle: {
                      color: '#000000'
                   },
              },
              legend: {
                  // orient: 'vertical',
              },
              xAxis: [{}],
              yAxis: [{}],
              toolbox: {
                show: true,
                feature: {
                    saveAsImage: {},
                }
              },
              tooltip: {},
              series: series_list
          };
          return option;
       },
       get_gene_option(){
         if( this.curr_cell_data == null ) {
             return this.placeholder_option('Waiting species data...');
         }
         var series_list = [];
         var sid = 0;
         for (const [celltype, coords] of Object.entries(this.curr_cell_data)) {
             var one_ct = {
                type: 'scatter',
                data: coords,
                dimensions: ['x', 'y'],
                symbolSize: 2,
                color:'#0f0f0f',
                itemStyle: {
                  opacity: 0.1
                },
                large: true
             };
             series_list.push(one_ct);
             sid = sid + 1;
         };
         var msg = '';
         if (this.curr_selected_gene == null)
             msg = 'Please select a specfic gene to display ...';
         else if (this.curr_gene_data == null ) 
             msg = 'Loading data ...';
         else {
             var data = [];
             var one_gene = {
                name : this.curr_selected_gene,
                type: 'scatter',
                symbolSize: 5,
                data: this.curr_gene_data,
                itemStyle: {
                  opacity: 0.8
                },
             };
             series_list.push(one_gene)
         }
         var option = {
              backgroundColor:'#FFFFFF',
              title : {
                   text : msg,
                   left: "center",
                   top: "center",
                   textStyle: {
                      color: '#000000'
                   },
              },
              xAxis: [
                 {
                    type: 'value'
                 }
              ],
              yAxis: [
                 {
                  type: 'value'
                 }
              ],
              toolbox: {
                show: true,
                feature: {
                    saveAsImage: {},
                }
              },
              tooltip: {},
              series: series_list
         };
         if( this.curr_cell_data != null &&  this.curr_gene_data != null )
         {
            option.visualMap= {
                  min: 0,
                  max: 5,
                  dimension: 2,
                  orient: 'vertical',
                  seriesIndex: sid  ,
                  right: 5,
                  top: 'center',
                  calculable: true,
                  inRange: {
                    color: ['blue', 'white','red']
                  }
                };
         }
         return option;
       },
       /*********************functions for echarts option end**********************/
     },
     mounted(){
         console.log('--------------');
         console.log(this.G_sample);
         console.log('--------------');
         if(this.G_sample != '' )
             this.updateCurrSample(this.G_sample);
         else
             this.updateCurrSample('Schmidtea mediterranea');
         this.gene_option = this.get_gene_option();
         this.cell_option  = this.get_cell_option();
         if( this.curr_selected_sample != null )
             this.loading_cell_data()
         if(this.G_gene != '' )
             this.selectGene(this.G_gene);
     },
  };
</script>

<style>
.inline_item_tight {
  display: inline-block;
  margin-left: 3px;
  vertical-align: middle;
}
.inline_item {
  display: inline-block;
  margin-left: 20px;
  vertical-align: middle;
}
</style>
