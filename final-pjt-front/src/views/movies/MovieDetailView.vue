<template>
    <div class="fill-container">
      <h1>Detail</h1>
      <div class="card" style="width: 30rem;">
        <img :src="poster_path" alt="...">
        <h5 class="card-title">{{ movie?.title }}</h5>
        <p class="card-text">release_date : {{ movie?.release_date }}</p>
        <p class="card-text">vote_average : {{ movie?.vote_average }}</p>
        <p class="card-text">overview : {{ movie?.overview }}</p>
        <div class="video-container">
          <iframe class="video-iframe" width="100%" height="300" :src="`https://www.youtube-nocookie.com/embed/${this.youtubeurl}`" frameborder="0" allowfullscreen></iframe>
        </div>
        <ReviewList :movieId="movie.id"></ReviewList>
      </div>
    </div>
</template>

<script>
import axios from 'axios'
import ReviewList from '@/components/movies/ReviewList'

export default {
  name: 'MovieDetailView',
  components: {
    ReviewList,
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
    getYoutubeUrl: function () {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movieId}/videos`,
      })
        .then((res) => {
          this.youtubeurl = res.data.results[res.data.results.length-1].key
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    this.getMovieById(this.$route.params.id)
    this.getYoutubeUrl()
  }
}
</script>

<style>

.billboard-row .billboard .billboard-pane, .billboard-row .billboard .fill-container {
    bottom: 0;
    left: 0;
    position: absolute;
    right: 0;
    top: 0;
}
.billboard-row .billboard .hero-image-wrapper .static-image {
    background-position: 50%;
    background-size: cover;
    bottom: 0;
    -ms-filter: progid:DXImageTransform.Microsoft.Alpha(Opacity=100);
    filter: alpha(opacity=100);
    left: 0;
    opacity: 1;
    position: absolute;
    right: 0;
    top: 0;
    transition: opacity .4s cubic-bezier(.665,.235,.265,.8) 0s;
    width: 100%;
}
</style>