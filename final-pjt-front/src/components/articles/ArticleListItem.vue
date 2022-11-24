<template>
  <div class="articlefont">
    <h2>{{ article.title }}</h2>
    <p>작성자 : {{ article.nickname }}</p>
    <p class="d-inline-block text-truncate" style="max-width: 400px;">{{ article.content }}</p>
    <p></p>
    <router-link :to="{ name: 'MovieDetailView', params: {id : article.id}  }">[DETAIL]</router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  }
}
</script>

<style>
.articlefont {
  color: #232323;
}
</style>
