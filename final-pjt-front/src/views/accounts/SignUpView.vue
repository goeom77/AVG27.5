<template>
  <div>
    <img src="https://discord.com/channels/@me/997060428385484880/1044398046328402011" alt="">
    <div>
      <form @submit.prevent="signUp">
        <div>
          <label for="username">id : </label>
          <input type="text" id="username" v-model="payload.username"><br>
    
          <label for="password1"> password : </label>
          <input type="password" id="password1" v-model="payload.password1"><br>
    
          <label for="password2"> password confirmation : </label>
          <input type="password" id="password2" v-model="payload.password2">
          <br>
          <label for="img"> 프로필 사진 : </label>
          <input type="file" ref="doc" id="img" @change="findImg"> 
          <br>  
          <label for="nickname"> nickname : </label>
          <input type="text" id="nickname" v-model="payload.nickname"> 
          <br>  
          <label for="age"> 나이 : </label>
          <input type="number" min="0" max="150" id="age" v-model="payload.age"> 
          <br> 
          <label for="mbti"> mbti : </label>
          <input type="text" id="mbti" v-model="payload.mbti">  
        </div>
        <input type="submit" value="SignUp">
      </form>
    </div>
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
        nickname: '',
        age: 0,
        mbti: '',
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
