<template>
  <div>
    <h1 class="allfont">게시글 수정</h1>
    <form @submit.prevent="articleEdit">
      <label for="title">제목 : </label>
      <input :value="title" @input="title=$event.target.value" class="form-control" type="text"><br>
      <label for="type">종류 : </label>
        <select id="type" v-model.trim="type">
          <option disabled="disabled">선택해 주세요.</option>
          <option value="공지사항">공지사항</option>
          <option value="자유게시판">자유게시판</option>
          <option value="Q&A">Q&A</option>
        </select>
      <br>
      <label for="content">내용 : </label>
      <textarea :value="content" @input="content=$event.target.value" class="form-control" rows="30"></textarea><br>
      <input type="submit" id="submit">
      <button @click="articleDelete">[DELETE]</button>
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
      title: null,
      content: null,
      type: null,
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/${this.$route.params.id}/`
      })
        .then((res) => {
          console.log(res)
          this.article = res.data
          this.title = this.article.title
          this.content = this.article.content
          this.type = this.article.type
          console.log(this.article)
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
        console.log(this.$store.state.articles)
        this.$store.dispatch('ArticleDelete', this.article.id)
        this.$router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    articleEdit() {
      const articleItem = {
        title: this.title,
        content: this.content,
        type : this.type
      }
      axios({
        method: 'PUT',
        url: `${API_URL}/articles/${this.$route.params.id}/`,
        data: articleItem,
      })
        .then((res) => {
          console.log(res) 
          this.$router.push({ name: 'DetailView', params: this.articleId})
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}
</script>

<style>
.allfont{
  color: white
}
</style>