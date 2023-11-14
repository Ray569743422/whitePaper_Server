<template>
    <div style="width:100%">

    <!-- searchable header -->
    <el-row>
        <el-col :span="24">
             <el-input v-model="name" placeholder="Enter name to search"></el-input>
             <el-button @click="searchMarkers" type="primary">Search</el-button>
             </el-col>
        </el-col>
    </el-row>
    <!-- searchable header end -->
    <el-row>
        <el-table :data="tableData">
              <el-table-column prop="name" label="Name"></el-table-column>
              <el-table-column prop="age" label="Age"></el-table-column>
              <el-table-column prop="email" label="Email"></el-table-column>
        </el-table>
    </el-row>
    </div>
</template>

<script>
export default {
    data(){
      return {
        name: '',
        table: 'test',
        tableData: []
      }
    },
    methods: {
        searchMarkers(){
          let params = new URLSearchParams({
            table: this.table,
            name: this.name
          });
          this.$axios.post('https://www.bgiocean.com/white_paper/api/searchJohn', params)
            .then(res=>{
                    console.log(res.data);
                    console.log(typeof(res.data));
                    console.log(res.data[0])
                    this.tableData=res.data[0];
                  })
        },
    },  
}
</script>
<style>
</style>
