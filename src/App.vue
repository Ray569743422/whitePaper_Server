<template>
  <div id="app">
    <header>
    <img src="./assets/BGI.png" style="width:100%;height:140px">
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" active-text-color="#409eff" style="margin-top: -10px;background-color:#033096;font-size:30px;" text-color="#ffffff">
        <el-menu-item index="1">Home</el-menu-item>
        <el-menu-item index="3">Browse Experiments</el-menu-item>
        <el-menu-item index="4">About Us</el-menu-item>
        <el-menu-item index="5">Test API</el-menu-item>
      </el-menu>
    </header>
    <article>
        <component  v-bind:is="selected"></component>
    </article>
    <hr>
    <footer>
      <div class="line"></div>
      <p>Contact: guolidong@genomics.cn; liyao1@genomics.cn; wangrui21@genomics.cn</p>
      <p>BGI - Aquatic Organism Cell Atlas</p>
    </footer>
  </div>
</template>

<script>
//
import Home from "./Home.vue";
import Tab from './Tab.vue'
import TestAPI from './TestAPI.vue'

export default {
  data() {
    return {
      activeIndex : '1',
      selected:"Home",
    }
  },
  components:{
     Home,
     Tab,
     TestAPI,
  },
  methods: {
    handleSelect(key, keyPath) {
        this.activeIndex = key;
        if ( key == "1")
        {
            this.selected = "Home";
        }
        else if ( key == "2")
        {
            this.selected = "searchGene";
        }
        else if ( key == "3")
        {
            this.selected = "Tab";
        }
        else if ( key == "5")
        {
            this.selected = "TestAPI";
        }
        else
        {
            this.selected = "Home";
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
    width:1503px;
    position: sticky;
    z-index: 999;
    top: 0;
    }
</style>
