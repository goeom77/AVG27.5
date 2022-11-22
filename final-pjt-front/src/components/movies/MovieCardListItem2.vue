<template>
  <div class="d-flex flex-row justify-content-start mt-3" style="margin: 10px 0px;">
    <div
      style="width: 300px;"
      @click="movieDetail(movie.id)"
    >
      <img :src="imgUrl" class="card-img-top" width="150px" alt="...">
      <div>
        <p>{{ movieTitle }}</p>
        <p>⭐: {{ vote_average }}</p>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'MovieCardListItem2',
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
      this.$router.push({ name: 'MovieDetail', params: {id}})
    }
  }
}
</script>

<style>

</style>