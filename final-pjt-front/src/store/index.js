import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)


const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  plugins: [
    createPersistedState() // 계산 된 값을 유지
  ],
  state: {
    articles: [],
    movies: [],
    ////////////////////////////////////////accounts//////////////
    token: null,
    username: null,
    profileuser: {},
    mbti: 'ESFJ',
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
    },
    UPDATE_USER(state, username) {
      state.username = username
    },
    GET_PROFILE_DATA(state, userdata) {
      state.profileuser = userdata
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
          // console.log(res, context)
          // console.log(res.data)
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
    ////////////////////////////////////////accounts//////////////
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: payload
      })
        .then((res) => {
          console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
          router.push({ name: 'ProfileView' })
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
          context.dispatch('getProfileData',username)
          router.push({ name: 'HomeView' })
          // context.commit('SET_PROFILE', res.data) 이 데이터가 뭐지? 유저 토큰 아닌가?
        })
        .catch((err) => 
          console.log(err))
      },
      getProfileData(context,username) {
        axios({
          method: 'get',
          url: `${API_URL}/accounts/profile/${username}/`,
        })
          .then((res) => {
            context.commit('GET_PROFILE_DATA', res)
          })
          .catch((err) => {
            console.log(err)
          })
      },
      logOut(context, islogin) {
        context.commit('LOG_OUT', islogin)
      },
      ////////////////////////////////////////articles//////////////
      ArticleDelete(context, article_id) {
        context.commit('ARTICLE_DELETE', article_id)
      },
  },
  modules: {
  }
})
