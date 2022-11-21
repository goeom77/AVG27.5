<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="payload.username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="payload.password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="payload.password2">
      <br>
      <label for="img"> 프로필 사진 : </label>
      <input type="file" ref="doc" id="img" @change="findImg"> 
      <br>  
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      payload: {
        username: '',
        password1: '',
        password2: '',
        profile_img: '',
      }
    }
  },
  methods: {
    findImg(event) {
      let payload = this.payload;
      let reader = new FileReader()
      reader.onload = function(event) {
        payload.profile_img = event.target.result;
      }
      reader.readAsDataURL(event.target.files[0])
    },
    signUp() {
      // console.log(this.payload)
      const payload = this.payload
      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>
