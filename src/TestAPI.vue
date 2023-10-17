<template>
  <div style="width:1503px;">
    <el-row>
        <el-col :span="24">
            <el-input v-model="url" placeholder="URL"></el-input>
        </el-col>
    </el-row>
    <el-row>
        <el-col :span="12">
            <el-input v-model="key1" placeholder="key"></el-input>
        </el-col>
        <el-col :span="12">
            <el-input v-model="value1" placeholder="value"></el-input>
        </el-col>
    </el-row>
    <el-row>
        <el-col :span="12">
            <el-input v-model="key2" placeholder="key"></el-input>
        </el-col>
        <el-col :span="12">
            <el-input v-model="value2" placeholder="value"></el-input>
        </el-col>
    </el-row>
    <el-row>
        <el-col :span="12">
            <el-input v-model="key3" placeholder="key"></el-input>
        </el-col>
        <el-col :span="12">
            <el-input v-model="value3" placeholder="value"></el-input>
        </el-col>
    </el-row>
    <el-row>
        <el-col :span="24">
             <el-button type="primary" @click.native="submit" >Test it</el-button>
        </el-col>
    </el-row>
    <el-row>
        <el-col :span="24">
            <span>Response: {{ msg }}</span>
        </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
    data(){
        return {
            url : 'URL',
            key1 :'key1',
            value1: 'value1',
            key2 :'key2',
            value2: 'value2',
            key3 :'key3',
            value3: 'value3',
            msg: '',
        }
    },
    methods: {
        submit(){
            var self = this;
            var params = new URLSearchParams()
            if(this.key1 != '' && this.key1 != 'key1'){
                params.append(this.key1,this.value1)
            }
            if(this.key2 != '' && this.key2 != 'key2'){
                params.append(this.key2,this.value2)
            }
            if(this.key3 != '' && this.key3 != 'key3'){
                params.append(this.key3,this.value3)
            }
            this.$axios.post(this.url, params)
                .then(res=>{
                        self.msg = res.data
                })   
        },
    }
}
</script>
<style>
</style>
