<template>
  <div style="margin: 5px 200px; width: 18%; height: 100px;">
    <div>
      <h1>최근 영화 추천</h1>
      <MovieCardListItem2
        v-for="movie in movie_latest"
        :key="movie.id"
        :movie="movie"
      />
    </div>

    <div>
      <h1>database 영화</h1>
      <MovieCardListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
    <div>
      <h1>USerInfo 유저정보</h1>
      <UserInfo/>
    </div>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/axios@1.1.2/dist/axios.min.js"></script>
<script>
import MovieCardListItem from '@/components/movies/MovieCardListItem'
import MovieCardListItem2 from '@/components/movies/MovieCardListItem2'
import UserInfo from '@/components/profiles/UserInfo'

export default {
  name: 'MovieView',
  components: {
    MovieCardListItem,
    MovieCardListItem2,
    UserInfo,
  },
  computed:{
    movies() {
      return this.$store.state.movies
    },
    movie_latest() {
      return this.$store.state.movie_latest
    }
  },
}
</script>

<style>

</style>