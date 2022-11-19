<template>
  <div id="app" class=''>
    <nav class="navbar bg-secondary bg-opacity-10">
      <ul class="nav">
        <li class="nav-item">
          <h1 class="">Umm</h1>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'MovieView' }">MoviePage</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'ArticleView' }">Articles</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" v-if="!isLogin" :to="{ name: 'SignUpView' }">SignUp</router-link>
        </li>
        <div>
          <router-link :to="{ name: 'LogInView' }" v-if="!isLogin">LogIn</router-link>
          <router-link :to="{ name: 'LogOutView' }" v-if="isLogin">LogOut</router-link>
        </div>
        <li class="nav-item">
          <router-link :to="{ name: 'ProfileView', params: { username: username } }" v-if="isLogin">Profile</router-link>
        </li>
      </ul>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
      },
    username() {
      return this.$store.state.username
    }
  }
}
</script>

<style>

</style>