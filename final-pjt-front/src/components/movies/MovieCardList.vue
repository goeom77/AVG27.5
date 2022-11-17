<template>
  <div  class="row row-cols-md-1 row-cols-lg-3 justify-content-around" style="margin: 5px 200px;">
    <MovieCardListItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import MovieCardListItem from '@/components/movies/MovieCardListItem'

export default {
  name: 'MovieCardList',
  components: {
    MovieCardListItem,
  },
  computed: {
    movies() {
      // console.log(this.$store.state.movies)
      return this.$store.state.movies
    }
  }
}
</script>

<style>

</style>