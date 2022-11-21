<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="payload.username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="payload.password"><br>

      <input type="submit" value="logIn">
    </form>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      payload: {
        username: '',
        password: '',
      }
    }
  },
  computed: {
    isLogin() {
      return this.$store.gatters.isLogin
    },
  },
  created() {
    if (this.isLogin) {
      alert('로그아웃 후 진행해주세요!')
      this.$router.back()
    }
  },
  methods: {
    logIn() {
      const payload = this.payload
      console.log(payload)
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>
