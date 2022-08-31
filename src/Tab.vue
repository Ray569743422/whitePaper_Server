<template>
  <div>
    <div>
    </header>
          <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" active-text-color="#409eff" style="margin: 0px;background:rgba(0,0,0,0);position=:relative;top:85px;font-size:30px;" text-color="#000000">
            <el-menu-item index=0 >Summary</el-menu-item>
            <el-menu-item index=1 >Publication</el-menu-item>
            <el-menu-item index=2 >Cell atles</el-menu-item>
            <el-menu-item index=3 >Data browser</el-menu-item>
          </el-menu>
    </div>
      <div>
          <component ref='mainMenu' v-bind:is="selected"></component>
      </div>
  </div>
</template>

<script>
    import Species from './Species.vue'
    import Publication from './Publication.vue'
    import cellAtles from './cellAtles.vue'
    import DataBrowser from './DataBrowser.vue'

export default {
    data(){
        return {
            activeIndex:'0',
            selected:'Species',
        }
    },
    components: {
      Species,
      Publication,
      cellAtles,
      DataBrowser,
    },
    methods: {
        "handleSelect"(key, keyPath){
            this.activeName = key;
<<<<<<< HEAD
            console.log(this.activeName);
            console.log(key);
            if(key=="Species"){
=======
            if(key=='0'){
>>>>>>> f3230fa5275a28396fd220ec544a5085b920c7de
                this.selected = "Species";
            }
            else if(key=='1')
            {
                this.selected = "Publication";
            }
            else if(key=='2'){
                this.selected = "cellAtles"
            }
            else if(key=='3'){
                this.selected = "DataBrowser"
            }
        }
    }
}
</script>
<style>
    .demo-tabs > .el-tabs__content {
        padding: 32px;
        color: #6b778c;
        font-size: 32px;
        font-weight: 600;
    }
    .el-tabs--right .el-tabs__content,
    .el-tabs--left .el-tabs__content {
        height: 100%;
    }
</style>
