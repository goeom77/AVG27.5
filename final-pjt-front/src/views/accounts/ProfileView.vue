<template>
  <div>
    <h1>프로필</h1>
    <!-- {{profileuser}} -->
    <div class="imgbox">
      <img
      class="profile"
      :src="profileuser.profile_img ? profileuser.profile_img : 'https://media.discordapp.net/attachments/997060428385484880/1042322474165096478/image.png'"
      alt="프로필 사진을 등록해주세요."
      />
    </div>
    
    <div>
      이름 : {{profileuser.nickname}} | 
      나이 : {{profileuser.age}} 
    </div>
    <div>
      mbti : {{profileuser.mbti}}
    </div>
    <p>followers : {{ profileuser.followers.length ? profileuser.followers.length : 0}} | 
    followings : {{ profileuser.followings.length ? profileuser.followings.length : 0 }}</p>
    <p>PIck :{{ profileuser.pickmovies.length ? profileuser.pickmovies.length : 0}} | 
    Wish :{{ profileuser.wishmovies.length ? profileuser.wishmovies.length : 0}} </p> 
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
    <div>
      <h5>{{profileuser.nickname}}님 PICK</h5>
      <div class="mainitem">
        <MovieCardListItem2
          v-for="movie in profileuser.pickmovies"
          :key="movie.id"
          :movie="movie"
        />
      </div>
      <hr>
      <h5>{{profileuser.nickname}}님 WISH</h5>
      <div class="mainitem">
        <MovieCardListItem2
          v-for="movie in profileuser.wishmovies"
          :key="movie.id"
          :movie="movie"
        />
      </div>
    </div>
    <div>
      <div>
        <hr>
        <h1>followers</h1>
        <ProfileMini
          v-for="people in profileuser.followers"
          :key="people.id"
          :people="people"
        />
        <hr>
      </div>
      <div>
        <h1>followings</h1>
        <ProfileMini
          v-for="people in profileuser.followings"
          :key="people.id"
          :people="people"
        />
      </div>
    </div>
  </div>

</template>

<script>
import MovieCardListItem2 from '@/components/movies/MovieCardListItem2'
import ProfileMini from '@/components/profiles/ProfileMini'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'ProfileView',
  components: {
    ProfileMini,
    MovieCardListItem2,
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
    samePeople() {
      return this.$route.params.username === this.user.username
    },
    followers_count() {
      return this.profileuser.followers === [] ? this.profileuser.followers.length : 0;
    },
    followings_count() {
      return this.profileuser.followings === [] ? this.profileuser.followings.length : 0;
    },
    pickmovies_count() {
      return this.profileuser.pickmovies === [] ? this.profileuser.pickmovies.length : 0;
    },
    wishmovies_count() {
      return this.profileuser.wishmovies === [] ? this.profileuser.wishmovies.length : 0;
    }
  },
  created() {
    // console.log( this.$route.params.username)
    const payload = { username: this.$route.params.username }
    this.getProfileData(payload)
    this.followCheck(payload)
  },
  methods: {
    getProfileData(payload) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${payload.username}/`,
      })
        .then((res) => {
          this.profileuser = res.data
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
          const payload = { username: this.$route.params.username }
          this.getProfileData(payload)
          
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