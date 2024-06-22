<template>
    <h1>検索</h1>

    <h2>能力</h2>
    <form v-for="(tag, index) in skill_tags" :key="index">
        <label><input type="checkbox" :value="index" @change="this.selected[0][index]=!this.selected[0][index];" /> {{ tag }}</label>
    </form>
    <h2>趣味</h2>
    <form v-for="(tag, index) in hobby_tags" :key="index">
        <label><input type="checkbox" class="tag_checkbox" @change="this.selected[1][index]=!this.selected[1][index];" /> {{ tag }}</label>
    </form>

    <h2>検索結果</h2>
    <div v-for="(hit_profile, index) in hit_profiles" :key="index">
        <a class="hit_plofile_box" v-if="hit_profile.skills.some(e => this.selected[0][e[0]]) || hit_profile.hobbys.some(e => this.selected[1][e[0]])" @click="this.$emit('profile_select', index);">
            <img :src="hit_profile.img" alt="プロフィール画像">
            <div class="details">
                <h2>{{ hit_profile.username }}</h2>
                <table>
                    <tr v-for="skill_id in hit_profile.skills" :key="skill_id">
                        <div v-if="this.selected[0][skill_id[0]]">
                            <td>{{ skill_tags[skill_id[0]] }}</td>
                            <td>{{ skill_id[1] }} / 5</td>
                        </div>
                    </tr>
                    <tr v-for="hobby_id in hit_profile.hobbys" :key="hobby_id">
                        <div v-if="this.selected[1][hobby_id[0]]">
                            <td>{{ hobby_tags[hobby_id[0]] }}</td>
                            <td>{{ hobby_id[1] }} / 5</td>
                        </div>
                    </tr>
                </table>
            </div>
        </a>
    </div>
</template>

<script>
export default {
    name: 'search-item',
    emits: ['profile_select'],
    props: ["skill_tags","hobby_tags","hit_profiles"],
    data(){
        return{
            selected:[{},{}]
        }
    }
}
</script>

<style scoped>
label{
    user-select: none;
}
h2{
    margin-top: 7px;
}
td{
    margin-right:10px;
}
.hit_plofile_box{
    display: flex;
    padding: 10px 0;
    margin: 0 15px;
    border-top:solid 2px #000;
    border-bottom:solid 2px #000;
}
.hit_plofile_box img{
    width:100px;
    height:100px;
    border-radius: 50%;
    padding:5px;
    margin-right:15px;
}
</style>
