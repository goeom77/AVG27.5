<template>
  <div>
    <h1>보고싶은 영화</h1>
    <WatchListForm
      @movie-add="movieAdd"
    />
    <WatchListItem
      v-for="(movie, index) in addedMovies"
      :key="index"
      :movie=movie
      @delete_movie="DeleteMovie"
    />
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm'
import WatchListItem from '@/components/WatchListItem'

export default {
  name: 'WatchListView',
  data() {
    return {
      addedMovies: [],
    }
  },
  components: {
    WatchListForm,
    WatchListItem
  },
  methods: {
    movieAdd(movieItem) {
      this.addedMovies.push(movieItem)
      // console.log(this.addedMovies)
    },
    DeleteMovie(deletemovie){
      const movieindex = this.addedMovies.indexOf(deletemovie)
      this.addedMovies[movieindex].isCompleted = !this.addedMovies[movieindex].isCompleted
    }
  }
}
</script>

<style>

</style>