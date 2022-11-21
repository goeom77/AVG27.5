<template>
  <div>
    <h1>Edit Page</h1>
    <form @submit.prevent="profileEdit">
      <label for="img"> 프로필 사진 : </label>
      <input type="file" ref="doc" id="img" @change="findImg"> 
      <br>  
      <label for="nickname"> nickname : </label>
      <input type="text" id="nickname" v-model="user.nickname"> 
      <br>  
      <label for="age"> 나이 : </label>
      <input type="number" min="0" max="150" id="age" v-model="user.age"> 
      <br> 
      <label for="mbti"> mbti : </label>
      <input type="text" id="mbti" v-model="user.mbti"> 
      <br>  
      <input type="submit" value="Edit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileEditView',
  data() {
    return {
      user: {},
    }
  },
  created() {
    this.getProfile()
  },
  methods: {
    getProfile() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${this.$route.params.username}/`,
      })
        .then((res) => {
          // console.log(res.data)
          this.user = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    findImg(event) {
      let payload = this.user;
      let reader = new FileReader()
      reader.onload = function(event) {
        payload.profile_img = event.target.result;
      }
      reader.readAsDataURL(event.target.files[0])
    },
    profileEdit() {
      const payload = this.user
      this.$store.dispatch('profileEdit', payload)
    }
  }
}
</script>
