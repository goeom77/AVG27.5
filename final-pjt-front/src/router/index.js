import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleView from '@/views/articles/ArticleView'
import CreateView from '@/views/articles/CreateView'
import DetailView from '@/views/articles/DetailView'
import SignUpView from '@/views/accounts/SignUpView'
import LogInView from '@/views/accounts/LogInView'
import MovieView from '@/views/movies/MovieView'
import MovieDetailView from '@/views/movies/MovieDetailView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'ArticleView',
    component: ArticleView
  },

  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },

  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },

  {
    path: '/movies',
    name: 'MovieView',
    component: MovieView,
  },

  {
    path: '/movies/:id',
    name: 'detail',
    component: MovieDetailView,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
