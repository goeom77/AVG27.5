<template>
  <div>
    <h5>글 번호 : {{ article.id }}</h5>
    <p>작성자 : {{ article.username }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>타입 : {{ article.type }}</p>
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
