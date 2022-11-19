<template>
  <div class="col row justify-content-center" style="margin: 10px 0px;">
    <div
      @click="movieDetail(movie.id)"
      class="card" style="width: 400px"
    >
      <img :src="imgUrl" class="card-img-top" alt="...">
      <div class="card-body">
        <h3 class="card-title">{{ movieTitle }}</h3>
        <h5 class="card-text">⭐: {{ vote_average }}</h5>
      </div>
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