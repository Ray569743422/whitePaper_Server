<template>
  <div style="margin-top:120px;">
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
  },
}
</script>

<style>
</style>
