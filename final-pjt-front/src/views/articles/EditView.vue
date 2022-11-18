<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="articleEdit">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>

      <label for="type">종류 : </label>
        <select id="type" v-model.trim="type">
          <option disabled="disabled">선택해 주세요.</option>
          <option value="공지사항">공지사항</option>
          <option value="자유게시판">자유게시판</option>
          <option value="Q&A">Q&A</option>
        </select>
      <br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "EditView",
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
          console.log('수정할 내용 챙김')
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
        console.log(this.$store.state.articles)
        this.$store.dispatch('ArticleDelete', this.article.id)
        this.$router.push({ name: 'DetailView', params: this.article.id})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    articleEdit() {
      axios({
        method: 'PUT',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`
      })
        .then((res) => {
          this.article = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    createArticle() {
      const title = this.title
      const content = this.content
      const type = this.type
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: {
          title: title,
          content: content,
          type: type,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.$router.push({ name: 'ArticleView' })
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>