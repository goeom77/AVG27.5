<template>
  <div>
    <h1>LogOut</h1>
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
        if (this.isLogin) {
            this.$store.dispatch('logIn',this.isLogin)
        } else {
            alert('잘못된 접근입니다')
            this.$router.back()
        }
    }

}
</script>

<style>

</style>