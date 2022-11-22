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
        <button v-if="login_user === write_user" @click="deleteReview" class="btn btn-outline-danger btn-sm mx-3">삭제</button>
        <div class="mx-2 pt-3">
          <span v-if="liked">
            <button @click="like" class="fas fa-heart" style="color: red"></button>
          </span>
          <span v-else>
            <button @click="like" class="far fa-heart" ></button>
          </span>
          <p class="text-center">{{ likeCount }}</p>
        </div>
      </div>
        <!-- <button @click="deleteReview">[Delete]</button> -->
      </div>
    </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewListItem',
  props: {
    review: Object
  },
  data() {
    return {
      reviewId: this.review.id,
      login_user: null,
      movieId: null,
      liked: null,
      likeCount: 0,
    }
  },
  computed: {
    write_user() {
      return this.review.user.pk
    },
  },
  created() {
    this.reviewlike
    this.login_user = this.$store.state.user.pk
    this.movieId = this.review.movie
  },  
  updated() {
    this.reviewlike
  },
  methods: {
    reviewlike(){
      axios({
      method: 'get',
      url: `${API_URL}/movies/${this.movieId}/review/${this.review.id}/like/`,
      headers: {Authorization: `Token ${this.$store.state.token}`}
    })
      .then((res) => {
        this.liked = res.data.liked
        this.likeCount = res.data.count
      })
      .catch((error) => {
        console.log(error)
      })
    },
    deleteReview: function () {
      console.log(this.reviewId)
      this.$emit('deleteReview', this.reviewId)
    },
    like() {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.movieId}/review/${this.reviewId}/like/`,
        headers: {Authorization: `Token ${this.$store.state.token}`}
      })
        .then((res) => {
          this.liked = res.data.liked
          this.likeCount = res.data.count
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  }
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