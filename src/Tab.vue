<template>
  <div>
    <div>
        <el-tabs style="height: 200px" class="demo-tabs" :default-active="activeName" @tab-click="handleClick">
            <el-tab-pane label="Species" name="Species">Species</el-tab-pane>
            <el-tab-pane label="Publication" name="Publication">Publication</el-tab-pane>
            <el-tab-pane label="cellAtles" name="cellAtles">Cell atles</el-tab-pane>
        </el-tabs>
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

export default {
    data(){
        return {
            activeName:"Species",
            selected:"Species",
        }
    },
    components: {
      Species,
      Publication,
      cellAtles
    },
    methods: {
        handleClick(key, keyPath){
            this.activeName = key;
            console.log(this.activeName);
            console.log(key);
            if(key=="Species"){
                this.selected = "Species";
            }
            else if(key=="Publication")
            {
                this.selected = "Publication";
            }
            else if(key=="cellAtles"){
                this.selected = "cellAtles"
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
