<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>게시판 : {{ article?.type }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <button @click="articleDelete" >[DELETE]</button>
    <router-link :to="{ name: 'EditView', params : {id : article.id}}" :article_edit="article">[EDIT]</router-link>
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
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`
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
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`
      })
      .then(() => {
        this.$store.dispatch('ArticleDelete', this.article.id)
        this.$router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    articleEdit() {

    }
  }
}
</script>
