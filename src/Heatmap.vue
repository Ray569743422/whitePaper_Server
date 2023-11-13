<template>
  <div id='app'>
      <div class="common-layout">
          <el-container style="height:320px;">
              <el-aside style="background:#EEF1F6;width:350px">
                      <title>Componement</title>
                      <h5>Gene heatmap</h5>
                      <el-form :model="form" label-width="120px" style="margin-right:50px">
                          <el-form-item label="Species">
                              <el-select v-model="species" placeholder="Select">
                                  <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"/>
                              </el-select>
                          </el-form-item>
                          <el-form-item label="Organ">
                              <el-select v-model="organ" placeholder="Select">
                                  <el-option v-for="item in organTypes" :key="item.value" :label="item.value" :value="item.value"/>
                              </el-select>
                          </el-form-item>
                          <el-form-item label="Gene Name">
                              <el-input v-model="geneNames" :rows="6" type="textarea" placeholder="Please input"/>
                          </el-form-item>
                          <el-form-item style="margin-left:-40px">
                              <el-button type="primary" @click="onSubmit">Submit</el-button>
                          </el-form-item>
                      </el-form>
              </el-aside>
              <el-main style="width:1113px;height:300px;">
                      <v-chart ref="my_gene_echarts" :option="gene_option" style="height:260px"/>
              </el-main>
          </el-container>
      </div>
  </div>
</template>

<script>
    // import echart
    import $ from 'jquery';
    import * as echarts from 'echarts';
    import VChart from "vue-echarts";
    var species=require('./conf/species.js');
    var expression_data_url = 'http://www.bgiocean.com:8020/code/index.php/WhitePaper/heatmap';

    export default{
        name : "heatmap",
        components: {
            VChart
        },
        data() {
            return{
                form: {},
                params: null,
                species: '',
                organ: '',
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

                organTypes: [],
                geneNames: 'PARP12\nsyn3',
                expression: [],
                gene_option: {},
                cellTypes: [],
                genes: [],
                res: {},
            }
        },
        methods: {
            onSubmit(){
                var self = this;
                console.log(self.species);
                console.log(self.geneNames);
                let params = new URLSearchParams({
                    species: self.species,
                    gene: self.geneNames,
                });
                console.log(params);
                self.loading_cell_data(expression_data_url, params);
            },

            // load data
            loading_cell_data(url, params){
                var self = this; 
                self.$axios.post(url, params)
                    .then(res=>{
                        self.res = res.data['ret'];
                        self.create_organ_type(self.res);
                        self.drawHeatmap();
                        console.log(self.organ);
                        });
            },

            create_organ_type(data){
                var self = this;
                let types = [];
                self.organTypes = [];
                for (var i = 0; i < data.length; i++){
                    var innerArray = data[i];
                    if (innerArray.length >= 3) {
                        types.push(innerArray[2]);
                    }
                }

                types = Array.from(new Set(types));

                for (var i = 0; i < types.length; i++){
                    self.organTypes.push({value: types[i]})
                }
            },

            select_organ(data){
                var self = this;
                const expression = [];
                for (var i = 0; i < data.length; i++){
                    var row = data[i];
                    if (row[2]===self.organ){
                        expression.push(row);
                    };
                };
                console.log(expression);
                return expression;
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
                };

                types = Array.from(new Set(types));

                for (var i = 0; i < types.length; i++){
                    self.cellTypes.push(types[i])
                };
            },

            create_gene_type(data){

                var self = this;

                let types = [];

                self.genes=[];

                for (var i = 0; i < data.length; i++){
                    var innerArray = data[i];
                    if (innerArray.length >= 3) {
                        types.push(innerArray[0]);
                    }
                };

                types=Array.from(new Set(types));

                for (var i = 0; i < types.length; i++){
                    self.genes.push(types[i])
                };
            },

            // plot heatmap
            drawHeatmap(){
                var self = this;

                const matrix = [];

                matrix.length = 0;

                const select_organ_data = self.select_organ(self.res);

                self.create_cell_type(select_organ_data);

                self.create_gene_type(select_organ_data);

                for (var i = 0; i < self.cellTypes.length; i++){
                    for (var j = 0; j < self.genes.length; j++){
                        for (var k = 0; k < select_organ_data.length; k++){
                            var row = select_organ_data[k];
                            if (self.cellTypes[i] === row[3] && self.genes[j] === row[0]){
                                matrix.push([i, j, parseFloat(row[1])*100]);
                            };
                        };
                    };
                };

                self.expression = matrix;

                console.log(self.expression);

                var option = {
                    tooltip: {
                        position: 'top'
                    },
                    grid: {
                        left: '15%',
                        height: '55%',
                        width: '85%',
                        top: '10%'
                    },
                    xAxis: {
                        type: 'category',
                        data: self.cellTypes,
                        splitArea: {
                            show: true
                        },
                        axisLabel:{
                            interval:0,
                            rotate: '45'
                        }
                    },
                    yAxis: {
                        type: 'category',
                        data: self.genes,
                        splitArea: {
                            show: true
                        }
                    },
                    visualMap: {
                        calculable: true,
                        orient: 'horizontal',
                        left: 'center',
                        bottom: '0%',
                        inRange: {
                                color: ['#87CEEb','#FFFFFF', '#021C57']
                                }
                    },
                    series: [
                        {
                            name: 'Punch Card',
                            type: 'heatmap',
                            data: self.expression,
                            label: {
                                show: false,
                            },
                            emphasis: {
                                itemStyle: {
                                    shadowBlur: 10,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            }
                        }
                    ]
                };
                self.gene_option = option;
            },
            
            placeholder_option(msg){
                return {
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
        },
        
        mounted(){
            if(this.species === '' ){
                this.species = 'Danio rerio';
            };

            if(this.organ === '' ){
                this.organ = 'Neuron';
            };

            if(this.species && this.geneNames) {
                this.params = new URLSearchParams({
                    species: this.species,
                    gene: this.geneNames,
                });
            };

            this.loading_cell_data(expression_data_url, this.params);

        }
}

</script>

<style>
    .selectComponent {
        background-color:#f5f5f5;
        width:300px;
    }
    .el-form-item{
        width: 100%;
    }
    .el-select{
        position:relative;
    }
    .el-tesxtarea{
        height:600px
    }
</style>
