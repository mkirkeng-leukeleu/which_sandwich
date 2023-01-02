<template>
  <div class="errorPage">
    <h1>Ooof, this is the error page.</h1>
    <p>We encountered an error with code: {{ error.statusCode }}</p>
    <br />
    <button @click="handleError">Let's go home!</button>
  </div>
</template>

<script>
export default {
  props: [
    'error'
  ],
  methods: {
    handleError() {
      console.log(this.error)
      clearError({ redirect: '/' })
    }
  }
}
</script>
