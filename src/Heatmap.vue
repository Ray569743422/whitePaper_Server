<template>
  <div id='app'>
      <div class="common-layout">
          <el-container style="height:320px;">
              <el-aside style="background:#EEF1F6;width:350px">
                      <title>Componement</title>
                      <h5>Feature heatmap</h5>
                      <el-form :model="form" label-width="120px" style="margin-right:50px">
                          <el-form-item label="Cell Type">
                              <el-select v-model="selected" placeholder="Select">
                                  <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"/>
                              </el-select>
                          </el-form-item>
                          <el-form-item label="Gene Name">
                              <el-input v-model="geneNames" :rows="4" type="textarea" placeholder="Please input"/>
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
    // 导入 echart
    import $ from 'jquery';
    import * as echarts from 'echarts';
    import VChart from "vue-echarts";

    // datasets
    var EXPRESSION_DATA_URL = 'http://49.235.68.146/gene_data/heatmap/'
    export default{
        name : "heatmap",
        components: {
            VChart
        },
        data() {
            return{
                form: {},
                test: null,
                options: [
                    {
                        value: 'Planarian',
                        label: 'Planarian',
                    },
                    {
                        value: 'Zebrafish',
                        label: 'Zebrafish',
                    },
                    {
                        value: 'Salamander',
                        label: 'Salamander',
                    },
                    {
                        value: 'Shark',
                        label: 'Shark',
                    },
                    {
                        value: 'Whale',
                        label: 'Whale',
                    },
                ],
                selected: "",
                // prettier-ignore
                cellTypes: ['Parapharyngeal', 'Cathepsin+cells', 'Epidermal', 'Muscle', 'Intestine', 'Pharynx', 'Neural', 'Neoblast', 'Protonephridia']
                ,
                // prettier-ignore
                geneNames: 'dd_Smed_v4_1_0_1\ndd_Smed_v4_899_0_1\ndd_Smed_v4_90_0_1\ndd_Smed_v4_920_0_1\ndd_Smed_v4_924_0_1\ndd_Smed_v4_940_0_1',
                // prettier-ignore
                name: {},
                expression: {},
                gene_option: {}
            }
        },
        methods: {
            onSubmit() {
                console.log(this.geneNames)
                console.log(this.geneNames=="")
                console.log(this.geneNames.split("\n"))
                if(this.geneNames==""){
                    console.log("不执行")
                }else{
                    console.log("执行")
                    this.generateExpression();
                }
            },
            // 绘制热图
            drowHeatmap(){
                var data = []
                for (var i=0;i<this.name.length;i++){
                    var gene = this.expression[this.name[i]]
                    for (var j=0; j<gene.length; j++){
                        data.push([j, i, gene[j]])
                    }
                }
                console.log(this.name)
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
                        data: this.cellTypes,
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
                        data: this.name,
                        splitArea: {
                            show: true
                        }
                    },
                    visualMap: {
                        min: 0.01,
                        max: 2,
                        calculable: true,
                        orient: 'horizontal',
                        left: 'center',
                        bottom: '0%',
                        inRange: {
                                color: ['#87CEEb','#021C57']
                                }
                    },
                    series: [
                        {
                            name: 'Punch Card',
                            type: 'heatmap',
                            data: data,
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
                this.gene_option = option;
            },
            //
            //创建表达量数组
            generateExpression(){
                var self = this;
                var path = EXPRESSION_DATA_URL;
                this.name=this.geneNames.split("\n")
                for (var i=0; i<this.name.length; i++){
                    var urlExpression = path + this.name[i] + ".json"
                    $.getJSON(urlExpression, function(_data){
                        self.expression[_data.name] = _data.data
                        var ready = true;
                        for (var j=0; j<self.name.length;j++){
                            if (self.expression[self.name[j]] == undefined) {
                                ready = false;
                            }
                        }
                        if (ready) {self.drowHeatmap()}
                    })
                };
            },
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
            }
        },
        created(){
        },
        mounted(){
            console.log(this.geneNames)
            console.log(this.geneNames=="")
            if(this.geneNames==""){
                console.log("不执行1")
            }else{
                console.log("执行1")
                this.generateExpression();
            }
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
