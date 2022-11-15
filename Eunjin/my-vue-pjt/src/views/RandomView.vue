<template>
  <div>
    <b-button block variant="outline-info" @click="pickMovie" style="width:500px;">PICK</b-button>
    <!-- <button @click="pickMovie">PICK</button> -->
    <p></p>
    <div id="flex">
      <div class="card w-50 mb-3">
        <img :src="imgUrl" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">{{ movie.title }}</h5>
        </div>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

const API_KEY = process.env.VUE_APP_MOVIE_API_KEY
const API_URL = 'https://api.themoviedb.org/3/movie/top_rated'
const params = {
  api_key: API_KEY,
  language : 'ko',
  page : '1',
}

export default {
  name: 'RandomView',
  data() {
    return {
      movies: [],
      movie : []
    }
  },
  created() {
    axios({
      method: 'get',
      url: API_URL,
      params: params
    })
      .then(response => {
        this.movies = response.data.results
        this.movie = _.sample(this.movies)
        console.log(this.movies)
        console.log(this.movie)
      })
      .catch(error => {
        console.log(error)
      })
  },
  computed: {
    imgUrl() {
      console.log(this.movie)
      return `https://image.tmdb.org/t/p/w500/${this.movie.backdrop_path}`
    }
  },
  methods: {
    pickMovie() {
      this.movie = _.sample(this.movies)
    }
  }
}
</script>

<style>
#flex {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>