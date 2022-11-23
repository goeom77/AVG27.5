<template>
  <div class="fill-container">
    <div class="youtube">
      <YoutubeCard :movie_title="movie_title"/>
    </div>
    <img class="poster" :src="imgUrl" alt="..." width="250px">
    <div class="allfont fontbox">
      <h1 class="card-title">{{ movie?.title }}</h1>
      <p class="card-text">개봉 날짜 : {{ movie?.release_date }}</p>
      <p class="card-text">평점 : {{ movie?.vote_average }}</p>
      <p class="card-text">줄거리 : {{ movie?.overview }}</p>
    </div>
  </div>
</template>

<script>
import YoutubeCard from '@/components/movies/YoutubeCard'

export default {
  name: 'MovieDetailViewLatest',
  components: {
    YoutubeCard,
  },
  data() {
    return {
      movie: null,
      movie_title: null,
    }
  },
  computed: {
    movies() {
      return this.$store.state.movie_latest
    },
    imgUrl() {
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
    },
    token() {
      return this.$store.state.token
    }
  },
  created() {

    this.getMovieById(this.$route.params.id)
  },
  methods: {
    getMovieById(id) {
      console.log(id)
      for (const movie of this.movies) {
        console.log(1)
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
    }
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
  overflow: hidden;
  position: relative;
  height: 80%
}
.allfont{
  color: white;
}
.fontbox {
  margin-top: -150px;
  margin-right: 15%;
  z-index: 50;
}
</style>