<template>
  <div>
    <nav id='nav' class="navbar">
      <ul class="nav">
        <li class="nav-item">
          <img src="https://cdn.discordapp.com/attachments/997060428385484880/1044398045946716311/image.png" alt="">
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'MovieView' }">Movie</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'ArticleView' }">Article</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" v-if="!isLogin" :to="{ name: 'SignUpView' }">SignUp</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'LogInView' }" v-if="!isLogin">LogIn</router-link>
          <router-link class="nav-link" :to="{ name: 'LogOutView' }" v-if="isLogin">LogOut</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'ProfileView', params: { username: username } }" v-if="isLogin">Profile</router-link>
        </li>
      </ul>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'HomeView',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
      },
    username() {
      return this.$store.state.username
    }
  },
  created() {
    this.getmoviedata()
    this.getmovielatest()
    this.getuserinfo()
  },
  methods: {
    getmoviedata() {
      const movie_length_latest = this.$store.movie_latest
      if (movie_length_latest === undefined) {
      const movie_length = this.$store.movies
      console.log(movie_length)
      axios.get(`${API_URL}/movies`)
        .then((res) => {
          this.$store.dispatch('getMovieData', res.data)
        })
        .catch((err) => { 
          console.log(err)
        })}
    },
    getmovielatest() {
      const movie_length = this.$store.movie_latest
      if (movie_length === undefined) {
      this.$store.dispatch('getMovieLatest')
      }
    },
    getuserinfo() {
      this.$store.dispatch('getUserInfo')
    }
  },
}
</script>

<style>
#nav {
  background-color: #232323;
}
</style>