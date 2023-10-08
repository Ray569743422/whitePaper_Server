<template>
  <div id="app">
    <!-- <pdf ref="pdf" :src="url" style="width: 100%;" /> -->
    <el-form>
        <el-form-item style="margin-left:-40px">
            <el-button type="primary" @click="test">Submit</el-button>
        </el-form-item>
    </el-form>
  </div>
</template>

<script>

export default {
    methods:{
        test(){
            let params = new URLSearchParams({name:'test', id:'1'});
            this.$axios.post('/code/index.php/Test/testAjax', params).then(
                res=>{console.log(typeof res);console.log(res);console.log(res.data)})
            },
        },
    }
</script>

<style>
#app {
  font-family: Helvetica, sans-serif;
  text-align: center;
}
</style>

