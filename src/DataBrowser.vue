<template>
  <div style="margin-top:120px;">
      <div style="margin-left:0%;background-color: rgb(238, 241, 246); border: 3px solid #eee;" >
          <!-- select gene start -->
          <p class="inline_item" > Switch Atlas:</p>
          <el-select class="inline_item" v-model="G_sample" filterable placeholder="" @change="selectSample" >
            <el-option v-for="item in samples" :key="item.name"
               :label="item.label" :value="item.name">
            </el-option>
          </el-select>
      </div>
      <div>
          <div>
              <p style="background-color:#021C57;color:#ffffff;height:50px;line-height:50px;font-size:40px;margin:10px 0 10px 0">Gene in UMAP Space</p>
              <component :G_sample='selected_sample' :G_gene='G_genes' v-bind:is='useUmap'></component>
          </div>
          <div>
              <p style="background-color:#021C57;color:#ffffff;height:50px;line-height:50px;font-size:40px;margin:0 0 20px 0">Heatmap of Geneset</p>
              <component :G_sample='selected_sample' :G_gene='G_genes' v-bind:is='useHeatmap'></component>
          </div>
      </div>
      <div>
          <p style="background-color:#021C57;color:#ffffff;height:50px;line-height:50px;font-size:40px;margin:20px 0 10px 0">Details of All Markers</p>
          <component :G_sample='selected_sample' :G_gene='G_genes' v-bind:is='useGene'></component>
      </div>
  </div>
</template>

<script>
//
import Gene from './Gene.vue'
import Heatmap from './Heatmap.vue'
import Umap from './Umap.vue'

var species = require('./conf/species.js');

export default {
  props:['G_sample'],
  data() {
    return {
      selected_sample: 'Schmidtea mediterranea',
      G_genes : '',
      G_genesets :[],
      useUmap:'Umap',
      useHeatmap:'Heatmap',
      useGene:'Gene',
      samples : species, 
    }
  },
  components:{
     Gene,
     Umap,
     Heatmap,
  },
  methods: {
    selectSample(sp){
        this.selected_sample = sp ; 
    },
    selectGene(prop) {
    },
  },
  created() {
        this.selected_sample = this.G_sample;
        console.log(this.selected_sample);
        console.log('DDDD');
  },
}
</script>

<style>
#app {
    font-family: Helvetica, sans-serif;
    text-align: center;
    margin-top: -8px;
}
header{
    position: sticky;
    z-index: 999;
    top: 0;
    margin-bottom: 8px;
    background-image:url("assets/sea.jpg");
    height:145px;
    }
</style>
