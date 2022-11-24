<template>
  <div>
    <!-- <p>{{ people }}</p> -->
    <!-- <p>{{ person }}</p> -->
    <div class="imgbox_mini">
      <img
      class="profile"
      :src="person.profile_img ? person.profile_img : 'https://media.discordapp.net/attachments/997060428385484880/1042322474165096478/image.png'"
      alt="프로필 사진을 등록해주세요."
      />
    </div>
    <div>
      {{person.nickname}}  {{person.mbti}}   |   
      <button @click="goprofile">{{pickmovies_count}}</button>
    </div>
    followers : {{ followers_count }}
    followings : {{ followings_count }}
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'ProfileMini',
  props: {
    people: [String, Number],
  },
  data(){
    return{
      person: [],
    }
  },
  created() {
    this.getProfileData(this.people)
  },
  computed: {
    followers_count() {
      return this.person.followers === [] ? this.person.followers.length : 0;
    },
    followings_count() {
      return this.person.followings === [] ? this.person.followings.length : 0;
    },
    pickmovies_count() {
      return this.person.pickmovies === [] ? this.person.pickmovies.length : 0;
    }
  },
  methods: {
    getProfileData(people) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/search/${people}/`,
        headers: {Authorization: `Token ${this.$store.state.token}`}
      })
        .then((res) => {
          console.log(res)
          this.person = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    goprofile() {
      console.log(this.person.username)
      this.$router.push({ name: 'ProfileMiniView' , params:{ username : this.person.username }})
    }
  }
}
</script>

<style>
.imgbox_mini {
  width: 50px;
  height: 50px; 
  border-radius: 70%;
  overflow: hidden;
}
</style>