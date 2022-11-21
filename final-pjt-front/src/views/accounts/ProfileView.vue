<template>
  <div>
    <h1>프로필</h1>
    <div>
      <img
        :src="profileuser.profile_img ? profileuser.profile_img : 'https://media.discordapp.net/attachments/997060428385484880/1042322474165096478/image.png'"
        alt="프로필 사진이 없습니다."
      />
    </div>
    <div>
      {{profileuser.followers.length ? profileuser.followers.length : '_'}}팔로워
      {{profileuser.followings.length ? profileuser.followings.length : '_'}}팔로잉
    </div>
  </div>

</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'ProfileView',
  computed: {
    isLogin() {
      return this.$store.gatters.isLogin
    },
    user() {
      return this.$store.state.user
    },
    profileuser() {
      return this.$store.state.profileuser
    },
    samePeople() {
      // true 같은 사람 false 다른 사람
      return this.$route.params.username === this.user.username
    },
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.getProfileData(payload)
  },
  methods: {
    getProfileData(payload) {
      // console.log(payload)
      this.$store.dispatch('getProfileUser', payload)
    }
  },
}
</script>

<style>

</style>