<template>
  <div
    @click="movieDetail(movie.id)"
    style="width: 100px; height: 200px; margin:1rem; background-color: rgba(50, 60, 65, 0.9)"
  >
    <img v-if="movie.poster_path" :src="imgUrl" class="card-img-top" alt="Not Found" onerror="this.src='#';" >
    <!-- <img v-else src="" height="72%" alt=""></img> -->
    <div class="card-body d-flex align-items-start flex-column">
      <p class="card-title fw-bold fs-6 mb-auto">{{ movie.title }}</p>
      <p class="my-0 align-text-bottom" v-if="movie.release_date">{{ movie.release_date | dateParse('YYYY-MM-DD') | dateFormat('YYYY') }}</p>
      <p class="my-0 align-text-bottom">⭐: {{ movie.vote_average }}</p>
    </div>
  </div>
</template>


<script>
export default {
  name: 'MovieCardListItem',
  props: {
    movie : Object,
  },
  computed: {
    imgUrl() {
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
    },
    movieTitle() {
      return this.movie.title
    },
    movieDesc() {
      return this.movie.overview
    },
    vote_average() {
      return this.movie.vote_average
    }
  },
  methods: {
    movieDetail(id) {
      this.$router.push({ name: 'detail', params: {id}})
    }
  }
}
</script>

<style>
</style>