<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: 'Welcome to the VueApp'
    }
  }
}
</script>

<style scoped>
.hello {
  text-align: center;
  margin-top: 20px;
}
</style>