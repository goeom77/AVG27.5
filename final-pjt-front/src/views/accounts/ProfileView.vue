<template>
  <div>
    <h1>프로필</h1>
    {{profileuser}}
    <div class="imgbox">
      <img
      class="profile"
      :src="profileuser.profile_img ? profileuser.profile_img : 'https://media.discordapp.net/attachments/997060428385484880/1042322474165096478/image.png'"
      alt="프로필 사진을 등록해주세요."
      />
    </div>
    {{ profileuser.followers }}
    
    <div>
      이름 : {{profileuser.nickname}}
    </div>
    <div>
      mbti : {{profileuser.mbti}}
    </div>
    <div>
      <button v-if="samePeople">
        <router-link
        :to="{
          name: 'ProfileEditView',
          params: {
            username: user.username,
          },
        }"
        ><span>Edit Profile</span></router-link></button>
      <div v-else @click="followPut()">
      <!-- v-else -->
        <button v-if="follow" @click="postfollow"><span>UnFollow</span></button>
        <button v-else @click="postfollow"><span>Follow</span></button>
      </div>
    </div>

    <!-- <div>
      {{profileuser.followers.count ? profileuser.followers.count : '_'}}팔로워
      {{profileuser.followings.count ? profileuser.followings.count : '_'}}팔로잉
    </div> -->
    <div>
      <div>
        <p>팔로워</p>
        <ProfileMini
          v-for="people in profileuser.followers"
          :key="people.id"
          :people="people"
        />
      </div>
    </div>
  </div>

</template>

<script>
import ProfileMini from '@/components/profiles/ProfileMini'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'ProfileView',
  components: {
    ProfileMini,
  },
  data() {
    return {
      follow: false,
      profileuser: {},
    }
  },
  computed: {
    isLogin() {
      return this.$store.gatters.isLogin
    },
    user() {
      return this.$store.state.user
    },
    // profileuser() {
    //   return this.$store.state.profileuser
    // },
    samePeople() {
      // true 같은 사람 false 다른 사람
      // console.log('사람비교')
      // console.log(this.$route.params.username)
      // console.log(this.user.username)
      return this.$route.params.username === this.user.username
    },
  },
  created() {
    console.log( this.$route.params.username)
    const payload = { username: this.$route.params.username }
    this.getProfileData(payload)
    this.followCheck(payload)
  },
  methods: {
    getProfileData(payload) {
      // console.log('여기다!!',payload)
      // this.$store.dispatch('getProfileUser', payload)
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${payload.username}/`,
      })
        .then((res) => {
          this.profileuser = res.data
          // context.commit('GET_PROFILE_USER', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    followPut() {
      this.$store.dispatch('followPut',this.profileuser.username)
    },
    followCheck(payload) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/${payload.username}/follow/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.follow = res.data
      })
    },
    postfollow() {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/${this.$route.params.username}/follow/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.follow = res.data
      })
    }
  },
}

</script>

<style>
.imgbox {
  width: 150px;
  height: 150px; 
  border-radius: 70%;
  overflow: hidden;
}
.profile {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>