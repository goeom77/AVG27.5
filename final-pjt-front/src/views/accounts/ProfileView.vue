<template>
  <div>
    <h1>Profile</h1>
    <div>
      <img
        :src="currentuser.profile_img ? currentuser.profile_img : 'https://user-images.githubusercontent.com/90893428/169695116-afc5cb17-b075-43c9-9ff8-7c8155c8dd79.png'"
        alt="프로필 사진이 없습니다."
      />
    </div>
    <div>
      팔로워 : {{currentuser.followers.length ? currentuser.followers.length : 0}}
      팔로잉 : {{currentuser.followings.length ? currentuser.followings.length : 0}}
    </div>
  </div>

</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'ProfileView',
  computed: {
    currentuser() {
      return this.$store.state.currentuser
    },
    isLogin() {
      return this.$store.gatters.isLogin
    },
    // username() {
    //   return this.$store.state.username
    // }
  },
  created() {
    const payload = { username: this.$route.params.username };
    this.getProfileData(payload);
  },
  // methods() {
  //   getProfiledata(payload) {
  //     this.$store.dispatch('getProfileData',payload)
  //   }
  // }
}
</script>

<style>

</style>