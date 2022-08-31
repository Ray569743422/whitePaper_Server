<template>
  <div id="app">
    <header>
    <img src="./assets/BGI.png" style="width:1503px;height:140px">
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" active-text-color="#409eff" style="margin-top: -10px;background-color:#021C57;font-size:30px;" text-color="#ffffff">
        <el-menu-item index="1">Home</el-menu-item>
        <el-menu-item index="2">Cell Cluster</el-menu-item>
        <el-menu-item index="3">Gene</el-menu-item>
        <el-menu-item index="4">Gene in Umap2D</el-menu-item>
        <el-menu-item index="5">Gene Heatmap</el-menu-item>
        <el-menu-item index="6">Tab</el-menu-item>
        <el-menu-item index="9" disabled>About Us</el-menu-item>
      </el-menu>
    </header>
    <article>
        <component ref='mainMenu' :G_sample='G_samplename' :G_gene='G_genes'  @updataGlobal="updateGValues($event)" v-bind:is="selected"></component>
    </article>
    <hr>
    <footer>
      <div class="line"></div>
      <p>Contact: guolidong@genomics.cn; liyao1@genomics.cn; wangrui21@genomics.cn</p>
      <p>Single Cell</p>
    </footer>
  </div>
</template>

<script>
//
import Home from "./Home.vue";
import Cluster from './Cluster.vue'
import Gene from './Gene.vue'
import Heatmap from './Heatmap.vue'
import Umap from './Umap.vue'
import Tab from './Tab.vue'

export default {
  data() {
    return {
      activeIndex : '1',
      selected:"Home",
      G_samplename : '',
      G_genes : '',
    }
  },
  components:{
     Home,
     Cluster,
     Gene,
     Umap,
     Heatmap,
     Tab
  },
  methods: {
    handleSelect(key, keyPath) {
        console.log(key)
        console.log(keyPath)
        this.activeIndex = key;
        console.log(this.activeIndex)
        if ( key == "2" )
        {
            this.selected = "Cluster";
        }
        else if ( key == "1")
        {
            this.selected = "Home";
        }
        else if ( key == "3")
        {
            this.selected = "Gene";
        }
        else if ( key == "4")
        {
            this.selected = "Umap";
        }
        else if ( key == "5")
        {
            this.selected = "Heatmap";
        }
        else if ( key == "6")
        {
            this.selected = "Tab";
        }
        else if ( key == "9")
        {
            this.selected = "About Us";
        }
        else
        {
            this.selected = "Home";
        }
    },
    updateGValues(prop) {
       for (var key in prop) {
          if( key == 'sample' )
             this.G_samplename = prop[key];
          else if ( key == 'gene' )
              this.G_genes = prop[key];
       }
       // handle jump now 
       for (var key in prop) {
          if( key == 'jump' ) {
              var jump_index = prop['jump'];
              this.$nextTick(() => {
                  this.handleSelect(jump_index,[jump_index]);
              });
          }
       }
    },
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
    }
</style>
