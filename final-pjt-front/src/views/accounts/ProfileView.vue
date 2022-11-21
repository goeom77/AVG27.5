<template>
  <div>
    <h1>프로필</h1>
    <div>
      <img
      :src="profileuser.profile_img ? profileuser.profile_img : 'https://media.discordapp.net/attachments/997060428385484880/1042322474165096478/image.png'"
      alt="프로필 사진이 등록해주세요."
      />
    </div>
    <div>
      이름 : {{user.nickname}}
    </div>
    <div>
      mbti : {{user.mbti}}
    </div>
    <div>
      <button v-if="samePeople"><span>Edit Profile</span></button>
      <div v-else @click="followPut(profileuser.pk)">
       <!-- v-else -->
        <button v-if="follow"><span>UnFollow</span></button>
        <button v-else><span>Follow</span></button>
      </div>
    </div>

    <div>
      {{profileuser.followers.length ? profileuser.followers.length : '_'}}팔로워
      {{profileuser.followings.length ? profileuser.followings.length : '_'}}팔로잉
    </div>
    <div>
      <div>
        <FollowUser/>
      </div>
    </div>
  </div>

</template>

<script>
import FollowUser from '@/components/profiles/FollowUser.vue'
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'
export default {
  
  name: 'ProfileView',
  components: {
    FollowUser,
  },
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
    follow() {
      return this.profileuser.pk in this.user.followers
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
    },
    followPut(profileuser_id) {
      this.$store.dispatch('followPut', profileuser_id)
    },
  },
}
</script>

<style>

</style>