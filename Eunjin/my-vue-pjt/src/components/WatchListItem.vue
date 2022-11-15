<template>
  <div><br>
    <span
      @click="deleteMovie"
      :class="{ 'is-completed': movie.isCompleted }"
    >{{ movie.inputDataKey }}</span>
  </div>
</template>

<script>

export default {
  name: 'WatchListItem',
  props: {
    movie: Object,
  },
  methods: {
    deleteMovie() {
      this.$emit('delete_movie', this.movie)
    }
  }
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>