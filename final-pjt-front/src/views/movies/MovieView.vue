<template>
  <div style="margin: 5px 200px; width: 18%; height: 100px;">
    <h1>최근 영화 추천</h1>
    <div>
      <MovieCardListItem2
        v-for="movie in movie_latest_data"
        :key="movie.id"
        :movie="movie"
      />
    </div>

    <h1>database 영화</h1>
    <div>
      <MovieCardListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/axios@1.1.2/dist/axios.min.js"></script>
<script>
import _ from 'lodash'
import MovieCardListItem from '@/components/movies/MovieCardListItem'
import MovieCardListItem2 from '@/components/movies/MovieCardListItem2'


export default {
  name: 'MovieView',
  components: {
    MovieCardListItem,
    MovieCardListItem2,
  },
  data() {
    return {
      movie_latest_data: [],
    }
  },
  created() {
    this.movie_latest
  },
  computed:{
    movies() {
      return this.$store.state.movies
    },
    movie_latest() {
      this.movie_latest_data = _.sampleSize(this.$store.state.movie_latest,5)
      console.log(this.movie_latest_data)
    }
  },
}
</script>

<style>

</style>