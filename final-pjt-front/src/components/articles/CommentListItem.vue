<template>
  <div>
    <div class="d-flex justify-content-between">
      <div>
        <p>{{ comment.content }}</p>
      </div>
      <div class="d-flex align-items-center">
      </div>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommentListItem',
  props: {
    comment: Object
  },
  methods: {
    deleteComment: function () {
      this.articleId = this.$route.params.articleId
      axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/community/${this.articleId}/comment/${this.comment.id}/`,
      headers: {Authorization: `Token ${this.$store.state.token}`}
      })
        .then((res) => {
          console.log(res)
          // console.log(comment.id)
          this.idx = this.comments.indexOf(this.comment)
          this.comments.splice(this.idx, 1)
          // console.log(this.comments)
          // console.log(this.comment)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style>

</style>