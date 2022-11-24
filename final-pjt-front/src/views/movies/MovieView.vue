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
    <div class="mt-5"></div>
    <div>
      <h5>{{ user_mbti }}인 {{user_nickname}}님에게 추천하는 영화</h5>
      <div class="mainitem">
        <MovieCardListItem2
          v-for="movie in movie_mbti_data"
          :key="movie.id"
          :movie="movie"
        />
      </div>
    </div>
    <div class="mt-5"></div>
    <div>
      <h5>{{ user_age }}세 {{user_nickname}}님에게 추천하는 영화</h5>
      <div class="mainitem">
        <MovieCardListItem2
          v-for="movie in movie_age_data"
          :key="movie.id"
          :movie="movie"
        />
      </div>
    </div>
    <div class="m-5"></div>
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
      movie_mbti_data: [],
      movie_age_data: [],
    }
  },
  created() {
    this.movie_latest,
    this.mbti,
    this.age,
    this.movie_age
  },
  computed: {
    user_mbti(){
      return this.$store.state.user.mbti
    },
    user_nickname(){
      return this.$store.state.user.nickname
    },
    user_age(){
      return this.$store.state.user.age
    },
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
    movie_age() {
      this.movie_age_data = _.sampleSize(this.$store.state.movie_age,5)
    },
    mbti() {
      console.log('얍')
      const mbti = this.$store.state.user.mbti
      if (mbti === 'INFJ' || mbti === 'ISTP' || mbti === 'ENFP') {
        this.movie_mbti_data = _.sampleSize(this.$store.state.movie_latest,5)
      } else if (mbti === 'ESFP' || mbti === 'ESFJ') {
        this.movie_mbti_data = _.sampleSize(this.$store.state.movies,5)
      } else {
        console.log(mbti)
        this.$store.dispatch('getMovieMbti', mbti)
        this.movie_mbti_data = _.sampleSize(this.$store.state.movie_mbti,5)
        }
      },
    age() {
      const age = this.$store.state.user.age
      this.$store.dispatch('getMovieage', age)
    }
  }
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

.scroll {
  overflow: auto;
  display: flex;
  white-space: nowrap;
  height:260px;
}

.scroll::-webkit-scrollbar {
  display: none;
}
</style>