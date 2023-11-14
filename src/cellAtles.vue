<template>
  <div style="margin-top:120px;">
  <h1>CellAtlas</h1>
    <div>
        <el-row>
            <el-col :span="6">
                <div style="border:1px solid;;border-radius:25px;border-color: #ccc;width:250px;height:300px;margin-left:60px">
                    <img src="./assets/cellAtlas/01.png" style="width:200px;height:200px;">
                    <p style="margin-left:-15px">Schmidtea mediterranea</p>
                    <el-button type="primary" style="margin-left:-15px" v-on:click="jumpUmapsc">Details</el-button>
                </div>
            </el-col>
            <el-col :span="6">
                <div style="border:1px solid;;border-radius:25px;border-color: #ccc;width:250px;height:300px;margin-left:60px">
                    <img src="./assets/cellAtlas/02.png" style="width:200px;height:200px;">
                    <p style="margin-left:-15px">Denio rerio</p>
                    <el-button type="primary" style="margin-left:-15px" v-on:click="jumpUmapda">Details</el-button>
                </div>
            </el-col>
            <el-col :span="6">
                <div style="border:1px solid;;border-radius:25px;border-color: #ccc;width:250px;height:300px;margin-left:60px">
                    <img src="./assets/cellAtlas/03.png" style="width:200px;height:200px;"><p style="margin-left:-15px">Nematostella vectensis</p>
                    <el-button type="primary" style="margin-left:-15px">Details</el-button>
                </div>
            </el-col>
            <el-col :span="6">
                <div style="border:1px solid;;border-radius:25px;border-color: #ccc;width:250px;height:300px;margin-left:60px">
                    <img src="./assets/cellAtlas/04.png" style="width:200px;height:200px;">
                    <p style="margin-left:-15px">Ciona intestinalis</p>
                    <el-button type="primary" style="margin-left:-15px">Details</el-button>
                </div>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="6">
                <div style="border:1px solid;;border-radius:25px;border-color: #ccc;width:250px;height:300px;margin-left:60px">
                    <img src="./assets/cellAtlas/05.png" style="width:200px;height:200px;">
                    <p style="margin-left:-15px">Clytia medusa</p><el-button type="primary" style="margin-left:-15px">Details</el-button>
                </div>
            </el-col>
            <el-col :span="6">
                <div style="border:1px solid;;border-radius:25px;border-color: #ccc;width:250px;height:300px;margin-left:60px">
                    <img src="./assets/cellAtlas/06.png" style="width:200px;height:200px;"><p style="margin-left:-15px">Octopus vulgaris</p>
                    <el-button type="primary" style="margin-left:-15px">Details</el-button>
                </div>
            </el-col>
            <el-col :span="6">
                <div style="border:1px solid;;border-radius:25px;border-color: #ccc;width:250px;height:300px;margin-left:60px">
                    <img src="./assets/cellAtlas/07.png" style="width:200px;height:200px;">
                    <p style="margin-left:-15px">Trachemys scripta elegans</p>
                    <el-button type="primary" style="margin-left:-15px">Details</el-button>
                </div>
            </el-col>
            <el-col :span="6">
                <div style="border:1px solid;;border-radius:25px;border-color: #ccc;width:250px;height:300px;margin-left:60px">
                    <img src="./assets/cellAtlas/08.png" style="width:200px;height:200px;">
                    <p style="margin-left:-15px">Strongylocentrotus purpuratus</p>
                    <el-button type="primary" style="margin-left:-15px">Details</el-button>
                </div>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="6">
                <div style="border:1px solid;;border-radius:25px;border-color: #ccc;width:250px;height:300px;margin-left:60px">
                    <img src="./assets/cellAtlas/09.png" style="width:200px;height:200px;">
                    <p style="margin-left:-15px">Branchiostoma floridae</p>
                    <el-button type="primary" style="margin-left:-15px">Details</el-button>
                </div>
            </el-col>
            <el-col :span="6">
                <div style="border:1px solid;;border-radius:25px;border-color: #ccc;width:250px;height:300px;margin-left:60px">
                    <img src="./assets/cellAtlas/10.png" style="width:200px;height:200px;">
                    <p style="margin-left:-15px">Xenia sp.</p>
                    <el-button type="primary" style="margin-left:-15px">Details</el-button>
                </div>
            </el-col>
        </el-row>
    </div>
  </div>
</template>

<script>
export default {
    data(){
        return {}
    },
    methods: {
        jumpUmapsc(){
            this.$emit('updataGlobal', {species: "Schmidtea mediterranea",gene:''});
        },
        jumpUmapda(){
            this.$emit('updataGlobal', {species: "Danio rerio", gene:''});
        }
    }
}
</script>
<style>
.el-row {
    margin-bottom: 20px;
    }
.el-row:last-child {
    margin-bottom: 0;
    }
.el-col {
    border-radius: 4px;
    }
</style>
