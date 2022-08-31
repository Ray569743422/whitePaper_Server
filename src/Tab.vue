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
        </el-tabs>
    </div>
      <div>
          <component ref='mainMenu' v-bind:is="selected"></component>
      </div>
  </div>
</template>

<script>
    import Species from './Species.vue'
    import JournalArticle from './JournalArticle.vue'
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
      JournalArticle,
      cellAtles,
      DataBrowser,
    },
    methods: {
        "handleSelect"(key, keyPath){
            this.activeName = key;
            if(key=='0'){
                this.selected = "Species";
            }
            else if(key=='1')
            {
                this.selected = "JournalArticle";
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
