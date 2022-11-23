<template>
  <div>
    <p>{{ people }}</p>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'ProfileMini',
  props: {
    people: [String],
  },
  created() {
    this.getProfileData(this.people)
  },
  methods: {
    getProfileData(people) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${people}/`,
        headers: {Authorization: `Token ${this.$store.state.token}`}
      })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}
</script>

<style>
</style>