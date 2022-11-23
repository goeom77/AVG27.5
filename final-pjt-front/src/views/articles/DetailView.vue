<template>
  <div>
    <h1 class="allfont">Detail</h1>
    <h2>제목 : {{ article?.title }}</h2>
    <h2 @click='profileView'>쓴사람이름 : {{ article?.username }}</h2>
    <p>게시판 : {{ article?.type }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <button @click="articleDelete" >[DELETE]</button>
    <router-link :to="{ name: 'EditView',  params : {id : article.id}}">[EDIT]</router-link>
    <div>
      <!-- 댓글내용 -->
      <comment-list :articleId="article.id"></comment-list>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '@/components/articles/CommentList'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components: {
    CommentList
  },
  data() {
    return {
      article: null,
    }
  },
  created() {
    this.getArticleDetail()
    console.log('디테일 도착')
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/${this.$route.params.id}/`
      })
        .then((res) => {
          this.article = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    articleDelete() {
      axios({
        method: 'delete',
        url: `${API_URL}/articles/${this.$route.params.id}/`
      })
      .then(() => {
        this.$store.dispatch('ArticleDelete', this.article.id)
        this.$router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    profileView() {
      console.log(this.article.user.username)
      console.log(this.article)
      this.$router.push({ name: 'ProfileView' , params:{ username : this.article.username }})
    }
  }
}
</script>
<style>
.allfont{
  color: white
}
</style>