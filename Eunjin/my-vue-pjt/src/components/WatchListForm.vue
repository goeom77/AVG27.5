<template>
  <div>
    <input 
      type="text"
      v-model="inputData"
      @keyup.enter="movieAdd"
    >
    <button @click="movieAdd" class="btn btn-info btn-sm" style="margin-left: 3px;">Add</button>
  </div>
</template>

<script> 
export default {
  name: 'WatchListForm',
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    movieAdd() {
      const movieItem = {
        inputDataKey: this.inputData,
        isCompleted: false,
      }
      this.$emit('movie-add', movieItem)
      this.inputData = null
    }
  }
}
</script>

<style>

</style>