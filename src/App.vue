<template>
  <div id="app">
    <header>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" active-text-color="#409eff" style="margin: 0px;">
        <el-menu-item index="1">Home</el-menu-item>
        <el-menu-item index="2">Cell Cluster</el-menu-item>
        <el-menu-item index="3">Gene</el-menu-item>
<<<<<<< HEAD
=======
        <el-menu-item index="4">Gene in Umap2D</el-menu-item>
>>>>>>> ae30c83383f4b67f2a23225d8b4e01ab96267fc2
        <el-menu-item index="9" disabled>About Us</a></el-menu-item>
      </el-menu>
      <div class="line"></div>
    </header>
    <article>
        <component v-bind:is="selected"></component>
    </article>
    <hr>
    <footer>
      <div class="line"></div>
      <p>Contact: guolidong@genomics.cn; liyao1@genomics.cn; wangrui</p>
      <p>Single Cell</p>
    </footer>
  </div>
</template>

<script>

import Home from "./Home.vue";
import Cluster from './Cluster.vue'
import Gene from './Gene.vue'
<<<<<<< HEAD

=======
import Umap from './Umap.vue'
>>>>>>> ae30c83383f4b67f2a23225d8b4e01ab96267fc2

export default {
  data() {
    return {
      activeIndex: '1',
      selected:"Home"
    }
  },
  components:{
     Home,
     Cluster,
<<<<<<< HEAD
     Gene
=======
     Gene,
     Umap
>>>>>>> ae30c83383f4b67f2a23225d8b4e01ab96267fc2
  },
  methods: {
    handleSelect(key, keyPath) {
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
<<<<<<< HEAD
=======
        else if ( key == "4")
        {
            this.selected = "Umap";
        }
>>>>>>> ae30c83383f4b67f2a23225d8b4e01ab96267fc2
        else if ( key == "9")
        {
            this.selected = "About Us";
        }
        else
        {
            this.selected = "Home";
        }
    }
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
    }
</style>
