<template>
  <div>
    <h2>제목 : {{ article.title }}</h2>
    <p>타입 : {{ article.type }}</p>
    <p>작성자 : {{ article.username }}</p>
    <router-link :to="{ name: 'DetailView', params: {id : article.id}  }">
      [DETAIL]
    </router-link>
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

</style>
