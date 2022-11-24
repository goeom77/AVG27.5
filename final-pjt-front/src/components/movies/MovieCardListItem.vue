<template>
  <div class="call" ontouchstart="this.classList.toggle('hover');">
    <div class="container" @click="movieDetail(movie.id)">
      <div class="front" style="background-image: url(https://unsplash.it/500/500/)">
        <img :src="imgUrl" alt="" style="width:150px;">
      </div>
      <div class="back">
        <div class="inner">
          <p width='100px' style="word-break:break-all">{{ movieTitle }}</p>
          <span>⭐: {{ vote_average }}</span>
        </div>
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
      this.$router.push({ name: 'MovieDetail', params: {id}})
    }
  }
}
</script>

<style>
  
</style>