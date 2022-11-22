<template>
  <div>
    <div class="d-flex justify-content-between">
      <div>
        <p>id : {{ review.id }}</p>
        <p>content : {{ review.content }}</p>
        <p>user : {{ review.user }}</p>
        <p>movie : {{ review.movie }}</p>
        <p>vote_average : {{ review.vote_average }}</p>
        <p>created_at : {{ review.created_at }}</p>
      </div>

      <div class="d-flex align-items-center">
        <button @click="deleteReview">[Delete]</button>
      </div>
    </div>
    <hr>
  </div>
</template>

<script>
// import axios from 'axios'

// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewListItem',
  props: {
    review: Object
  },
  data() {
    return {
      reviewId: this.review.id,
    }
  },
  methods: {
    deleteReview: function () {
      console.log(this.reviewId)
      this.$emit('deleteReview', this.reviewId)
    },
  // deleteReview: function () {
      //   axios({
      //     method: 'delete',
      //     url: `${API_URL}/movies/review/${this.reviewId}/`,
      //   })
      //   .then(() => {
      //     // console.log(res, 'item에서 삭제중!!')
      //     this.$emit('deleteReview')
      //     })
      //     .catch((err) => {
      //       console.log(err)
      //     })
      // },
  },
}
</script>

<style>
  .likes-count {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .v-application .amber--text.text--lighten-1 {
    color: #ffca28 !important;
    caret-color: #ffca28 !important;
  }
</style>