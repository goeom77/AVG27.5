<template>
  <div>
    <MovieCardList/>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/axios@1.1.2/dist/axios.min.js"></script>
<script>
import axios from 'axios'
import MovieCardList from '@/components/movies/MovieCardList'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieView',
  components: {
    MovieCardList,
  },
  created() {
    this.getmoviedata()
  },
  methods: {
  getmoviedata() {
    axios.get(`${API_URL}/movies`)
      .then((res) => {
        console.log('axios then 들어옴')
        console.log(res.data)
        this.$store.dispatch('getMovieData', res.data)
      })
      .catch((err) => { 
        console.log(err)
      })
    }
  },

}
</script>

<style>

</style>