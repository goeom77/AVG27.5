import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)


const API_URL = 'http://127.0.0.1:8000'
// const MOVIE_API_KEY = process.env.VUE_APP_MOVIE_API_KEY
const MOVIE_API_KEY = '859b52ab552de5015f0e7dbaa748474e'
const LATEST_API_URL = `https://api.themoviedb.org/3/movie/now_playing?api_key=${MOVIE_API_KEY}&language=ko-kr&page=1`


export default new Vuex.Store({
  plugins: [
    createPersistedState() // 계산 된 값을 유지
  ],
  state: {
    articles: [],
    movies: [],
    movie_latest: [],
    ////////////////////////////////////////accounts//////////////
    token: null,
    username: null,
    user: {},// user.pk
    profileuser: {},
    mbti: '',
  },
  getters: {
    ////////////////////////////////////////accounts//////////////
    isLogin(state) {
      return state.token ? true : false //로그인 상태면 true 아니면 false
    },
  },
  mutations: {
    MOVIE_DATA(state, moviedata) {
      state.movies = moviedata
    },
    MOVIE_LATEST(state, moviedata) {
      state.movie_latest = []
      state.movie_latest = moviedata
      moviedata.forEach(movie => {
        const movie_g = {
          id: movie.id,
          title: movie.title,
          genre_ids: movie.genre_ids,
          poster_path: movie.poster_path,
          overview: movie.overview,
          vote_average: movie.vote_average,
        }
        state.movies.push(movie_g)
    })},
    ////////////////////////////////////////accounts//////////////
    SIGN_UP(state, token) {
      state.token = token
    },
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    SAVE_USER(state, username) {
      state.username = username
    },
    LOG_OUT(state, islogin) {
      state.islogin = !islogin
      state.token = null
      state.user = {}
    },
    UPDATE_USER(state, username) {
      state.username = username
    },
    GET_USERNAME(state, username) {
      // console.log(username)
      state.username = username
    },
    GET_NOW_USER(state, payload) {
      // console.log(payload)
      state.user = payload
    },
    GET_PROFILE_USER(state, payload) {
      // console.log(payload)
      state.profileuser = payload
    },
    ////////////////////////////////////////articles//////////////
    ARTICLE_DELETE(state, article_id) {
      state.articles = state.articles.filter((article) => {
        return !(article.id === article_id)
      })
    },
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/articles/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          context.commit('GET_ARTICLES', res.data)
          this.$router.push({ name: 'ArticleView' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMovieData(context, moviedata) {
      context.commit('MOVIE_DATA', moviedata)
    },
    getMovieLatest(context){
      axios({
        method: 'get',
        url: `${LATEST_API_URL}`,
      })
        .then((res) => {
          context.commit('MOVIE_LATEST', res.data.results)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    ////////////////////////////////////////accounts//////////////
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: payload
      })
        .then((res) => {
          console.log(res.data)
          context.dispatch('getUsername', payload.username)
          router.push({ name: 'LogInView' })
        })
    },
    profileEdit(context, payload) {
      const username = payload.username
      axios({
        method: 'put',
        url: `${API_URL}/accounts/profile/${username}/`,
        data: payload,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then(() => {
          context.dispatch('getNowUser',username)
          router.push({name:'MovieView'})
        })
    },
    logIn(context, payload) {
      const username = payload.username
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: payload
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
          context.dispatch('getUsername', username)
          context.dispatch('getNowUser',username)
          router.push({ name: 'MovieView' })
          // context.commit('SET_PROFILE', res.data) 이 데이터가 뭐지? 유저 토큰 아닌가?
        })
        .catch((err) => 
          console.log(err))
    },
    getUsername(context, username) {
      context.commit('GET_USERNAME', username)
    },
    getNowUser(context,username) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${username}/`,
      })
        .then((res) => {
          // console.log(res.data)
          context.commit('GET_NOW_USER', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getProfileUser(context,payload) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${payload.username}/`,
      })
        .then((res) => {
          // console.log(res.data)
          context.commit('GET_PROFILE_USER', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logOut(context, islogin) {
      context.commit('LOG_OUT', islogin)
    },
    followPut(context, follow_id){
      axios({
        method: 'post',
        url: `${API_URL}/accounts/${follow_id}/follow/`,
        headers: {
          Authorization: `Token ${context.state.token}`},
      })
      .then((res) => {
          // console.log('follow상태')
          console.log(res)
      })
    },
    getUserInfo(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/users/`,
      })
        .then((res) => {
          context.commit('GET_USER_INFO', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      context.commit('GET_USER_INFO')
    },
    ////////////////////////////////////////articles//////////////
    ArticleDelete(context, article_id) {
      context.commit('ARTICLE_DELETE', article_id)
    },
  },
  modules: {
  }
})
