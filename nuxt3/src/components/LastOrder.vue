<template>
  <div class="container">
    <div><h1>Last order</h1></div>
    <OrderView :orderData="orderData"/>
    <br/>
    <NuxtLink to="/">
      Go back to the homepage...
    </NuxtLink>
  </div>
</template>

<script>
export default {
    props: {
        orderData: {
            type: Object
        }
    }
}
</script>

<style scoped>
.container {
  display: block;
}
</style>
