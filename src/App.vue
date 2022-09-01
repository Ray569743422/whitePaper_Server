<template>
  <div id="app">
    <header>
    <img src="./assets/BGI.png" style="width:1503px;height:140px">
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" active-text-color="#409eff" style="margin-top: -10px;background-color:#021C57;font-size:30px;" text-color="#ffffff">
        <el-menu-item index="1">Home</el-menu-item>
        <el-menu-item index="2">Search Gene</el-menu-item>
        <el-menu-item index="3">Browse Experiments</el-menu-item>
        <el-menu-item index="4">About Us</el-menu-item>
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
import ComingSoon from './CommingSoon.vue'

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
     ComingSoon,
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
            this.selected = "ComingSoon";
        }
        else if ( key == "3")
        {
            this.selected = "Tab";
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
    position: sticky;
    z-index: 999;
    top: 0;
    }
</style>
