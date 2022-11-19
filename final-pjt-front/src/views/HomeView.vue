<template>
  <div>
    <router-link :to="{ name: 'ArticleView' }">Articles</router-link> | 
    <router-link :to="{ name: 'SignUpView' }" v-if="!isLogin">SignUpPage</router-link> | 
    <router-link :to="{ name: 'MovieView' }">MoviePage</router-link>
    <div>
      <router-link :to="{ name: 'LogInView' }" v-if="!isLogin">LogIn</router-link>
      <router-link :to="{ name: 'LogOutView' }" v-if="isLogin">LogOut</router-link>
    </div>
    <router-link :to="{ name: 'ProfileView', params: { username: username } }" v-if="isLogin">Profile</router-link>
    <!-- <div v-if="isLogin">
      <p>{{username}}님 환영합니다.</p>
    </div> -->
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