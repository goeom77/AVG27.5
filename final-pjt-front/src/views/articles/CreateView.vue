<template>
  <div class="allfont">
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
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
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
      type: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      const type = this.type
      
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!type) {
        alert('타입을 정해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/articles/`,
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
.allfont{
  color: white
}
</style>
