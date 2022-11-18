<template>
  <div>
    <router-link :to="{ name: 'ArticleView' }">Articles</router-link> | 
    <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> | 
    <router-link :to="{ name: 'MovieView' }">MoviePage</router-link>  |
    <div v-if="!isLogin">
      <router-link :to="{ name: 'LogInView' }">LogIn</router-link>
    </div>
    <div v-if="isLogin">
      <router-link :to="{ name: 'LogOutView' }">LogOut</router-link>
    </div>
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
  }
}
</script>

<style>

</style>