<template>
  <div class="col row justify-content-center" style="margin: 10px 0px;">
    <div class="card" style="width: 400px">
      <img :src="imgUrl" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ movieTitle }}</h5>
        <p class="card-text" style="position:relative; height:300px; overflow-y:scroll;">{{ movieDesc }}</p>
      </div>
    </div>
  </div>


</template>

<script> 
export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  computed: {
    imgUrl() {
      return `https://image.tmdb.org/t/p/w500/${this.movie.backdrop_path}`
    },
    movieTitle() {
      return this.movie.title
    },
    movieDesc() {
      return this.movie.overview
    }
  }
}
</script>

<style>

</style>