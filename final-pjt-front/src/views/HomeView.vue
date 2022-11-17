<template>
  <div>
    <router-link :to="{ name: 'ArticleView' }">Articles</router-link> | 
    <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> | 
    <router-link :to="{ name: 'LogInView' }">LogInPage</router-link> |
    <router-link :to="{ name: 'MovieView' }">MoviePage</router-link>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'HomeView'
}
</script>

<style>

</style>