<template>
    <div>
      <h1>Detail</h1>
      <div class="card" style="width: 30rem;">
        <img :src="poster_path" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">{{ movie?.title }}</h5>
          <p class="card-text">release_date : {{ movie?.release_date }}</p>
          <p class="card-text">vote_average : {{ movie?.vote_average }}</p>
          <p class="card-text">overview : {{ movie?.overview }}</p>
          <!-- <p class="card-text">genres : 
            <span>
                {% for genre in movie.genres.all %}
                    {{ genre.name }}
                {% endfor %}
            </span>
          </p> -->
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'MovieDetailView',
  data() {
    return {
      movie: null,
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
    poster_path(){
      return 'https://image.tmdb.org/t/p/original/' + this.movie.poster_path
    }
  },
  methods: {
    getMovieById(id) {
      console.log(id)
      // const id = this.$route.params.id
      for (const movie of this.movies) {
        if (movie.id === Number(id)) {
          this.movie = movie
          break
        }
      }
    }
  },
  created() {
    this.getMovieById(this.$route.params.id)
  }
}
</script>

<style>

</style>