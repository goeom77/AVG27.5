<template>
  <div>
    <h1>ProfileView</h1>
    {{username}}님 환영합니다.
  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'ProfileView',
  computed: {
    username() {
      return this.$store.state.username
    }
  },
  // 여기서 로그인 정보를 확인하고 만약 로그인 되어있다면 개인 프로필로 들어가기
  // methods() {
    // getProfile() {
    //   axios({
    //   method: 'get',
    //   url: `${API_URL}/accounts/profile/${this.$route.params.username}/`,
    //   })
    //     .then((res) => {
    //       this.profileUser = res.data
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // }
  // }
}
</script>

<style>

</style>