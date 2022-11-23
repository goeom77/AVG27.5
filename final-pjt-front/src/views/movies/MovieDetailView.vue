<template>
  <div class="fill-container">
    <YoutubeCard class="youtube" :movie_title="movie_title"/>
    <img class="poster" :src="imgUrl" alt="..." width="250px">
    <div class="allfont fontbox">
      <h1 class="card-title">{{ movie?.title }}</h1>
      <p class="card-text">개봉 날짜 : {{ movie?.release_date }}</p>
      <p class="card-text">평점 : {{ movie?.vote_average }}</p>
      <p class="card-text">줄거리 : {{ movie?.overview }}</p>
      <div>
        <div>
          <button v-if="!pick" @click="choosepick">PICK</button>
          <button v-if="pick" @click="choosepick">UNPICK</button>
        </div>
        <div>
          <button v-if="!wish" @click="choosewish">WISH</button>
          <button v-if="wish" @click="choosewish">UNWISH</button>
        </div>
      </div>
      <ReviewList :movieId="movie.id"></ReviewList>
    </div>
  </div>
</template>

<script>
import axios from "axios"
const API_URL = 'http://127.0.0.1:8000'

import ReviewList from '@/components/movies/ReviewList'
import YoutubeCard from '@/components/movies/YoutubeCard'

export default {
  name: 'MovieDetailView',
  components: {
    ReviewList,
    YoutubeCard,
  },
  data() {
    return {
      movie: null,
      movie_title: null,
      wish: false,
      pick: false,
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
    imgUrl() {
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
    },
    token() {
      return this.$store.state.token
    },
  },
  created() {
    this.getmovielatest()
    this.getMovieById(this.$route.params.id)
    this.getWishStatus(this.$route.params.id)
    this.getPickStatus(this.$route.params.id)
  },
  methods: {
    getMovieById(id) {
      console.log(id)
      for (const movie of this.movies) {
        if (movie.id === Number(id)) {
          this.movie = movie
          this.movie_title = movie.title
          console.log(this.movie)
          break
          }
      }
    },
    getmovielatest() {
      // const movie_length = this.$store.movie_latest
      this.$store.dispatch('getMovieLatest')
    },
    getWishStatus(id) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${id}/wishmovies/`,
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((res) => {
          this.wish = res.data
        })
    },
    getPickStatus(id) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${id}/pickmovies/`,
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((res) => {
          this.pick = res.data
        })
    },
    choosewish() {
      const id = this.$route.params.id
      axios({
        method: 'post',
        url: `${API_URL}/movies/${id}/wishmovies/`,
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((res) => {
          this.wish = res.data
        })
    },
    choosepick() {
      const id = this.$route.params.id
      axios({
        method: 'post',
        url: `${API_URL}/movies/${id}/pickmovies/`,
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((res) => {
          this.pick = res.data
        })
    },
  }
}
</script>

<style>
.poster {
  margin-top: -250px;
  margin-left: 35%;
  z-index: 25;
}
.youtube{
  z-index: 0;
}
.allfont{
  color: white
}
.fontbox {
  margin-top: -150px;
  margin-right: 15%;
  z-index: 50;
}
</style>