<template>
  <div>
    
  </div>
</template>

<script>
export default {
  name: 'LogOut',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },                                                                                                                                                                 
  created() {
    console.log(this.isLogin)
    if (this.isLogin) {
      this.$store.dispatch('logOut',this.isLogin)
    } else {
      this.$router.back()
    }
  }

}
</script>

<style>

</style>