<template>
  <div>
    <h5 class="fw-bold my-4">댓글</h5>
    <comment-list-item class="container"
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    >
    </comment-list-item>
    <textarea v-model="content" class="form-control" placeholder="댓글을 남겨보세요." rows="5"></textarea>
    <div class="d-flex justify-content-end my-2">
      <button @click="createComment" class="btn btn-success">등록</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentListItem from '@/components/articles/CommentListItem.vue'

export default {
  name: 'CommentList',
  data: function () {
    return {
      comments: [],
      comment: null,
      content: null,
      user: null,
    }
  },
  props: {
    articleId: [String, Number],
  },
  components: {
    CommentListItem,
  },
  methods: {
    createComment: function () {
      const commentItem = {
        content: this.content,
        user: this.user,
        article: this.articleId,
      }
      if (commentItem.content) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/articles/${this.articleId}/comment/`,
          data: commentItem,
          headers: {Authorization: `Token ${this.$store.state.token}`}
        })
          .then((res) => {
            this.content = null
            this.comment = res.data
            this.comments.push(this.comment)
            // console.log(res.data)
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
  },
  created: function(){
    axios({
          method: 'get',
          url: `http://127.0.0.1:8000/articles/${this.articleId}/comment/`,
          headers: {Authorization: `Token ${this.$store.state.token}`}
        })
          .then((res) => {
            console.log(res, '댓글 받아오는 중!!')
            this.comments = res.data 
          })
          .catch((err) => {
            console.log(err)
          })
  },
}
</script>

<style>

</style>