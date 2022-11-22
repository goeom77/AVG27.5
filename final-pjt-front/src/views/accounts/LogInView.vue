<template>
  <div class="login-card">
    <div>
      <img src="https://cdn.discordapp.com/attachments/997060428385484880/1044398045946716311/image.png" alt="">
    </div>
    <div class="login-card-div">
      <b-form @submit.prevent="logIn()" @reset="onReset">
        <div class="pt-5"></div>
        <div class="login-card-div-input">
          <b-form-group id="input-group-1" label="Your ID: " label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="payload.username"
              type="text"
              placeholder="Enter your ID"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-2" label="Password: " label-for="input-2">
            <b-form-input
              id="input-2"
              type="password"
              placeholder="Enter your Password"
              v-model="payload.password"
              required
              ></b-form-input>
            </b-form-group>
            <br>
            <br>
            <b-button type="submit" variant="primary">LOGIN</b-button>
            <b-button type="reset" variant="danger">Reset</b-button>
        </div>
  
      </b-form>
    </div>

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
      this.$store.dispatch('logIn', payload)
    },
    onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.payload.username = ''
        this.payload.password = ''
        // Trick to reset/clear native browser form validation state
      }
  }
}
</script>

<style>
.login-card {
  margin: 0 auto;
  margin-top: 100px;
  height: 100vh;
}
.login-card-div {
  padding: 0 auto;
  margin: 0 auto;
  min-height: 200px;
  min-width: 500px;
  height: 300px;
  width: 600px;
  background-color: #D9D9D9;
  border-radius: 10px;
}
.login-card-div-input {
  margin: 0 auto;
  min-height: 300px;
  min-width: 400px;
  height: 350px;
  width: 550px;
}
</style>