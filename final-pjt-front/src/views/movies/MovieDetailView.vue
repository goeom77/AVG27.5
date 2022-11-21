<template>
  <div class="fill-container">
    <div>
      <YoutubeCard class="you" :movie_title="movie.title"/>
      <img class="poster" :src="poster_path" alt="..." width="250px">
      <h5 class="card-title">{{ movie?.title }}</h5>
      <p class="card-text">release_date : {{ movie?.release_date }}</p>
      <p class="card-text">vote_average : {{ movie?.vote_average }}</p>
      <p class="card-text">overview : {{ movie?.overview }}</p>
      <ReviewList :movieId="movie.id"></ReviewList>
    </div>
  </div>
</template>

<script>

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
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
    poster_path(){
      return 'https://image.tmdb.org/t/p/original/' + this.movie.poster_path
    }
  },
  methods: {
    getMovieById(id) {
      console.log(id)
      // const id = this.$route.params.id
      for (const movie of this.movies) {
      if (movie.id === Number(id)) {
        this.movie = movie
        break
        }
      }
    },
  created() {
    this.getMovieById(this.$route.params.id)

  }
}
}
</script>

<style>
.poster {
  margin-top: -400px;
  margin-left: 35%;
  z-index: 1;
}
.you{
  z-index: -1;
}
</style>