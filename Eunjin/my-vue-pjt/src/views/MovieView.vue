<template>
  <div class="row row-cols-md-1 row-cols-lg-3 justify-content-around" style="margin: 5px 200px;">
    <MovieCard
      v-for="(movie, index) in movies"
      :key="index"
      :movie="movie"
    />
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import axios from 'axios'

const API_KEY = process.env.VUE_APP_MOVIE_API_KEY
const API_URL = 'https://api.themoviedb.org/3/movie/top_rated'
const params = {
  api_key: API_KEY,
  language : 'ko',
  page : '1',
}
export default {
  name: 'MovieView',
  data() {
    return {
      movies: []
    }
  },
  components: {
    MovieCard
  },
  created() {
    axios({
      method: 'get',
      url: API_URL,
      params: params
    })
      .then(response => {
        console.log(response.data.results)
        this.movies = response.data.results
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style>

</style>