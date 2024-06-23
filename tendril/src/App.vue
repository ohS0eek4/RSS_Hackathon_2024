<script setup>
import headlist from './components/header.vue'
import hello from './components/hello.vue'
import search_item from './components/search.vue'
import profile from './components/profile.vue'
import relation from './components/relation.vue'
</script>

<template>
  <header>
    <headlist />
  </header>
  <main v-if="response">
    <hello />
    <hr />
    <search_item @profile_select="response.data.profile_select" :skill_tags="response.data.all_skill_tags" :hobby_tags="response.data.all_hobby_tags" :hit_profiles="response.data.profile_datas" />
    <hr />
    <profile :skill_tags="response.data.all_skill_tags" :hobby_tags="response.data.all_hobby_tags" :profile_data="response.data.profile_datas[show_profile_id]" />
    <hr />
    <relation :relation_data="response.data.reration_data" />
  </main>
</template>

<script>
import axios from 'axios';

export default {
  name: "app",
  data() {
    return{
      show_profile_id:1,
      response:false
    }
  },
  methods: {
    profile_select(msg) {
      this.show_profile_id=msg
    },
    getdatas: async function() {
      this.response = await axios.get('http://localhost:8080/json')
      console.log(this.response.data)
    }
  },
  mounted(){
    this.getdatas()
  }
}
</script>

<style scoped>
main{
  max-width: 1280px;
  margin: 0 auto;
  padding:15px;
}

hr{
  margin:20px 30px;
}
</style>
