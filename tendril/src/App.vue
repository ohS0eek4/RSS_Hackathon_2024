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
  <main>
    <hello />
    <hr />
    <search_item @profile_select="profile_select" :skill_tags="all_skill_tags" :hobby_tags="all_hobby_tags" :hit_profiles="test_profile_datas" />
    <hr />
    <profile :skill_tags="all_skill_tags" :hobby_tags="all_hobby_tags" :profile_data="test_profile_datas[show_profile_id]" />
    <hr />
    <relation />
  </main>
</template>

<script>
export default {
  name: "app",
  data() {
    return{
      show_profile_id:1,

      all_skill_tags:["フロントエンド","バックエンド","組み込み","PM"],
      all_hobby_tags:["絵描き","魚釣り"],
      test_profile_datas:[
        {
          username: "とっとこhoge太郎",
          img: "src/assets/plofile_img/monogatari_kyojinno_katani_noru.png",
          affiliation: "ho-ge開発・PM",
          skills: [[0,2],
                  [1,3],
                  [2,2],
                  [3,3]],
          hobbys: [[0,4],
                  [1,3]],
          comment:"肩にちっちゃい人間を載せています。英語は苦手です。",
          desired:2,
        },{
          username: "とっとこhoge次郎",
          img: "src/assets/plofile_img/2.png",
          affiliation: "ho-ge開発・フロント",
          skills: [[1,2],
                  [3,3]],
          hobbys: [[0,4],
                  [1,3]],
          comment:"肩にちっちゃい人間を載せています。英語は苦手です。",
          desired:2,
        },{
          username: "とっとこhoge三郎",
          img: "src/assets/plofile_img/3.png",
          affiliation: "ho-ge開発・バック",
          skills: [[0,2]],
          hobbys: [[0,4]],
          comment:"肩にちっちゃい人間を載せています。英語は苦手です。",
          desired:2,
        }
      ],
      test_rerations:[
        {
          from:0,
          to:1,
          level:3
        },
        {
          from:2,
          to:1,
          level:4
        },
        {
          from:1,
          to:0,
          level:2
        },
        {
          from:1,
          to:2,
          level:5
        },
        {
          from:0,
          to:2,
          level:4
        },
        {
          from:2,
          to:0,
          level:4
        },
        {
          from:0,
          to:1,
          level:4
        },
      ]
    }
  },
  methods: {
    profile_select(msg) {
      this.show_profile_id=msg
    }
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
