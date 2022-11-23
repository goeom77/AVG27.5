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
      // console.log('여기다!!',payload)
      // this.$store.dispatch('getProfileUser', payload)
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${people}/`,
        headers: {Authorization: `Token ${this.$store.state.token}`}
      })
        .then((res) => {
          console.log(res)
          // context.commit('GET_PROFILE_USER', res.data)
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