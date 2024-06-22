<template>
    <h1>{{ profile_data.username }} のプロフィール</h1>
    <div class="profile-container">
        <div class="profile-image">
            <img :src="this.profile_data.img" alt="キャラクターイラスト">
        </div>
        <div class="profile-details">
            <h2>所属</h2>
            <p>{{ profile_data.affiliation }}</p>
            <h2>能力</h2>
            <table>
                <tr v-for="(skill, index) in profile_data.skills" :key="index">
                    <td>{{ skill_tags[skill[0]] }}</td>
                    <td>{{ create_skill_star(skill[1]) }}</td>
                </tr>
            </table>
            <h2>趣味</h2>
            <table>
                <tr v-for="(hobby, index) in profile_data.hobbys" :key="index">
                    <td>{{ hobby_tags[hobby[0]] }}</td>
                    <td>{{ create_skill_star(hobby[1]) }}</td>
                </tr>
            </table>
            <h2>趣味</h2>
            <h2>コメント</h2>
            <p>{{ profile_data.comment }}</p>
            <h2>希望役職</h2>
            <p>{{ skill_tags[profile_data.desired] }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'profile-item',
    props: ["skill_tags","hobby_tags","profile_data"],
    methods:{
        create_skill_star: function(score){
            var skill_level_star=""
            for(var j=0; j<5; j++){
                if(j < score){
                    skill_level_star+="★";
                }else{
                    skill_level_star+="☆";
                }
            }
            return skill_level_star;
        },
    },
}
</script>

<style scoped>
.profile-container{
    display: flex;
}

img{
    border-radius: 5%;
    width:300px;
    margin-right:100px;
}

h1{
    margin-bottom:20px;
}

@media screen and (max-width: 700px) {    
    .profile-container{
        display:block;
    }
}
</style>