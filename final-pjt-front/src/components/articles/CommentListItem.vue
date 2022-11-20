<template>
  <div>
    <div class="d-flex justify-content-between">
      <div>
        <!-- <p>id : {{ comment.id }}</p> -->
        <p>content : {{ comment.content }}</p>
        <p>user : {{ comment.user }}</p>
        <p>article : {{ comment.article }}</p>
        <p>created_at : {{ comment.created_at }}</p>
      </div>
      <div class="d-flex align-items-center">
        <button @click="deleteComment">[Delete]</button>
      </div>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentListItem',
  props: {
    comment: Object
  },
  data() {
    return {
      commentId: this.comment.id,
      // articleId: this.comment.article
    }
  },
  methods: {
    deleteComment: function () {
      // const articleId = this.articleId
      axios({
        method: 'delete',
        url: `${API_URL}/articles/comment/${this.commentId}/`,
      })
      .then(() => {
        // console.log(res, 'item에서 삭제중!!')
        this.$emit('deleteComment')
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