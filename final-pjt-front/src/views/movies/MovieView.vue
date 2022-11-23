<template>
  <div>
    <div class="mt-5"></div>
    <div>
      <h5>최근 영화 추천</h5>
      <div class="mainitem">
        <MovieCardListItem2
          v-for="movie in movie_latest_data"
          :key="movie.id"
          :movie="movie"
        />
      </div>
    </div>
    <div class="m-5">

    </div>
    <div>
      <h5>database 영화</h5>
      <div class="mainitem">
        <MovieCardListItem
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
        />
      </div>
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
    username() {
      return this.$store.state.username
    },
    movie_latest() {
      this.movie_latest_data = _.sampleSize(this.$store.state.movie_latest,5)
      console.log(this.movie_latest_data)
    },
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
}
</script>

<style>
#movie-nav {
  justify-content: flex-end;
  align-content: center;
  height: 80px;
}
.mainitem {
  display: flex;
  flex-direction:row nowrap;
  justify-content:flex-start;
  height:200px;
  width:100%
}
</style>